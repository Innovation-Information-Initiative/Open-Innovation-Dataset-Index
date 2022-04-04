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
last_edit: Tue, 29 Mar 2022 14:09:23 GMT
location: https://doi.org/10.5281/zenodo.3710993
maintained_by: Cyril Verluise
record_creation_timestamp: 11/17/2020 10:38:00
related_project_shortnames: rons, lens
related_publications: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
relationships:
- rons
- lens
schema_fields: '[''PMID'', ''subject'', ''item'', ''npl_cat'', ''ref'', ''version'',
  ''volume'', ''PMCID'', ''journal_title'', ''institution'', ''language_is_reliable'',
  ''patcit_id'', ''abstract'', ''issue'', ''tsg'', ''journal_title_abbrev'', ''body'',
  ''pat_publn_id'', ''title'', ''hash_id'', ''hostname'', ''URL'', ''name'', ''acc_num'',
  ''source'', ''type'', ''is_referenced_by_count'', ''docdb_family_id'', ''cited_by'',
  ''tdoc_num'', ''tech'', ''inpadoc_family_id'', ''ISBN'', ''md5'', ''is_cited_by_count'',
  ''bibref_score'', ''date'', ''page'', ''event'', ''npl_cat_score'', ''npl_cat_language_flag'',
  ''author'', ''reference_doi'', ''publication_date'', ''appln_id'', ''language_code'',
  ''npl_publn_id'', ''meeting'', ''publication_number'', ''ISSN'', ''citation'', ''funder'',
  ''url'', ''reference_count'', ''wg'', ''DOI'']'
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