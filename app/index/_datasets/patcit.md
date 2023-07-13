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
contributors: Cyril Verluise,Gabriele Cristelli, Kyle Higham, Lucas Violon, Gaétan
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
last_edit: Wed, 12 Jul 2023 18:42:12 GMT
location: https://doi.org/10.5281/zenodo.3710993
maintained_by: Cyril Verluise
open_access: 'TRUE'
record_creation_timestamp: 11/17/2020 10:38:00
related_project_shortnames: rons, lens
related_projects:
  similar:
  - patstat
  - lens
  - rons
related_publications: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
relationships:
- rons
- lens
salient_fields: DOI, PMID, ISSN, ISBN
schema_fields:
- DOI
- npl_cat_language_flag
- wg
- tsg
- meeting
- hostname
- publication_date
- reference_count
- patcit_id
- date
- acc_num
- body
- name
- ISSN
- journal_title_abbrev
- hash_id
- language_code
- source
- ref
- inpadoc_family_id
- PMCID
- tech
- docdb_family_id
- PMID
- language_is_reliable
- URL
- npl_cat
- author
- issue
- page
- volume
- is_referenced_by_count
- funder
- ISBN
- subject
- cited_by
- npl_cat_score
- event
- institution
- item
- version
- url
- type
- bibref_score
- pat_publn_id
- npl_publn_id
- md5
- title
- journal_title
- tdoc_num
- appln_id
- is_cited_by_count
- publication_number
- abstract
- reference_doi
- citation
shortname: patcit
tags:
- citation
- scholarly literature
- in-text
- front-page
- patent
- science
- database
- Wikipedia
- validation
terms_of_use: CC-BY 4.0 International
timeframe: 1836-2018
title: PatCit
uuid: bd8a562a-ce58-4a61-925d-88f0d0695974
versioning: 'TRUE'
---