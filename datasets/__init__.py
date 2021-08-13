import json
import requests
import csv
import sys
import re
import gspread
import frontmatter
import os
import uuid
import urllib.parse
from datetime import datetime

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

	#get metadata associated with dataset
	dataset = frontmatter.load(new_file)
	parsed_url = urllib.parse.quote(dataset['url'], safe='')
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url
	wiki_res = requests.get(wiki_req)
	try:
		result = wiki_res.json()[0]
	except:
		print('could not complete request')
		return

	#generate UUID for entry and write to file
	rec_uuid = uuid.uuid4()
	dataset['uuid'] = str(rec_uuid)
	f = open(new_file, "w")
	f.write(frontmatter.dumps(dataset))
	f.close()

	# if it's a webpage, zotero did not complete request
	if 'itemType' in result and result['itemType'] == 'webpage':
		print('no citation metadata available for this source')
		metadata = [
				str(rec_uuid),
				str(dataset["title"]), # Title
				str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), # Record Creation Timestamp
				str(dataset["url"]), # URL
				" " # DOI?
				" ", # I3 member author?
				" ", # additional metadata?
				str(dataset["description"] if "description" in dataset else ''), # Description
				" ", # Terms of use
				" ", # Timeframe
				" ", # Documentation
				" ", # Performance/error metrics
				str(dataset["citation"] if "citation" in dataset else ''), # Citation
				" ", # Open-source code
				" ", # Versioning
				" ", # API or Bulk downloads
				str("".join(dataset["tags"]) if "tags" in dataset else ''), # Keywords associated with this dataset
				" " # Datasets and publications using this dataset
		]


	else:
		tags = (list(map(lambda item: item["tag"].split(', '), result["tags"])))
		flat_tags = [val for sublist in tags for val in sublist]

		# get citation associated with dataset
		bib_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/bibtex/' + parsed_url
		citation = requests.get(bib_req).text

		try:
			#crosswalk zotero to sheet schema
			#cast to strings to append to google sheet
			metadata = [
				str(rec_uuid),
				str(result["title"] if result["title"] else dataset["title"]), # Title
				str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), # Record Creation Timestamp
				str(result["url"]if result["url"] else dataset["url"]), # URL
				str(result["extra"] if "DOI" in result["extra"] else ''), # DOI?
				" ", # I3 member author?
				' ', # additional metadata?
				str(dataset["description"] if "description" in dataset 
					else result["abstractNote"] 
					if "abstractNote" in result else ''), # Description
				" ", # Terms of use
				" ", # Timeframe
				" ", # Documentation
				" ", # Performance/error metrics
				str(citation if citation else ''), # Citation
				" ", # Open-source code
				" ", # Versioning
				" ", # API or Bulk downloads
				str("".join(flat_tags)), # Keywords associated with this dataset
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

