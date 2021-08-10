import json
import requests
import csv
import logging
import os
import re
import gspread
import frontmatter
import pandas as pd
from urllib.parse import urlparse

def parse_and_submit(new_file, sheet_id, output_dir, creds):

	#get google sheet object
	scope = ["https://spreadsheets.google.com/feeds"]
	gc = gspread.service_account_from_dict(creds, scope)

	#download google sheet
	sheet = gc.open_by_key(key=sheet_id)
	try:
		ws = sheet.worksheets()[0]
	except gspread.exceptions.APIError:
		raise Exception(f"failed to download sheet {sh}")

	data = ws.get()
	df = pd.DataFrame(data)
	print(df)

	#get citation metadata associated with file
	dataset = frontmatter.load(new_file)
	parsed_url = urlparse(dataset['url'])
	req = 'https://en.wikipedia.org/api/rest_v1/data/citation/zotero/' + parsed_url.netloc + parsed_url.path + parsed_url.params
	req = re.sub(r'\/$', '', req)

	res = requests.get(req)
	json = res.json()
	print(json)

	if len(json.items) > 0:
		print('length is greater than 0')
	else:
		print('length is 0')

	#if nothing returned, just append title and url (in future append message to PR)


	# format as json object


	# # add an empty row to the sheet 
	# # ws.resize(1)
	# # (don't overwrite the whole file or it makes it illegible)
	# # ws.append_row(row)