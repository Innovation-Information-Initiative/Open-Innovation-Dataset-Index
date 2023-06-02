# python script to version the google sheet
import json
import os
import pkg_resources
import subprocess
from datetime import time
import pandas as pd
import sys
sys.path.append('scripts/libraries')

import google
from google.cloud import bigquery

from helpers import gsheets, files, metadata, timing
from helpers.utils import get_project_root
from helpers.sprites import create_sprites

archive_targets = ['Open_Innovation_Datasets']

# go through every entry in gsheet

# check metadata updates
# update metadata


def update_metadata(sheets, output_dir, creds):
	os.makedirs(output_dir, exist_ok=True)

	for i, sh in enumerate(sheets):
		ws = gsheets.init(sh["id"], sh["title"], creds)
		data = gsheets.get(ws)

		filename = os.path.join(output_dir, f"{sh['title']}.csv")

		if sh["title"] in archive_targets:
			data, headers = gsheets.json_from_data(data)
			data, update_metadata = metadata.get_metadata(data)

			md_path = os.path.join(get_project_root(), sh["directory"])
			files.update_markdown(data, md_path)

		files.write_csv_from_dict(data, filename)
		print(f"sheet written to {filename}")

		# push schema changes back to gsheet
		if update_metadata:
			data_df = pd.DataFrame.from_dict(data)
			data_df.colums = headers
			gsheets.post_df(ws, data_df)


if __name__ == "__main__":
	if os.environ.get("ENV") == 'local':
		f = open('keys/sheets_key.json')
		creds = json.load(f)
	else:
		creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	sheets = json.loads(os.environ.get("INPUT_SHEETS", "{}"))
	output_dir = os.environ.get("INPUT_TEMPDIR")

	client = bigquery.Client()

	update_metadata(
		sheets=sheets,
		output_dir=os.path.join(get_project_root(), output_dir),
		creds=creds,
	)
