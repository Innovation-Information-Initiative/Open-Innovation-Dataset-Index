---
contributors:
- Agnes Cameron
description: Guide to popular validation datasets, tools and techniques for innovation research.
tags:
- validation
- open data
title: Validation in Innovation Data
shortname: validation
uuid: a2ba7a86-73af-4494-8a28-3c86784f7d03
---

Within the space of Innovation research, there is a diversity of approaches to validating the reliability of new datasets, metrics and tools. Validation datasets are of particular salience to machine learning tasks, where they are used to evaluate and tune models prior to testing. The wider concept of a 'validation dataset' is necessarily a bit ambiguous -- many regular datasets may be used for the cross-checking of the effectiveness of a particular model. Here, we list datasets designed with this task in mind, however, this list could be extended to include datasets popularly employed for this task.

The construction of a validation dataset often involves the costly production of high-quality human-annotated data. When tailored to individual projects (e.g. to validate a particular research question), these datasets are not always published with a view to re-use, despite being potentially valuable tools for researchers examining similar fields. 

This guide aims to index the validation datasets that are available (so researchers can make use of them), point to ones that have been made but are not currently public, outline various validation methods and tools, and also to index validation datasets that do not currently exist, but would be of use to the community.

### Contribute

As of December 2023, there is a [specific tab](https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1512625211) in the IIIndex Google sheet for researchers to name desired and existing validation datasets. You can also tag existing projects that you know have validation data using the 'validation' tag.

This guide is [editable](https://github.com/Innovation-Information-Initiative/Open-Innovation-Dataset-Index/blob/main/collections/validation.md), and additions are enthusiastically welcome. This guide is also periodically updated both with datasets added to the index, and responses to our [researcher survey](https://docs.google.com/forms/d/1FojKdh00M0JTVPAO5pocF3d3agItxttZ2MQzrV160I4/edit?pli=1#responses).

Lastly, I am always interested to talk to researchers about how to best support the contribution of validation data into the collective domain. Please [get in touch]("mailto:agnescam@mit") with any queries, comments and suggestions.

### Standalone validation datasets

These bear the most similarity to machine learning approaches to data publication, and as such are published on the machine learning model comparison platforms [Kaggle](https://www.kaggle.com/) and [HuggingFace](https://huggingface.co/). These are datasets produced with the explicit purpose of validating a range of machine learning models' effectiveness.

* **[Google Patent Phrase Similarity Dataset](https://iiindex.org/datasets/phrase_similarity.html)** -- A human rated contextual phrase to phrase matching dataset focused on technical terms from patents.
* **[BIGPATENT](https://iiindex.org/datasets/bigpatent.html)** -- Human-written abstractive summaries of 1.3 million patent document records, plus evaluations of popular learning/summarisation models trained on this data.
* **[Patent PDF Samples with Extracted Structured Data](https://iiindex.org/datasets/patent_pdf_samples.html)** -- Training dataset for entity extraction from PDFs of US and EU patents. The structured data contains labels for eleven patent entities (e.g. patent inventor, publication date, classification number, patent title), global properties (US/EU issued, language, invention type), and the location of any figures or schematics on the patent's first page. 

### Projects with published validation data

These projects have developed and published validation datasets for reuse as part of their research process.

* **[Patcit](https://iiindex.org/datasets/patcit.html)** -- Verluise et. al developed a human-annotated dataset to compensate for inconsistencies in formats of patent numbers, in order to evaluate of their model that automates this process (160 patents annotated), and a second dataset for the parsing of citations (300 patents annotated).
* **[Reliance on Science](https://iiindex.org/datasets/rons.html)** -- Marx and Fuegi hired a group of research assistants to create a dataset of citations extracted from randomly-selected patents.
* **[Stanford NLP Model Output for Biofuel Patent Classification](https://iiindex.org/datasets/biofuel_classification.html)** -- Kessler publishes a dataset of 1000 manually classified biofuel patents (1976-2014), which is split for validation of the classification model


### Projects with validation data not currently public

(please correct if published!)

* **[Patent Scope and Examiner Toughness](https://iiindex.org/datasets/patent_scope_toughness.html)** -- Kuhn and Thompson collaborate with seven patent attorneys who complete a questionnaire on the scope of a patent (140 total) relative to other patents in the same area. Described in [this paper](https://ssrn.com/abstract=2977273).
* **[Text Matching to Measure Patent Similarity](https://onlinelibrary.wiley.com/doi/abs/10.1002/smj.2699)** -- Arts, Cassiman and Gomez recruited thirteen paid experts from five different fields to rate the technological similarity of different patents in their field of expertise, a total of 850 patents
* **[Natural language processing to identify the creation and impact of new technologies in patent text](https://www.sciencedirect.com/science/article/pii/S0048733320302195?via%3Dihub)** -- Arts et. Al manually collect patents linked to prestigious awards, and manually match to patents, as a marker for impact / radical innovation

### Tools for constructing validation datasets

Here annotation tools for creating high-quality human-made datasets are listed. Typically these tools speed up and allow for collaboration on the costly process of producing human-generated data.

* **[Prodigy](https://iiindex.org/tools/prodigy.html)** -- scriptable annotation tool, used to rapidly create new machine learning datasets with human annotation.
* **[Doccano](https://github.com/doccano/doccano)** -- open-source text annotation tool, particularly useful for sentiment analysis

### Desired validation datasets

These are not known to exist at present, and are published here as a placeholder/flag for future research proposals.

* _"An extensive dataset of human-annotated patent similarity would be highly useful. Ideally, the dataset would cover different aspects of patent similarity (eg, style, function, domain), a measure of annotator disagreement, and would cover patents from different time periods."_
