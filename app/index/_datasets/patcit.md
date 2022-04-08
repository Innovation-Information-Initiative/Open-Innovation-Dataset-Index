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
last_edit: 04/08/2022, 15:47:15
location: https://doi.org/10.5281/zenodo.3710993
maintained_by: Cyril Verluise
record_creation_timestamp: 11/17/2020 10:38:00
related_project_shortnames: rons, lens
related_publications: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
relationships:
- rons
- lens
schema_fields:
- name
- PMCID
- ISBN
- npl_cat_score
- ISSN
- reference_count
- body
- publication_number
- language_code
- journal_title_abbrev
- npl_publn_id
- title
- pat_publn_id
- is_referenced_by_count
- npl_cat
- hash_id
- appln_id
- abstract
- meeting
- is_cited_by_count
- publication_date
- issue
- subject
- bibref_score
- item
- institution
- cited_by
- ref
- tdoc_num
- md5
- version
- DOI
- PMID
- URL
- reference_doi
- patcit_id
- tsg
- author
- tech
- wg
- hostname
- funder
- page
- acc_num
- docdb_family_id
- type
- event
- npl_cat_language_flag
- inpadoc_family_id
- date
- source
- citation
- url
- journal_title
- language_is_reliable
- volume
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