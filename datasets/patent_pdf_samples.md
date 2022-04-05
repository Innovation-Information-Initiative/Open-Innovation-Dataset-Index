---
bigquery: https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=labeled_patents&page=dataset
contributors: Google Patents
cost: None
description: 'The dataset consists of PDFs in Google Cloud Storage from the first
  page of select US and EU patents, and BigQuery tables with extracted entities, labels,
  and other properties, including a link to each file in GCS. The structured data
  contains labels for eleven patent entities (patent inventor, publication date, classification
  number, patent title, etc.), global properties (US/EU issued, language, invention
  type), and the location of any figures or schematics on the patent''s first page.


  The structured data is the result of a data entry operation collecting information
  from PDF documents, making the dataset a useful testing ground for benchmarking
  and developing AI/ML systems intended to perform broad document understanding tasks
  like extraction of structured data from unstructured documents. This dataset can
  be used to develop and benchmark natural language tasks such as named entity recognition
  and text classification, AI/ML vision tasks such as image classification and object
  detection, as well as more general AI/ML tasks such as automated data entry and
  document understanding. Google is sharing this dataset to support the AI/ML community
  because there is a shortage of document extraction/understanding datasets shared
  under an open license.

  '
documentation: At site
last_edit: 04/05/2022, 13:50:15
location: https://console.cloud.google.com/marketplace/product/global-patents/labeled-patents
maintained_by: Google Cloud Public Datasets Program
schema_fields:
- y_relative_min
- x_relative_min
- class_international
- publication_date
- y_relative_max
- inventor_line_1
- application_number
- issuer
- class_us
- title_line_1
- language
- representative_line_1_eu
- x_relative_max
- invention_type
- filing_date
- number
- applicant_line_1
- gcs_path
- priority_date_eu
shortname: patent_pdf_samples
tags:
- machine learning
- OCR
- document recognition
- benchmarking
terms_of_use: CC BY 4.0
title: Patent PDF Samples with Extracted Structured Data
uuid: 8b8da8ff-2b09-4e1f-9523-c0c549c5cfa1
---