# this file handles requests to external APIs
# (citoid, bigquery, dataverse, zenodo) to retrieve
# additional metadata about a source

import urllib.parse
import requests
import json

def citoid_request(url):
	parsed_url = urllib.parse.quote(url, safe=" ")
	wiki_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/' + parsed_url
	wiki_res = requests.get(wiki_req)

	bib_req = 'https://en.wikipedia.org/api/rest_v1/data/citation/bibtex/' + parsed_url
	bibtex = requests.get(bib_req).text

	result = wiki_res.json()

	print(wiki_res.json())
	try:
		result = wiki_res.json()[0]
	except:
		print('could not complete request')
		return None

	return result, bibtex


# todo: add bigquery, dataverse, zenodo requests