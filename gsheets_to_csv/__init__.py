import csv
import os
import frontmatter
import json
import gspread  # type: ignore

def json_from_data(data):
	result = []
	headers = data[0]
	headers = list(map(lambda header: header.replace(" ", "_").lower(), headers))

	del data[0]

	for row in data:
		obj = {}
		for i, header in enumerate(headers):
			try:
				obj[header] = row[i]
			except:
				obj[header] = ""
		result.append(obj)

	return result

def update_markdown(data, directory):

	for file in os.listdir(directory):
		filepath = os.path.join(directory + '/', file)
		if file.endswith(".md") and not file.startswith("_"):
			dataset = frontmatter.load(filepath)

			# find row with the same UUID
			for entry in data:
				if 'uuid' in dataset and entry['uuid'] == dataset["uuid"]:
					row = entry

			# diff 
			for term in row:
				#check not empty null or blank
				if row[term] and row[term].strip():
					dataset[term] = row[term]

			f = open(filepath, 'w')
			f.write(frontmatter.dumps(dataset))
			f.close()

def generate_markdown(data, directory):
	# remove headers

	uuids = []
	for file in os.listdir(directory):
		if file.endswith(".md") and not file.startswith("_"):
			# if the UUIDs match, remove from the list
			dataset = frontmatter.load(os.path.join(directory + '/', file))
			if 'uuid' in dataset: 
				uuids.append(dataset['uuid'])
				
	to_gen = []
	for i, dataset in enumerate(data):
		if dataset['uuid'] not in uuids:
			to_gen.append(data[i])

	for row in to_gen:
		print("creating file for", row["title"])
		#create title
		filepath = os.path.join(directory + '/', row['shortname'] + '.md')

		# create file
		f = open(filepath, 'w')

		dataset = frontmatter.load(filepath)

		for term in row:
			#check not empty null or blank
			if row[term] and row[term].strip():
				dataset[term] = row[term]

		dataset["description"] = row["description"].replace('\n', ' ')


		# dataset["uuid"] = row["uuid"]
		# dataset["title"] = row["title"]
		# dataset["location"] = row["location"]
		# if 'doi' in row and row["doi"] != '':
		#     dataset["doi"] = row["doi"]
		# dataset["description"] = row["description"].replace('\n', ' ')

		f.write(frontmatter.dumps(dataset))
		f.close()


def write_worksheet_to_csv(data, file):
	with open(file, "w", newline="") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerows(data)


def load_sheets_into_csv(sheets, output_dir, creds):
	scope = ["https://spreadsheets.google.com/feeds"]
	gc = gspread.service_account_from_dict(creds, scope)

	os.makedirs(output_dir, exist_ok=True)
	outputs = []

	for i, sh in enumerate(sheets):
		if "id" not in sh:
			print("id required to lookup sheet")
			continue
		sheet = gc.open_by_key(key=sh["id"])

		try:
			if "title" in sh:
				print("downloading", sh["title"]) 
				ws = sheet.worksheet(title=sh["title"])
			else:
				print("Sheet title not specified; selecting first")
				ws = sheet.worksheets()[0]
		except gspread.exceptions.APIError:
			raise Exception(f"failed to download sheet {sh['title']}")

		if "range" in sh:
			data = ws.get(sh["range"])
		else:
			data = ws.get()

		filename = os.path.join(output_dir, f"{sh['title']}.csv")
		write_worksheet_to_csv(data, filename)

		if sh["title"] == 'Open_Patent_Datasets' or sh["title"] == 'Innovation_Data_Toolkit':
			data_json = json_from_data(data)
			# print(json.dumps(data_json, indent = 2))
			generate_markdown(data_json, sh["directory"])
			update_markdown(data_json, sh["directory"])

		outputs.append(filename)
		print(f"sheet written to {filename}")
	return outputs

	