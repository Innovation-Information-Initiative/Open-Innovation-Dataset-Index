# python script to version the google sheet
import json
import os
import pkg_resources
import subprocess
from datetime import time
import pandas as pd

from helpers import gsheets, files, schemas, timing
from helpers.utils import get_project_root
from helpers.sprites import create_sprites

archive_targets = ['Open_Innovation_Datasets', 'Innovation_Data_Toolkit']


def archive_gsheet(sheets, output_dir, creds):
	os.makedirs(output_dir, exist_ok=True)

	for i, sh in enumerate(sheets):
		ws = gsheets.init(sh["id"], sh["title"], creds)
		data = gsheets.get(ws)

		filename = os.path.join(output_dir, f"{sh['title']}.csv")

		if sh["title"] in archive_targets:
			data, headers = gsheets.json_from_data(data)

			if timing.check_day_period(0, time(00,00), time(00,30)):
				data, update_metadata = schemas.get_schemas(data)
			else:
				update_metadata = False
			md_path = os.path.join(get_project_root(), sh["directory"])
			new_files = files.generate_markdown(data, md_path)
			create_sprites(new_files)
			files.update_markdown(data, md_path)

		files.write_csv_from_dict(data, filename)
		print(f"sheet written to {filename}")

		# push schema changes back to gsheet
		if update_metadata:
			data_df = pd.DataFrame.from_dict(data)
			data_df.colums = headers
			gsheets.post_df(ws, data_df)


if __name__ == "__main__":
	creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	sheets = json.loads(os.environ.get("INPUT_SHEETS", "{}"))
	output_dir = os.environ.get("INPUT_TEMPDIR")

	archive_gsheet(
		sheets=sheets,
		output_dir=os.path.join(get_project_root(), output_dir),
		creds=creds,
	)
