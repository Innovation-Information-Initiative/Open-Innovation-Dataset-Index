---
authors:
- Agnes Cameron
- Matt Marx
description: Starting point list of datasets and resources for the study of innovation,
  including guides to interpreting patent identifiers, request APIs, and disambiguation
  tools.
tags: patents
title: Essential Innovation Analysis Datasets
uuid: 4f841bda-4401-4cfd-ab89-403d577099f4
---

Many researchers focused on innovation want to understand the origins of ideas, including as captured as published papers, their evolution and commercialization by firms, including as patents and products. The following datasets provide a starting point for analysis of innovation data. We note proprietary or limited-access options but focus on open-access datasets, which can be retrieved without needin to pay or request access and are *italicized*. Other than prioritizing open datasets, we list them alphabetically.


* patent data and disambiguation
	* [*Google Patents Public Datasets*](https://iiindex.org/datasets/google_patents_public)
	* [*PatentsView*](https://iiindex.org/datasets/patentsview) -- contains data on USPTO patents since 1976.
	* [PATSTAT](https://iiindex.org/datasets/patstat) (NB: not an open dataset)
* scientific literature
	*  [*Microsoft Academic Graph "MAG"*](https://iiindex.org/datasets/makg.html) -- MAG is the original source of open metadata on scientific articles from all fields. It includes abstracts but not full-text. Coverage is 1800-2020. For articles after 2021 see OpenAlex. 
	*  [*OpenAlex*](http://openalex.org) -- an open-source, drop-in replacement for MAG by the curators of Unpaywall. Official release will be 3 January 2022.
	*  [*PubMed*](https://pubmed.ncbi.nlm.nih.gov/download/#annual-baseline) -- Public data on articles in the life sciences and related fields.
	*  [Dimensions](https://www.dimensions.ai/scientometric-research/) -- publication data access by request only. (NB: not an open dataset)
	*  [Clarivate Web of Science](https://access.clarivate.com/login?app=wos&alternative=true&shibShireURL=https:%2F%2Fwww.webofknowledge.com%2F%3Fauth%3DShibboleth&shibReturnURL=https:%2F%2Fwww.webofknowledge.com%2F%3Fmode%3DNextgen%26action%3Dtransfer%26path%3D%252Fwos%252Fauthor%252Fsearch%26DestApp%3DUA&referrer=mode%3DNextgen%26path%3D%252Fwos%252Fauthor%252Fsearch%26DestApp%3DUA%26action%3Dtransfer&roaming=true) -- proprietary data on scientific publications, available via license or limited online searches. (NB: not an open dataset)
	*  [Elsevier Scopus](https://www.scopus.com/home.uri) -- proprietary data on scientific publications, available via license or limited online searches. (NB: not an open dataset)
* patent citation to scientific literature
	* [*Lens.org*](https://iiindex.org/datasets/lens) -- Data queriable through the Lens API and also downloadable in bulk. Creates a unique identifier for papers, patents, authors, inventors and institutions.
	* [*Patcit*](https://iiindex.org/datasets/patcit)
	* [*Reliance on Science*](http://relianceonscience.org) -- contains front-page and in-text citations to scientific articles from worldwide patents
* matching patents to products
	* [*IPRoduct*](http://iproduct.io) -- links patents to products via Virtual Patent Marking.
* matching patents to firms
	* [*Chinese Patent Data Project*](https://iiindex.org/datasets/chinese_patent_data)
	* [*DISCERN Patent Compustat Crosswalk*](https://iiindex.org/datasets/discern) -- links patent assignees to public firms 1980-2015, including resolution of firm acquisitions and reclassifications.
	* [*KPSS patent assignees to firms 1920-2019*](https://github.com/KPSS2017/Technological-Innovation-Resource-Allocation-and-Growth-Extended-Data) -- 1926-2019.
	* [UVA Darden Global Corporate Patent Dataset](https://patents.darden.virginia.edu/) - 1980-2017, must request access.

## Guides

* [WIPO Manual on Open Source Patent Analytics](https://wipo-analytics.github.io/) and accompanying [Github Repository](https://github.com/wipo-analytics), which gives a practical guide to free and open source software tools for patent analytics
* [Lens Labs Knowledge Database](https://support.lens.org/knowledge-database/), which contains extensive information about patent analysis, including legal status calculation, geographical variability in patent law, analysis of biological patents and guides to reading patents
* Paul Oldham's guide [Understanding Patent Data Fields](https://www.pauloldham.net/patent-data-fields/), which gives a thorough overview of using patent identifiers, and also features in the WIPO manual
