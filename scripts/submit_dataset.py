import os
import uuid
import frontmatter
import sys
import json
from datetime import datetime
import pandas as pd

from helpers import files, gsheets, metadata
from helpers.utils import get_project_root
from helpers.sprites import create_sprites

def parse_and_submit(new_file, sheet_id, sheet_title, output_dir, creds):
	#download google sheets
	ws = gsheets.init(sheet_id, sheet_title, creds)
	# raw_data = gsheets.get(ws)
	# data, schema = gsheets.json_from_data(raw_data)
	sheet_df, schema = gsheets.get_df(ws)

	#generate UUID for entry and write to file
	record = frontmatter.load(new_file)
	new_uuid = uuid.uuid4()
	record['uuid'] = str(new_uuid)
	files.update_frontmatter(record, new_file)

	#create sprite for UUID
	create_sprites([str(new_uuid)])

	dataset = {}

	print('head is', sheet_df.head())

	#copy submitted info from markdown to record
	for field in sheet_df.head():
		if field in record: 
			dataset[field] = record[field]
		else:
			dataset[field] = ''

	# add additional metadata
	shortname, ext = os.path.splitext(os.path.basename(new_file))
	dataset['last_edit'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	dataset['shortname'] = shortname
	dataset['uuid'] = str(new_uuid)

	print(record['location'])

	#get citation
	result, bibtex = metadata.citoid_request(record['location'])

	if 'itemType' in result and result['itemType'] == 'webpage':
		print('no citation metadata available for this source')

	else:
		try:
			if "tags" in result and len(result["tags"]) > 0:
				tags = list(map(lambda item: item.split(', ').strip(), result["tags"]))
				flat_tags = [val for sublist in tags for val in sublist]
			else:
				flat_tags = []
		except:
			flat_tags = []
			print('could not extract tags from result')

		try:
			if "tags" in dataset and len(dataset["tags"]) > 0:
				flat_tags = flat_tags + list(map(lambda tag: tag.split(' ').strip(), dataset["tags"]))
				flat_tags = [tag.rstrip(',').rstrip(';') for tag in flat_tags]
		except:
			print('could not extract tags from dataset')

		dataset["title"] = result["title"] if "title" in result else ''
		dataset["location"] = result["url"] if "url" in result else ''
		dataset["doi"] = result["DOI"] if "DOI" in result else result["extra"] if "DOI" in result["extra"] else ''
		if 'description' not in dataset and 'abstractNote' in result:
			dataset["description"] = result["abstractNote"]
		dataset["tags"] = str(', '.join(str(tag) for tag in flat_tags))

		if bibtex is not None:
			dataset['citation'] = bibtex

	print(pd.json_normalize(dataset))
	# sheet_df = sheet_df.append(pd.json_normalize(dataset), ignore_index=True)
	sheet_df = pd.concat([sheet_df,pd.json_normalize(dataset)],join='inner')
	print('df is', sheet_df)
	sheet_df.columns=schema

	#first, append to csv (write updated sheet in case of any changes)
	try:
		filename = os.path.join(get_project_root(), output_dir, os.environ.get("OUTPUT_FILE"))
		sheet_df.to_csv(filename, index=False)
	except:
		e = sys.exc_info()[0]
		print('issue writing to csv', e)

	#then push to google sheet
	raw_row = pd.json_normalize(dataset).values.tolist()[0]
	row = list(map(lambda val: str(val), raw_row))
	gsheets.post(ws, row)


if __name__ == "__main__":
	filepath = os.path.join(get_project_root(), sys.argv[1])

	parse_and_submit(
		new_file = filepath,
		sheet_id = os.environ.get("INPUT_SHEET_ID"),
		sheet_title = os.environ.get("INPUT_SHEET_TITLE"),
		output_dir = os.environ.get("INPUT_TEMPDIR"),
		creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
	)

	print("processed", filepath)
