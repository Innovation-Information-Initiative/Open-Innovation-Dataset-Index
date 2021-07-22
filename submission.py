import json
import os
import sys

from json_submissions import parse_and_submit

if __name__ == "__main__":
    new_file = sys.argv[1]
    creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
    sheet_id = os.environ.get("INPUT_SHEET_ID")
    output_dir = os.environ.get("INPUT_TEMPDIR")

    parse_and_submit(
        sheet_id=sheet_id,
        output_dir=output_dir,
        creds=creds,
    )

    print("new file is ", new_file)