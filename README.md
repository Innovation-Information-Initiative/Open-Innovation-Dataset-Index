# I³ Tracker for Essential Open Innovation Datasets 

This repository is set up to track, version, and contribute updates to the [I³ Essential Open Innovation Dataset Index](https://iiindex.org/), which consists of lists of datasets and tools relevant to Innovation Data. This index may be collaboratively edited, either by making edits to markdown files contained in this repository, or editing metadata in the [Google Sheet](https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1389884911).

The repository checks the Google Sheet for changes every 5min (and will update the site if there are any), and will also re-build the site automatically when somebody makes an edit via git. The site is generated from markdown files in this repository using the static site generator Jekyll.

## Add/edit a Dataset using Git

Each record in the index has a corresponding markdown file (auto-generated) in the folder [`datasets/`](/datasets). These files contain the basic metadata associated with the record in the frontmatter, and also allow more long-form information, such as details of queries, images, and other written information, to be added. Both of these things are editable.

When a markdown file is added to the `datasets/` folder, a GitHub action publishes the metadata in the frontmatter to the Google Sheet, and to the archive csv, to keep the records up to date. This script calls various metadata scrapers to automatically pull information like permalinks, citation information, and versioning. Once the file has been successfully committed, a second action will run to refresh the state of the website to reflect the edits.

**Contribution Steps**

1. fork the repository, create a markdown in the folder 'datasets' based on the [template file](datasets/_template.md) 
2. add as much metadata as you like, and create a pull request in this repository
3. all being well, this should automatically merge. if not, you can check the GitHub actions log, or open an issue. (make sure it's in the correct folder, and has a _.md_ file extension before doing so)

If the dataset is hosted on a platform with parseable citation metadata (Dataverse, Zenodo, ICPSR, and major university repositories are examples of these), then the tool will automatically pull most of the data associated with the dataset -- fields that will auto-fill are indicated by a comment. If the dataset is hosted on e.g. a personal site, then you might want to include some more information -- but ultimately, only a title and URL is really necessary. However you fill out your dataset, a uuid and timestamp will be generated for it automatically; these aren't fields you need to include (hence not included in the template).

The reason we've done this is to save you from copy-pasting a lot of information from existing repositories, and to make it easier for you to curate more useful and harder-to-scrape metadata -- such as the timeframes of datasets, links to code and documentation, and datasets that might be built on top of it but don't use an easy-to-parse citation. So definitely prioritise these fields!

If you're unsure of how to make a pull request, github has some [good guides](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to doing this. You can also just make an edit to the Google Sheet, which will have an equivalent effect.

If there's a piece of metadata you think we should collect but don't, please add it to the frontmatter of the markdown files you contribute.  (Nothing will break!)  Then open an issue mentioning the new field, so that we can discuss adding it to the repository officially too.

To contribute a new dataset via pull request, please use the template file [`datasets/_template.md`](datasets/_template.md) as a reference:

```markdown
---
title: #required
url: #required
doi: #scrapeable
citation: #scrapeable
description: #scrapeable
timeframe:
documentation:
error_metrics:
code:
versioning: #scrapeable
terms_of_use: #scrapeable
tags:
references:
---


body text. info about `queries`, links and images goes here :)
```

## Collections

The site also indexes collections, which are pages containing thematic information about datasets, tools and resources. These are housed in the folder [`collections/`](/collections). The collection [`intro.md`](/collections/intro.md) is an example -- this particular collection is also rendered on the front page of the site.

In the same manner as datasets, collection files can be added or edited using pull requests, where the repository is forked, and additions or edits to the collections can be made. The collections are not currently tracked via Google Sheets, and so may only be edited via git.

To create a new collection, the collection template may be copied to use as a reference:

```markdown
---
title:
author:
tags:
---

Collections are a way to list resources around a theme, relevant to a research agenda or set of papers, or as an introduction to various aspects of the field. They are formatted in markdown:

To list a dataset that's in the index, use a relative link, e.g.

```markdown
[local dataset name](/datasets/dataset_shortname)
```

Dataset shortnames can be found either by looking at the urls directly, or through the 'shortnames' column of the [Google Sheet](https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1389884911).


## Index

A versioned .csv file containing the index may be accessed in the folder `index_archive`. If you'd like to browse and query either sheet, you can do so using Github's Flat Data tool [here](https://flatgithub.com/Innovation-Information-Initiative/Dataset-Index-Sheet-Tracker?filename=index_archive%2FOpen_Innovation_Datsets.csv&filters=&sha=50624ec98ff61d670b75aa9f9206650395bc624b&sort=Title%2Casc&stickyColumnName=Title). The Github Action that pulls the sheet is based on Dolthub's [Gsheets-to-csv](https://github.com/dolthub/gsheets-to-csv) action.

<img width="1280" alt="Screenshot 2021-07-13 at 13 35 49" src="https://user-images.githubusercontent.com/16444898/125452541-3ca1ac05-16b8-4fa3-8b21-beee9b6db01b.png">
