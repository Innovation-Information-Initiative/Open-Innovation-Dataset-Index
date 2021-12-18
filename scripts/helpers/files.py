# this file handles processing of repository files
# inc. markdown and csvs

import frontmatter
import json
import io
import random
import os
import csv

def write_csv(data, filepath):
	with open(filepath, "w", newline="") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerows(data)


def update_frontmatter(record, filepath):
	f = io.open(filepath, 'wb')
	frontmatter.dump(record, f)
	f.close()


def update_markdown(data, directory):
	for file in os.listdir(directory):
		filepath = os.path.join(directory + '/', file)
		if file.endswith(".md") and not file.startswith("_"):
			record = frontmatter.load(filepath)

			# find row with the same UUID
			for entry in data:
				if 'uuid' in record and entry['uuid'] == record["uuid"]:
					row = entry

					# diff 
					for term in row:
						#check not empty null or blank
						if row[term] and row[term].strip():
							record[term] = row[term]

					if row["tags"] and row["tags"].strip():
						record["tags"] = list(map(lambda tag: tag.strip(), row["tags"].split(',')))

			update_frontmatter(record, filepath)


def generate_markdown(data, directory):
	# remove headers

	uuids = []
	for file in os.listdir(directory):
		if file.endswith(".md") and not file.startswith("_"):
			# if the UUIDs match, remove from the list
			try:
				record = frontmatter.load(os.path.join(directory + '/', file))
				if 'uuid' in record: 
					uuids.append(record['uuid'])
			except:
				print('error in markdown')

	to_gen = []
	for i, record in enumerate(data):
		if record['uuid'] not in uuids:
			to_gen.append(data[i])

	new_files = []
	for row in to_gen:
		print("creating file for", row["title"])
		new_files.append(row['uuid'])

		#create title
		if row['shortname'] and row['shortname'].strip():
			filepath = os.path.join(directory + '/', row['shortname'] + '.md')
		else:
			shortname = row["title"].lower().replace(' ', '_') + "_" + str(random.randrange(0,50))
			filepath = os.path.join(directory + '/', shortname + '.md')

		#open and close file
		if not os.path.exists(filepath):
			open(filepath, 'w').close()

		record = frontmatter.load(filepath)

		for term in row:
			#check not empty null or blank
			if row[term] and row[term].strip():
				record[term] = row[term]

		if row["tags"] and row["tags"].strip():
			record["tags"] = list(map(lambda tag: tag.strip(), row["tags"].split(',')))

		record["description"] = row["description"].replace('\n', ' ')

		update_frontmatter(record, filepath)

	return new_files


