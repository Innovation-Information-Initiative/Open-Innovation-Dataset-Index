import csv
import logging
import os
import frontmatter
import json
import gspread  # type: ignore

logger = logging.getLogger("gsheets-to-csv")
logger.setLevel(logging.INFO)

def json_from_data(data):
    result = []
    headers = data[0]
    headers = list(map(lambda header: header.replace(" ", "_").lower(), headers))
    print(headers)

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

def update_markdown(data):

    for file in os.listdir('datasets'):
        print('processing', file)
        filepath = os.path.join('datasets/', file)
        if file.endswith(".md"):
            dataset = frontmatter.load(filepath)

            # find row with the same UUID
            for entry in data:
                if 'uuid' in dataset and entry['uuid'] == dataset["uuid"]:
                    row = entry

            # diff 
            for term in row:
                #check not empty null or blank
                if row[term] and row[term].strip():
                    print(term, "-", row[term])
                    dataset[term] = row[term]

            f = open(filepath, 'w')
            f.write(frontmatter.dumps(dataset))
            f.close()

def generate_markdown(data):
    # remove headers

    uuids = []
    for file in os.listdir('datasets'):
        if file.endswith(".md"):
            # if the UUIDs match, remove from the list
            print('processing', file)
            dataset = frontmatter.load(os.path.join('datasets/', file))
            if 'uuid' in dataset: 
                uuids.append(dataset['uuid'])
                
    to_gen = []
    for i, dataset in enumerate(data):
        if dataset['uuid'] not in uuids:
            to_gen.append(data[i])

    # json_gen = json_from_data(to_gen)
    # print(json_gen)

    for row in to_gen:
        #create title
        filepath = os.path.join('datasets/', row['shortname'] + '.md')

        dataset = frontmatter.load(filepath)
        dataset["uuid"] = row["uuid"]
        dataset["title"] = row["title"]
        dataset["url"] = row["url"]
        if 'doi' in row and row["doi"] != '':
            dataset["doi"] = row["doi"]
        dataset["description"] = row["description"].replace('\n', ' ')

        # create file and write data
        f = open(filepath, 'w')
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
        logger.info(f"downloading sheet: {sh}")
        print(f"downloading sheet: {sh}")
        if "id" not in sh:
            logger.warning("Id required to lookup sheet")
            continue
        sheet = gc.open_by_key(key=sh["id"])

        try:
            if "title" in sh:
                ws = sheet.worksheet(title=sh["title"])
            else:
                logger.info("Sheet title not specified; selecting first")
                ws = sheet.worksheets()[0]
        except gspread.exceptions.APIError:
            raise Exception(f"failed to download sheet {sh}")

        if "range" in sh:
            data = ws.get(sh["range"])
        else:
            data = ws.get()

        filename = os.path.join(output_dir, f"{sh['title']}.csv")
        write_worksheet_to_csv(data, filename)

        if sh["title"] == 'Open_Patent_Datasets':
            data_json = json_from_data(data)
            # print(json.dumps(data_json, indent = 2))
            generate_markdown(data_json)
            update_markdown(data_json)

        outputs.append(filename)
        logger.info(f"sheet written to {filename}")
    return outputs

    