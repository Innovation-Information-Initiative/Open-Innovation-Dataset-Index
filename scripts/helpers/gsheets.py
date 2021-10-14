import gspread
import json

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

def init(sheet_id, sheet_title, creds):
	scope = ["https://spreadsheets.google.com/feeds"]
	gc = gspread.service_account_from_dict(creds, scope)
	sheet = gc.open_by_key(key=sheet_id)

	try:
		print("downloading", sheet_title) 
		ws = sheet.worksheet(title=sheet_title)
	except gspread.exceptions.APIError:
		raise Exception(f"failed to load sheet {sheet_title}")

	return ws

def get(ws, data_range=None):
	if data_range:
		data = ws.get(data_range)
	else:
		data = ws.get()

	return data


def post(ws, data):
	try:
		ws.append_rows(data, value_input_option='RAW', insert_data_option='INSERT_ROWS')
	except gspread.exceptions.APIError:
		print(f"error submitting data to {sheet_title}")


