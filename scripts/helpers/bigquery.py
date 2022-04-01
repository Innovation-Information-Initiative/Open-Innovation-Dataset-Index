import sys
sys.path.append('scripts/libraries')
import google
from google.cloud import bigquery


# Construct a BigQuery client object.
client = bigquery.Client()
datasets = client.list_datasets('patcit-public-data')

field_set = set()

for dataset in datasets:
	tables = client.list_tables(dataset)
	for table_ref in tables:
		# table = bigquery.Table(table_list)
		table = client.get_table(table_ref)
		for field in table.schema:
			field_set.add(field.name)

# print(list(field_set))