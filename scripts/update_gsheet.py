import os
import uuid
import frontmatter
import sys
import json
from datetime import datetime
import pandas as pd

from helpers import files, gsheets
from helpers.utils import get_project_root

def parse_and_submit(record_uuid, update_col, update_payload, sheet_id, sheet_title, output_dir, creds):
	#download google sheets
	ws = gsheets.init(sheet_id, sheet_title, creds)
	sheets_record, schema = gsheets.get_df(ws)

	#get index of record with matching uuid
	ind = sheets_record.index[sheets_record['uuid']==record_uuid].tolist()[0]

	print(schema)
	print(sheets_record.columns.values)

	if update_col in list(sheets_record.columns.values):
		relationships = sheets_record.at[ind, update_col].replace("'", '"')

		try:
			relationships = json.loads(relationships)
		except:
			print('existing relationships not in list form')

		if isinstance(relationships, list):
			relationships.append(update_payload)
			rships_no_dup = [i for n, i in enumerate(relationships) if i not in relationships[n + 1:]]
			print('before', relationships, 'after', rships_no_dup)
			sheets_record.at[ind, update_col] = rships_no_dup
		else:
			sheets_record.at[ind, update_col] = [update_payload]

	sheets_record.at[ind, 'last_edit'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	sheets_record.columns=schema
	gsheets.post_df(ws, sheets_record)


if __name__ == "__main__":
	uuid = sys.argv[1]
	update_col = sys.argv[2]

	payload =  json.loads(os.environ.get("rship", "{}"))
	print("input is", payload, payload['uuid'], payload['shortname'])

	f = open('keys/sheets_key.json')
	creds = json.load(f)
	# creds =  json.loads(os.environ.get("INPUT_CREDS", "{}"))

	parse_and_submit(
		record_uuid = uuid,
		update_col = update_col,
		update_payload = payload,
		sheet_id = os.environ.get("INPUT_SHEET_ID"),
		sheet_title = 'Open_Innovation_Datasets',
		output_dir = os.environ.get("INPUT_TEMPDIR"),
		creds = creds
	)

	print("processed relationship update")
