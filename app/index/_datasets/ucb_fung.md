---
layout: default
bigquery: https://console.cloud.google.com/bigquery?p=erudite-marker-539&d=JEMS16&page=dataset
citation: Balsmeier, B., Assaf, M., Chesebro, T., Fierro, G., Johnson, K., Johnson,
  S., Li, G., W.S. Lueck, O’Reagan, D., Yeh, W., Zang, G., Fleming, L. “Machine learning
  and natural language processing applied to the patent corpus.” Forthcoming at Journal
  of Economics and Management Strategy.
contributors: Balsmeier, B., Assaf, M., Chesebro, T., Fierro, G., Johnson, K., Johnson,
  S., Li, G., W.S. Lueck, O’Reagan, D., Yeh, W., Zang, G., Fleming, L.
cost: None
description: 'Drawing upon recent advances in machine learning and natural language
  processing, we introduce new tools that automatically ingest, parse, disambiguate
  and build an updated database using United States patent data. The tools identify
  unique inventor, assignee, and location entities mentioned on each granted US patent
  from 1976 to 2016. We describe data flow, algorithms, user interfaces, descriptive
  statistics, a novelty measure based on the first appearance of a word in the patent
  corpus, and an automated co-inventor network mapping tool. '
documentation: https://funginstitute.berkeley.edu/wp-content/uploads/2016/11/Machine_learning_and_natural_language_processing_on_the_patent_corpus.pdf
last_edit: 04/07/2022, 22:43:29
location: https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/ucb-fung-patent
related_publications: ' https://doi.org/10.1111/jems.12259'
schema_fields:
- Geography
- int64_field_0
- sequence
- string_field_1
- AssistExaminer
- CPC_Layer_1
- PrimaryExaminer
- PatentNoOrNPL_cited
- FirstMiddleName
- PatentNo_citing
- CPC_Full
- id
- CountryCodeOrNPL_cited
- Sequence
- GovernmentInterests
- Company
- Type
- PatentNo
- InventorID
- InventorFullname
- LastName
- FullName
- FutureUse
- State
- Self_Citation_Flag
- FamilyID
- City
- assignee_disambiguated
- Country
- Abstract
- string_field_2
- Title
- ApplNo
- CPC_Layer_2
- IssueDate
- ApplDate
- Word
- LawFirm
- pdpass
- CurrentUse
shortname: ucb_fung
tags:
- patents
- machine learning
- disambiguation
- metrics
- novelty
terms_of_use: Creative Commons Attribution 4.0 International license
timeframe: 1976-2016
title: UCB Fung Institute Patent Data
uuid: e3d20ecd-fa26-4572-9c1f-2b26aa47e15d
---