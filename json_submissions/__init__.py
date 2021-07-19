import json
import requests
import csv
import logging
import os
import gspread

def parse_and_submit(sheet_id, output_dir, creds):
	scope = ["https://spreadsheets.google.com/feeds"]
	gc = gspread.service_account_from_dict(creds, scope)

	with open(os.environ.get("INPUT_FILE"), 'r') as json_file:
		data = json.load(json_file)

	row=[]
	for attribute, value in data:
		row.append(value)

	#append to google sheet
	sheet = gc.open_by_key(key=sheet_id)
	try:
		ws = sheet.worksheets()[0]
	except gspread.exceptions.APIError:
		raise Exception(f"failed to download sheet {sh}")

	# add an empty row to the sheet 
	# ws.resize(1)
	# (don't overwrite the whole file or it makes it illegible)
	ws.append_row(row)