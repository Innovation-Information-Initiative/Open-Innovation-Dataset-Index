# python script to version the google sheet
import json
import os
import pkg_resources
import subprocess

from helpers import gsheets, files
from helpers.utils import get_project_root
from helpers.sprites import create_sprites

archive_targets = ['Open_Innovation_Datasets', 'Innovation_Data_Toolkit']

def check_bigquery(data):
	bq_fields = []
	for row in data:
		if 'bigquery' in row and row['bigquery'].strip() != '' and 'schema' not in row:
			print(row['title'], row['bigquery'])
	return bq_fields

def archive_gsheet(sheets, output_dir, creds):
	os.makedirs(output_dir, exist_ok=True)

	for i, sh in enumerate(sheets):
		ws = gsheets.init(sh["id"], sh["title"], creds)
		data = gsheets.get(ws)

		filename = os.path.join(output_dir, f"{sh['title']}.csv")
		files.write_csv(data, filename)

		if sh["title"] in archive_targets:
			data, schema = gsheets.json_from_data(data)
			md_path = os.path.join(get_project_root(), sh["directory"])
			new_files = files.generate_markdown(data, md_path)
			create_sprites(new_files)
			files.update_markdown(data, md_path)
			bq_fields = check_bigquery(data)

			if len(bq_fields) > 0:
				print('bq fields true')
				# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'google-cloud-bigquery'])

		print(f"sheet written to {filename}")

if __name__ == "__main__":
	creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	sheets = json.loads(os.environ.get("INPUT_SHEETS", "{}"))
	output_dir = os.environ.get("INPUT_TEMPDIR")

	archive_gsheet(
		sheets=sheets,
		output_dir=os.path.join(get_project_root(), output_dir),
		creds=creds,
	)
