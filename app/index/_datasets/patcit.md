---
layout: default
api_or_bulk_downloads: Bulk
authors: Cyril Verluise, Gabriele Cristelli, Kyle Higham, Lucas Violon, Gaétan de
  Rassenfosse
bigquery: https://console.cloud.google.com/bigquery?project=patcit-public-data&p=patcit-public-data&page=project
citation: 'Cyril Verluise, Gabriele Cristelli, Kyle Higham, Lucas Violon, & Gaétan
  de Rassenfosse. (2020). PatCit: A Comprehensive Dataset of Patent Citations (Version
  0.3.1) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4391095'
code: https://cverluise.github.io/notebook
contributors: Cyril Verluise, Gabriele Cristelli, Kyle Higham, Lucas Violon, Gaétan
  de Rassenfosse
cost: None
datasets_and_publications_using_this_dataset: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
description: 'In-text and front page citations to non-patent literature and in-text
  patent citations, extracted and parsed. patCit builds on DOCDB, the largest database
  of Non Patent Literature (NPL) citations. First, we deduplicate this corpus and
  organize it into 10 categories. Then, we design and apply category specific information
  extraction models using spaCy. Eventually, when possible, we enrich the data using
  external domain specific high quality databases. Managed as an open-source, collaboratively
  maintained project. '
documentation: https://cverluise.github.io/PatCit/
doi: https://doi.org/10.5281/zenodo.3710993
error_metrics: 'yes'
last_edit: 04/08/2022, 06:38:21
location: https://doi.org/10.5281/zenodo.3710993
maintained_by: Cyril Verluise
record_creation_timestamp: 11/17/2020 10:38:00
related_project_shortnames: rons, lens
related_publications: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
relationships:
- rons
- lens
schema_fields:
- language_code
- PMID
- appln_id
- reference_doi
- npl_publn_id
- npl_cat
- event
- url
- tdoc_num
- name
- PMCID
- item
- citation
- md5
- source
- is_referenced_by_count
- date
- institution
- ISSN
- is_cited_by_count
- tsg
- hostname
- inpadoc_family_id
- language_is_reliable
- publication_number
- journal_title_abbrev
- page
- cited_by
- body
- tech
- docdb_family_id
- publication_date
- funder
- npl_cat_score
- type
- abstract
- issue
- ref
- meeting
- bibref_score
- pat_publn_id
- subject
- wg
- acc_num
- author
- URL
- DOI
- hash_id
- journal_title
- volume
- ISBN
- reference_count
- npl_cat_language_flag
- version
- title
- patcit_id
shortname: patcit
superseded_by: Wed, 23 Feb 2022 03:04:44 GMT
tags:
- citation
- scholarly literature
- in-text
- front-page
- patent
- science
- database
- Wikipedia
terms_of_use: CC-BY 4.0 International
timeframe: 1836-2018
title: PatCit
uuid: bd8a562a-ce58-4a61-925d-88f0d0695974
versioning: 'Yes'
---