---
bigquery: https://console.cloud.google.com/bigquery?p=patents-public-data&d=uspto_oce_claims&page=dataset
citation: 'Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, Patent Claims
  and Patent Scope (October 2016). USPTO Economic Working Paper 2016-04. Available
  at: SSRN: https://ssrn.com/abstract=2844964'
cost: None
description: The Patent Claims Research Dataset contain detailed information on claims
  from U.S. patents granted between 1976 and 2014 and U.S. patent applications published
  between 2001 and 2014. The dataset is derived from the Patent Application Publication
  Full-Text and Patent Grant Full Text files, available at https://bulkdata.uspto.gov/,
  to which the Office of Chief Economist (OCE) applied a Python algorithm to identify
  individual claims as well as the dependency relationship between claims. From the
  parsed claims text, OCE created six data files containing individually-parsed claims,
  claim-level statistics, and document-level statistics, including newly-developed
  measures of patent scope.
documentation: Available at source, including documentation of variables
doi: 'http://dx.doi.org/10.2139/ssrn.2844964 '
last_edit: Wed, 02 Apr 2025 08:02:45 GMT
location: https://www.uspto.gov/ip-policy/economic-research/research-datasets/patent-claims-research-dataset
maintained_by: EconomicsData@uspto.gov
open_access: 'FALSE'
related_publications: https://ssrn.com/abstract=2844964
schema_fields:
- pat_dep_wrd_ct
- appl_id
- cns_ct
- claim_no
- ind_flg
- claim_txt
- pub_no
- pub_dep_wrd_avg
- pub_dep_wrd_ct
- dependencies
- pub_wrd_ct
- pat_dep_wrd_min
- word_ct
- pub_wrd_min
- or_ct
- pat_wrd_min
- pat_wrd_ct
- pat_no
- char_ct
- pat_clm_ct
- pat_dep_clm_ct
- pat_dep_wrd_avg
- sf_ct
- pub_wrd_avg
- pub_dep_clm_ct
- pub_clm_ct
- publication_number
- pat_wrd_avg
- pub_dep_wrd_min
shortname: uspto_patent_claims
tags:
- financial services
- scope
- economics
terms_of_use: 'USPTO’s online databases are not designed or intended to be a source
  for bulk downloads of USPTO data when accessed through the website’s interfaces.
  Individuals, companies, IP addresses, or blocks of IP addresses who, in effect,
  deny or decrease service by generating unusually high numbers of database accesses
  (searches, pages, or hits), whether generated manually or in an automated fashion,
  may be denied access to USPTO servers without notice.


  Bulk data products may be separately obtained from the USPTO, either for free or
  at the cost of dissemination. For details, see information on Electronic Bulk Data
  Products: https://www.uspto.gov/learning-and-resources/electronic-bulk-data-products'
timeframe: 1976-2014
title: USPTO OCE Patent Claims Research Data
uuid: 7d8cda0b-9ee1-47b9-9dca-8adb93206024
versioning: 'FALSE'
---