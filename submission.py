import json
import os

from json_submission import parse_and_submit

if __name__ == "__main__":
    creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
    sheet_id = os.environ.get("INPUT_SHEET_ID")
    output_dir = os.environ.get("INPUT_TEMPDIR")

    parse_and_submit(
        sheets=sheet_id,
        output_dir=output_dir,
        creds=creds,
    )

    print("ran function")