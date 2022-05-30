# this file handles processing of repository files
# inc. markdown and csvs

import frontmatter
import json
import io
import random
import os
import csv
import re
import pandas as pd

def write_csv_from_dict(data, filepath):
	df = pd.DataFrame.from_dict(data)
	df.to_csv(filepath)
	# with open(filepath, "w", newline="") as csvfile:
	# 	writer = csv.writer(csvfile, delimiter=",")
	# 	writer.writerows(data)


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
						if term in row and row[term].strip():
							record[term] = row[term]

					if "title" in row and row["title"].strip():
						title = re.sub('\s+',' ',row["title"]).strip() # stop the titles breaking search
						record["title"] = title

					if "related_projects" in row and row["related_projects"].strip():
						record["related_projects"] = {}
						try:
							#try reading as JSON
							related_projects = json.loads(row["related_projects"])
							for project in related_projects:
								print(project)
								if project["relationship_type"] in record["related_projects"]:
									record["related_projects"][project["relationship_type"]].append(project["shortname"])
								else:
									record["related_projects"][project["relationship_type"]] = [project["shortname"]]
						except:
							print("can't read as JSON")

					if "tags" in row and row["tags"].strip():
						record["tags"] = list(map(lambda tag: tag.strip(), row["tags"].split(',')))

					if "schema_fields" in row and row["schema_fields"].strip():
						record["schema_fields"] = list(map(lambda field: field.strip(), row["schema_fields"].split(',')))


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
			if term in row and row[term].strip():
				record[term] = row[term]

		if "title" in row and row["title"].strip():
			title = re.sub('\s+',' ',row["title"]).strip() # stop the titles breaking search
			record["title"] = title

		# if "related_project_shortnames" in row and row["related_project_shortnames"].strip():
		# 	record["relationships"] = list(map(lambda tag: tag.strip(), row["related_project_shortnames"].split(',')))

		if "tags" in row and row["tags"].strip():
			record["tags"] = list(map(lambda tag: tag.strip(), row["tags"].split(',')))

		if "schema_fields" in row and row["schema_fields"].strip():
			record["schema_fields"] = list(map(lambda field: field.strip(), row["schema_fields"].split(',')))

		if "related_projects" in row and row["related_projects"].strip():
			record["related_projects"] = {}
			try:
				#try reading as JSON
				related_projects = json.loads(row["related_projects"])
				for project in related_projects:
					print(project)
					if project["relationship_type"] not in record["related_projects"]:
						record["related_projects"][project["relationship_type"]].append(project["shortname"])
					else:
						record["related_projects"][project["relationship_type"]] = [project["shortname"]]
			except:
				print("can't read as JSON")

		record["description"] = row["description"].replace('\n', ' ')

		update_frontmatter(record, filepath)

	return new_files


