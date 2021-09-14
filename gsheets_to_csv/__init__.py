import csv
import logging
import os
import frontmatter
import gspread  # type: ignore

logger = logging.getLogger("gsheets-to-csv")
logger.setLevel(logging.INFO)

# def json_from_data(data):
#     result = []
#     headers = data[0]
#     del data[0]

#     for row in data:
#         print(row)
#         obj = {}
#         for i, header in enumerate(headers):
#             try:
#                 obj[header] = row[i]
#             except:
#                 print('end of row')
#         result.append(obj)

#     return result

def update_markdown(data):
    for file in os.listdir('datasets'):
        if file.endswith(".md"):
            dataset = frontmatter.load(os.path.join('datasets/', file))

            # find row with the same UUID
            for row in data:
                if 'uuid' in dataset and row[0] == dataset["uuid"]:
                    sheet_row = row
                    print('file is', file, "row is", row)


def generate_markdown(data):
    # remove headers
    del data[0]

    uuids = []
    for file in os.listdir('datasets'):
        if file.endswith(".md"):
            # if the UUIDs match, remove from the list
            dataset = frontmatter.load(os.path.join('datasets/', file))
            if 'uuid' in dataset: 
                uuids.append(dataset['uuid'])
                
    to_gen = []
    for i, row in enumerate(data):
        if row[0] not in uuids:
            to_gen.append(data[i])

    # json_gen = json_from_data(to_gen)
    # print(json_gen)

    for row in to_gen:
        #create title
        filepath = os.path.join('datasets/', row[3] + '.md')

        # create file
        f = open(filepath, 'w')

        dataset = frontmatter.load(filepath)
        dataset["uuid"] = row[0]
        dataset["title"] = row[1]
        dataset["url"] = row[4]
        if row[5] != '':
            dataset["doi"] = row[5]
        dataset["description"] = row[6].replace('\n', ' ')

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
            generate_markdown(data)
            update_markdown(data)

        outputs.append(filename)
        logger.info(f"sheet written to {filename}")
    return outputs

    