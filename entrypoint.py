import json
import os

from gsheets_to_csv import load_sheets_into_csv

if __name__ == "__main__":
    creds = json.loads(os.environ.get("INPUT_CREDS", "{}"))
    sheets = json.loads(os.environ.get("INPUT_SHEETS", "{}"))
    output_dir = os.environ.get("INPUT_TEMPDIR")

    outputs = load_sheets_into_csv(
        sheets=sheets,
        output_dir=output_dir,
        creds=creds,
    )

    json_results = os.environ.get("INPUT_OUTPUT_JSON")
    print("JSON_RESULTS", json_results)
    if json_results in {"true", "True"}:
        results = json.dumps(outputs)
    else:
        results = " ".join(outputs)

    print(f"::set-output name=results::{results}")