---
api_or_bulk_downloads: Bulk
bigquery: https://console.cloud.google.com/bigquery?project=patcit-public-data&p=patcit-public-data&page=project
citation: 'Cyril Verluise, Gabriele Cristelli, Kyle Higham, Lucas Violon, & Gaétan
  de Rassenfosse. (2020). PatCit: A Comprehensive Dataset of Patent Citations (Version
  0.3.1) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4391095'
code: https://cverluise.github.io/notebook
contributors:
- Cyril Verluise
- Gabriele Cristelli
- Kyle Higham
- Lucas Violon
- Gaétan de Rassenfosse
cost: None
datasets_and_publications_using_this_dataset: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3754772
description: 'Citazioni nel testo e in prima pagina alla letteratura non brevettuale
  e citazioni brevettuali nel testo, estratte e analizzate. patCit si basa su DOCDB,
  il più grande database di citazioni di letteratura non brevettuale (NPL). Innanzitutto,
  deduplicamo questo corpus e lo organizziamo in 10 categorie. Quindi, progettiamo
  e applichiamo modelli di estrazione delle informazioni specifici per categoria utilizzando
  spaCy. Eventualmente, quando possibile, arricchiamo i dati utilizzando database
  esterni di alta qualità specifici per il dominio. Gestito come un progetto open-source
  e gestito in modo collaborativo. '
documentation: https://cverluise.github.io/PatCit/
doi: https://doi.org/10.5281/zenodo.3710993
error_metrics: 'yes'
last_edit: Sun, 31 Mar 2024 23:38:16 GMT
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
salient_fields:
- DOI
- PMID
- ISSN
- ISBN
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
slug: patcit
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