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

	#get frontmatter of changed file
	dataset = frontmatter.load(new_file)

	#get metadata associated with dataset
	parsed_url = urllib.parse.quote(dataset['url'], safe=" ")
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

	shortname, ext = os.path.splitext(os.path.basename(new_file))

	# add licenses!!
	# if it's a webpage, zotero did not complete request
	if 'itemType' in result and result['itemType'] == 'webpage':
		print('no citation metadata available for this source')
		metadata = [
				str(rec_uuid),
				str(dataset["title"]), # Title
				str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), # Record Creation Timestamp
				shortname,
				str(dataset["url"]), # URL
				str(dataset["doi"] if "DOI" in dataset else " "), # DOI?
				str(dataset["description"] if "description" in dataset else " "), # Description
				str(dataset["terms"] if "terms" in dataset else " "), # Terms of use
				str(dataset["timeframe"] if "timeframe" in dataset else " "), # Timeframe
				str(dataset["documentation"] if "documentation" in dataset else " "), # Documentation
				str(dataset["error_metrics"] if "error_metrics" in dataset else " "), # Performance/error metrics
				str(dataset["citation"] if "citation" in dataset else " "), # Citation
				str(dataset["code"] if "code" in dataset else " "), # Open-source code
				str(dataset["versioning"] if "versioning" in dataset else " "), # Versioning
				str(dataset["access"] if "access" in dataset else " "), # API or Bulk downloads
				str(dataset["tags"] if "tags" in dataset else " "), # Keywords associated with this dataset
				" " # Datasets and publications using this dataset
		]


	else:
		if "tags" in result and len(result["tags"]) > 0:
			tags = (list(map(lambda item: item["tag"].split(', '), result["tags"])))
			flat_tags = [val for sublist in tags for val in sublist]
		else:
			flat_tags = []

		if "tags" in dataset and len(dataset["tags"]) > 0:
			flat_tags = flat_tags + dataset["tags"].split(' ')
			flat_tags = [tag.rstrip(',').rstrip(';') for tag in flat_tags]

		print('flat tags is', str(', '.join(str(tag) for tag in flat_tags) ))
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
				shortname,
				str(result["url"] if "url" in result else dataset["url"]), # URL
				str(result["DOI"] if "DOI" in result else result["extra"] if "DOI" in result["extra"] else " "), # DOI?
				str(dataset["description"] if "description" in dataset else result["abstractNote"] if "abstractNote" in result else " "), # Description
				str(dataset["terms"] if "terms" in dataset else " "), # Terms of use
				str(dataset["timeframe"] if "timeframe" in dataset else " "), # Timeframe
				str(dataset["documentation"] if "documentation" in dataset else " "), # Documentation
				str(dataset["error_metrics"] if "error_metrics" in dataset else " "), # Performance/error metrics
				str(citation if citation else " "), # Citation
				str(dataset["code"] if "code" in dataset else " "), # Open-source code
				str(dataset["versioning"] if "versioning" in dataset else " "), # Versioning
				str(dataset["access"] if "access" in dataset else " "), # API or Bulk downloads
				str(', '.join(str(tag) for tag in flat_tags)), # Keywords associated with this dataset
				" " # Datasets and publications using this dataset
			]
		except:
			e = sys.exc_info()[0]
			print('could not fetch metadata', e)


	# write out additions to metadata
	f.write(frontmatter.dumps(dataset))
	f.close()


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

