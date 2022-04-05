import sys
sys.path.append('scripts/libraries')
import google
from google.cloud import bigquery
from furl import furl
from datetime import datetime

client = bigquery.Client()

def check_bigquery(data):
	bq_fields = []
	for row in data:
		if 'bigquery' in row and row['bigquery'].strip() != '':
			bq_fields.append({'uuid': row['uuid'], 'bq_url': row['bigquery']})
	return bq_fields


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

def get_schemas(data):
	update_metadata = False
	bq_fields = check_bigquery(data)
	bq_projects = get_bq_datasets(bq_fields)

	for project in bq_projects:
		project['schema'] = ', '.join(get_schema_fields(project))

	for row in data:
		project = next((item for item in bq_projects if item["uuid"] == row["uuid"]), None)
		if project is not None:
			# do we need to update the sheet
			if 'schema_fields' in row and project['schema'] != row['schema_fields']:
				update_metadata = True
			elif 'schema_fields' not in row:
				update_metadata = True
			row['schema_fields'] = project['schema']
			row['last_edit'] =  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			print('added fields to', row['title'])

	return data, update_metadata

