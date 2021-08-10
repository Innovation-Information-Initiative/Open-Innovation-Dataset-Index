import json
import requests
import csv
import sys
import re
import gspread
import frontmatter
import pandas as pd
from datetime import datetime
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
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url.netloc + parsed_url.path + parsed_url.params
	wiki_req = re.sub(r'\/$', '', wiki_req)
	wiki_res = requests.get(wiki_req)
	result = wiki_res.json()[0]

	bib_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/bibtex/' + parsed_url.netloc + parsed_url.path + parsed_url.params
	bib_req = re.sub(r'\/$', '', bib_req)
	citation = requests.get(bib_req)

	print(list(map(lambda item: item["tag"].split(), result["tags"])))

	# try:
		#crosswalk zotero to sheet schema
	metadata = {
		"Title": result["title"],
		"Record Creation Timestamp": datetime.now(),
		"URL": result["url"],
		"DOI?": result["extra"] if "DOI" in result["extra"] else '',
		"I3 member author?": "",
		"Would you like to add additional metadata?": '',
		"Description": result["abstractNote"],
		"Terms of use": "",
		"Timeframe": "",
		"Documentation": "",
		"Performance/error metrics": "",
		"Citation": citation,
		"Open-source code": "",
		"Versioning": "",
		"API or Bulk downloads": "",
		"Keywords associated with this dataset": list(map(lambda item: item["tag"], result["tags"])),
		"Datasets and publications using this dataset": ""
	}

	new_df = pd.json_normalize(metadata)
	df = df.append(new_df, verify_integrity=True)
	print(df)
	# except:
	# 	e = sys.exc_info()[0]
	# 	print('could not fetch metadata', e)

	#if nothing returned, just append title and url (in future append message to PR)


	# format as json object


	# # add an empty row to the sheet 
	# # ws.resize(1)
	# # (don't overwrite the whole file or it makes it illegible)
	# # ws.append_row(row)