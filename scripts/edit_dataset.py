import os
import uuid
import frontmatter
import sys
import json
from datetime import datetime
import pandas as pd

from helpers import files, gsheets, metadata
from helpers.utils import get_project_root

def parse_and_submit(edited_file, sheet_id, sheet_title, output_dir, creds):
	#download google sheets
	ws = gsheets.init(sheet_id, sheet_title, creds)
	sheets_record, schema = gsheets.get_df(ws)

	#generate UUID for entry and write to file
	file_record = frontmatter.load(edited_file)
	ind = sheets_record.index[sheets_record['uuid']==file_record['uuid']].tolist()[0]

	for key in file_record.keys():
		if key in list(sheets_record.columns.values):
			sheets_record.at[ind, key] = file_record[key]

	sheets_record.at[ind, 'last_edit'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	sheets_record.columns=schema
	gsheets.post_df(ws, sheets_record)


if __name__ == "__main__":
	filepath = os.path.join(get_project_root(), sys.argv[1])

	parse_and_submit(
		edited_file = filepath,
		sheet_id = os.environ.get("INPUT_SHEET_ID"),
		sheet_title = 'Open_Innovation_Datasets',
		output_dir = os.environ.get("INPUT_TEMPDIR"),
		creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	)

	print("processed", filepath)
