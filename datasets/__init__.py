import json
import requests
import csv
import sys
import re
import gspread
import frontmatter
import os
from datetime import datetime
from urllib.parse import urlparse

def write_worksheet_to_csv(data, metadata, file):
	print(file)
	with open(file, "w", newline="") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerows(data)
		writer.writerow(metadata)


def parse_and_submit(new_file, sheet_id, output_dir, creds):

	#get google sheet object
	scope = ["https://spreadsheets.google.com/feeds"]
	gc = gspread.service_account_from_dict(creds, scope)

	#download google sheet
	sheet = gc.open_by_key(key=sheet_id)
	try:
		ws = sheet.worksheets()[0]
	except gspread.exceptions.APIError:
		raise Exception(f"failed to download sheet")

	data = ws.get()

	#get citation metadata associated with file
	dataset = frontmatter.load(new_file)
	parsed_url = urlparse(dataset['url'])
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url.netloc + parsed_url.path + parsed_url.params
	wiki_req = re.sub(r'\/$', '', wiki_req)
	wiki_res = requests.get(wiki_req)
	result = wiki_res.json()[0]
	# print(result)

	bib_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/bibtex/' + parsed_url.netloc + parsed_url.path + parsed_url.params
	bib_req = re.sub(r'\/$', '', bib_req)
	citation = requests.get(bib_req).text
	# print(citation)

	tag_arr = []
	tags = (list(map(lambda item: item["tag"].split(', '), result["tags"])))
	flat_tags = [val for sublist in tags for val in sublist]

	try:
		#crosswalk zotero to sheet schema
		#cast to strings to append to google sheet
		metadata = [
			str(result["title"]), # Title
			str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), # Record Creation Timestamp
			str(result["url"]), # URL
			str(result["extra"] if "DOI" in result["extra"] else ''), # DOI?
			" ", # I3 member author?
			' ', # additional metadata?
			str(result["abstractNote"]), # Description
			" ", # Terms of use
			" ", # Timeframe
			" ", # Documentation
			" ", # Performance/error metrics
			str(citation), # Citation
			" ", # Open-source code
			" ", # Versioning
			" ", # API or Bulk downloads
			str(flat_tags), # Keywords associated with this dataset
			" " # Datasets and publications using this dataset
		]
	except:
		e = sys.exc_info()[0]
		print('could not fetch metadata', e)

	#first, append to csv (write updated sheet in case of any changes)
	try:
		filename = os.path.join(output_dir, "Open_Patent_Datasets.csv")
		write_worksheet_to_csv(data, metadata, filename)
	except:
		e = sys.exc_info()[0]
		print('issue writing to csv', e)

	#then, push row to google sheet
	try:
		ws.append_row(metadata, value_input_option='RAW', insert_data_option='INSERT_ROWS')
	except:
		e = sys.exc_info()[0]
		print('could not write to google sheet', e)

