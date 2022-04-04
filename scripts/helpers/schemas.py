import sys
sys.path.append('scripts/libraries')
import google
from google.cloud import bigquery
from furl import furl

client = bigquery.Client()

def check_bigquery(data):
	bq_fields = []
	for row in data:
		if 'bigquery' in row and row['bigquery'].strip() != '' and 'schema' not in row:
			print(row['title'], row['bigquery'])
			bq_fields.append({'uuid': row['uuid'], 'bq_project': row['bigquery']})
	return bq_fields


def get_schema_fields(dataset_id):
	field_set = set()

	for dataset in datasets:
		tables = client.list_tables(dataset)
		for table_ref in tables:
			# table = bigquery.Table(table_list)
			table = client.get_table(table_ref)
			for field in table.schema:
				field_set.add(field.name)

	return list(field_set)

def get_bq_datasets(bq_fields):
	for project in bq_projects:
		# is the url for a bigquery project at all?
		if 'bigquery' in project['bigquery']:
			url_args = furl(project['bigquery'])
			print(url_args)
			# is this an actual BQ page or a marketplace page?
			# is it for a project or a dataset?
			# append array of datasets for each field

def get_schemas(data):
	bq_fields = check_bigquery(data)
	bq_datasets = get_bq_datasets(bq_fields)

	return data

