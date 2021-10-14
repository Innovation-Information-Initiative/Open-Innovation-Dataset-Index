# this file handles requests to external APIs
# (citoid, bigquery, dataverse, zenodo) to retrieve
# additional metadata about a source

import urllib.parse
import requests
import json

def citoid_request(url)
	parsed_url = urllib.parse.quote(url, safe=" ")
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url
	wiki_res = requests.get(wiki_req)

	try:
		result = wiki_res.json()[0]
	except:
		print('could not complete request')
		return None

	return result


# todo: add bigquery, dataverse, zenodo requests