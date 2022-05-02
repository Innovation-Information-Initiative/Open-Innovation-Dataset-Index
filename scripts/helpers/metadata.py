# this file handles requests to external APIs
# (citoid, bigquery, dataverse, zenodo) to retrieve
# additional metadata about a source
import urllib.parse
import requests
import json
import sys
sys.path.append('scripts/libraries')
import google
from google.cloud import bigquery
from furl import furl
from datetime import datetime
import sickle

client = bigquery.Client()

def check_oai(data):
	oai_entries = []
	oai_mappings = {
		'dataverse.harvard.edu': 'http://dataverse.harvard.edu//oai',
		# 'zenodo.org': 'https://zenodo.org/oai2d',
	}

	for substring, endpoint in oai_mappings.items():
		for row in data:
			if 'location' in row and substring in row['location']:
				oai_entries.append({'uuid': row['uuid'], 'location': row['location'], 'endpoint': endpoint})

	return oai_entries


def check_bigquery(data):
	bq_fields = []
	for row in data:
		if 'bigquery' in row and row['bigquery'].strip() != '':
			bq_fields.append({'uuid': row['uuid'], 'location': row['bigquery']})
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
		if 'bigquery' in bq_project['location']:
			url_args = furl(bq_project['location']).args
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
		elif 'marketplace' in bq_project['location']:
			project, dataset = bq_project['location'].split('/')[-2:]
			print(project, dataset)
			bq_project['project'] = project

			#account for name change -- should find a better solution to this
			if bq_project['project'] == 'google_patents_public_datasets' or 'google_patents_public_datasets': 
				bq_project['project'] = 'patents-public-data'
			bq_project['datasets'] = [dataset]

		else:
			print('record does not link to bigquery dataset', project['location'])

	return bq_fields

def get_bq_metadata(data):
	bq_fields = check_bigquery(data)
	bq_projects = get_bq_datasets(bq_fields)

	for project in bq_projects:
		project['schema_fields'] = get_schema_fields(project)

	return bq_projects

def citoid_request(url):
	parsed_url = urllib.parse.quote(url, safe=" ")
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url
	wiki_res = requests.get(wiki_req)

	bib_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/bibtex/' + parsed_url
	bibtex = requests.get(bib_req).text

	result = wiki_res.json()

	print(wiki_res.json())
	try:
		result = wiki_res.json()[0]
	except:
		print('could not complete request')
		return None

	return result, bibtex

def get_citation_metadata(data):

	return projects


def get_oai_metadata(data):
	projects = check_oai(data)
	print(projects)

	return []


def get_metadata(data):
	update_metadata = False

	# check if OAI repo (dv, zenodo to start)
	projects = get_oai_metadata(data)
	projects = projects + get_bq_metadata(data) 

	# add all the updates
	for row in data:
		project = next((item for item in projects if item["uuid"] == row["uuid"]), None)
		if project is not None:
			# do we need to update the sheet
			# convert row back to list -> sets and then compare
			row_schema_list = row['schema_fields'].split(', ')
			if 'schema_fields' in row and set(project['schema']) != set(row_schema_list) and row_schema_list != ['']:
				print("sets don't match")
				update_metadata = True
				row['last_edit'] =  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
				row['schema_fields'] = ', '.join(project['schema'])
			elif 'schema_fields' not in row:
				print("field doesn't exist")
				update_metadata = True
				row['last_edit'] =  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
				row['schema_fields'] = ', '.join(project['schema'])
			print('added fields to', row['title'])


# todo: add bigquery, dataverse, zenodo requests