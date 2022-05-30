import sys
sys.path.append('scripts/libraries')
import google
from google.cloud import bigquery
from furl import furl
from datetime import datetime
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'keys/sheets_key.json'
client = bigquery.Client()

def check_bigquery(data):
	bq_fields = []
	for row in data:
		if 'bigquery' in row and row['bigquery'].strip() != '':
			bq_fields.append({'uuid': row['uuid'], 'bq_url': row['bigquery']})
	return bq_fields


def match_salient_fields(salient_fields_path, fields_list):
	salient_fields = pd.read_csv(salient_fields_path, header=0)
	suggestions = []
	for field_name in salient_fields['Name'].values:
		possibilities = []
		for field in fields_list:
			ratio = fuzz.ratio(field, field_name)
			if ratio > 60:
				possibilities.append({
					'field': field,
					'salient_field': field_name,
					'score': ratio
					})
		if len(possibilities) > 0:
			top_suggestion = sorted(possibilities, key=lambda poss: poss['score'])[0]
			suggestions.append(top_suggestion)
	if len(suggestions) > 0:
		print(row['title'], suggestions)

	return suggestions


def get_schema_fields(bq_project):
	field_set = set()
	print('project is', bq_project['project'])
	try:
		client = bigquery.Client(bq_project['project'])
	except:
		print("couldn't find project ", bq_project['project'])
		return []

	for dataset in bq_project['datasets']:
		try:
			tables = client.list_tables(dataset)
			print('dataset is', dataset)
			for table_ref in tables:
				table = client.get_table(table_ref)
				for field in table.schema:
					field_set.add(field.name)
		except:
			print("couldn't find dataset")
			return []

	return list(field_set)


def get_bq_datasets(bq_fields):
	for bq_project in bq_fields:
		# is the url for a bigquery project at all?
		if 'bigquery' in bq_project['bq_url']:
			url_args = furl(bq_project['bq_url']).args
			bq_project['project'] = url_args['p']

			# get the datasets in project
			if url_args['page'] == 'project':
				bq_project['datasets'] = []
				datasets = client.list_datasets(url_args['p'])
				for dataset in datasets:
					bq_project['datasets'].append(dataset.dataset_id)

			# if it's just that dataset, get and put in array
			elif url_args['page'] == 'dataset' or url_args['page'] == 'table':
				bq_project['datasets'] = [url_args['d']]

		# for marketplace pages, get id and dataset from url
		elif 'marketplace' in bq_project['bq_url']:
			project, dataset = bq_project['bq_url'].split('/')[-2:]
			print(project, dataset)
			bq_project['project'] = project

			#account for name change -- should find a better solution to this
			if bq_project['project'] == 'google_patents_public_datasets' or 'google_patents_public_datasets': 
				bq_project['project'] = 'patents-public-data'
			bq_project['datasets'] = [dataset]

		else:
			print('record does not link to bigquery dataset', project['bq_url'])

	return bq_fields

def get_schemas(data, salient_fields_path):
	update_metadata = False
	bq_fields = check_bigquery(data)
	bq_projects = get_bq_datasets(bq_fields)

	for project in bq_projects:
		project['schema'] = get_schema_fields(project)

	for row in data:
		project = next((item for item in bq_projects if item["uuid"] == row["uuid"]), None)
		if project is not None:
			# do we need to update the sheet
			# convert row back to list -> sets and then compare
			if 'schema_fields' in row:
				row_schema_list = row['schema_fields'].split(', ')
				if set(project['schema']) != set(row_schema_list) and row_schema_list != ['']:
					print("sets don't match")
					update_metadata = True
					row['schema_fields'] = ', '.join(project['schema'])
			else:
				print("field doesn't exist")
				update_metadata = True
				row['schema_fields'] = ', '.join(project['schema'])

			# match salient fields
			salient_fields = match_salient_fields(salient_fields_path, project['schema'])
			if 'salient_fields' in row:
				row_salient_fields = row['salient_fields'].split(', ')
				if set(salient_fields) != set(row_salient_fields):
					update_metadata = True
					row['schema_fields'] = ', '.join(salient_fields)
			else:
				update_metadata = True
				row['salient_fields'] = ', '.join(salient_fields)

			if update_metadata == True:
				row['last_edit'] =  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

			print('added fields to', row['title'])

	return data, update_metadata

