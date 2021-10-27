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
	# raw_data = gsheets.get(ws)
	# data, schema = gsheets.json_from_data(raw_data)
	sheet_df, schema = gsheets.get_df(ws)

	#generate UUID for entry and write to file
	record = frontmatter.load(filepath)
	dataset = {}

	print('head is', sheet_df.head())

	#copy submitted info from markdown to record
	for field in sheet_df.head():
		if field in record: 
			dataset[field] = record[field]
		else:
			dataset[field] = ''


	#get citation
	result, bibtex = metadata.citoid_request(record['location'])

	gsheets.post(ws, row)


if __name__ == "__main__":
	filepath = os.path.join(get_project_root(), sys.argv[1])

	parse_and_submit(
		edited_file = filepath,
		sheet_id = os.environ.get("INPUT_SHEET_ID"),
		sheet_title = 'Open_Patent_Datasets',
		output_dir = os.environ.get("INPUT_TEMPDIR"),
		creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	)

	print("processed", filepath)
