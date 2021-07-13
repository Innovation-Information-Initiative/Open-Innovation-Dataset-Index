import csv
import logging
import os

import gspread  # type: ignore

logger = logging.getLogger("gsheets-to-csv")
logger.setLevel(logging.INFO)


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

        filename = os.path.join(output_dir, f"{sh["title"]}.csv")
        write_worksheet_to_csv(data, filename)
        outputs.append(filename)
        logger.info(f"sheet written to {filename}")
    return outputs