---
layout: default
citation: PATSTAT
code: 'patstat cookbook'' by Gaétan de Rassenfosse https://onlinelibrary.wiley.com/doi/full/10.1111/1467-8462.12073 '
contributors: EPO
cost: €975.00 - € 1460.00
description: 'PATSTAT contains bibliographical and legal event patent data from leading
  industrialised and developing countries. This is extracted from the EPO’s databases
  and is either provided as bulk data or can be consulted online. '
last_edit: Sat, 05 Mar 2022 18:25:32 GMT
location: https://www.epo.org/searching-for-patents/business/patstat.html#tab3
maintained_by: European Patent Office
record_creation_timestamp: 11/27/2020 17:20:46
shortname: patstat
tags:
- Europe
- patents
terms_of_use: Requires a subscription to access
title: PATSTAT
uuid: e390a212-3a92-4d8f-ac4d-ca2c960a36d3
---

PATSTAT contains bibliographical and legal event patent data from over 100 patent offices, managed by the EPO. This is extracted from the EPO's databases and is either provided as bulk data or can be consulted online.

The PATSTAT product line consists of two individual databases. They are available as a bulk data set or via PATSTAT Online, a web-based interface to the databases.

The first, [PATSTAT Global](https://www.epo.org/searching-for-patents/business/patstat.html), is the database most commonly referred to as 'PATSTAT'. The second, PATSTAT Register, and associated queries, is indexed [here](/datasets/patstat_register).

## Example Queries for PATSTAT Global

Gaétan de Rassenfosse, Hélène Dernis and Geert Boedt wrote a guide to PATSTAT, including 10 queries and details of the schema, full details of which are available [here](https://onlinelibrary.wiley.com/doi/epdf/10.1111/1467-8462.12073). The full code is shared [here](http://www.runmycode.org/companion/view/559).

The below queries are formatted in MySQL, and are copied from the 2014 version of the code -- the paper contains some guidance to adapting different dialects. For details about the approach of each query, refer to the paper.

### 1. Identification of Patents by Technology Field
```SQL
SELECT DISTINCT
    t1.appln_id, t1.appln_auth, t1.appln_nr, t1.appln_kind
FROM
    tls201_appln t1
        INNER JOIN
    tls209_appln_ipc t2 ON t1.appln_id = t2.appln_id
WHERE
    year(t1.appln_filing_date) = 2005
        AND (t1.appln_kind = 'A' OR t1.appln_kind = 'W')
        AND t2.ipc_class_symbol LIKE 'F03D%'
ORDER BY t1.appln_auth , t1.appln_id;

CREATE VIEW our_sample AS
    SELECT DISTINCT
        t1.appln_id, t1.appln_auth, t1.appln_nr, t1.appln_kind
    FROM
        tls201_appln t1
            INNER JOIN
        tls209_appln_ipc t2 ON t1.appln_id = t2.appln_id
    WHERE
        year(t1.appln_filing_date) = 2005
            AND (t1.appln_kind = 'A' OR t1.appln_kind = 'W')
            AND t2.ipc_class_symbol LIKE 'F03D%'
    ORDER BY t1.appln_auth , t1.appln_id;
```
  
### 2: Identifying Patent Cooperation Treaty Applications
```SQL
SELECT 
    t1.appln_id AS PCT_appln_id,
    t1.appln_auth AS PCT_appln_auth,
    t1.appln_nr AS PCT_appln_nr,
    t1.appln_kind,
    t2.appln_id AS appln_id_sf,
    t2.appln_auth AS appln_auth_sf
FROM
    our_sample t1
        INNER JOIN
    tls201_appln t2 ON t1.appln_id = t2.internat_appln_id
WHERE
    t1.appln_auth = 'DK'
        AND t2.appln_auth IN ('CN' , 'JP')
ORDER BY t1.appln_id;
```

### 3. Obtaining Information on Priority Status
```SQL
SELECT DISTINCT
    t1.appln_id,
    (CASE
        WHEN t2.appln_id IS NULL THEN 1
        ELSE 0
    END) AS is_a_pf
FROM
    our_sample t1
        LEFT OUTER JOIN
    tls204_appln_prior t2 ON t1.appln_id = t2.appln_id
ORDER BY t1.appln_id;

```

### 4. Computing the Patent Family Size
```SQL
SELECT 
    t1.appln_id, COUNT(t3.appln_id) AS family_size
FROM
    our_sample t1
        INNER JOIN
    tls219_inpadoc_fam t2 ON t2.appln_id = t1.appln_id
        INNER JOIN
    tls219_inpadoc_fam t3 ON t3.inpadoc_family_id = t2.inpadoc_family_id
GROUP BY t1.appln_id
ORDER BY t1.appln_id;
```

### 5. Computing the Patent Family Size (adapted to measure the geographic family size)
```SQL
SELECT 
    t1.appln_id,
    COUNT(DISTINCT t4.publn_auth) AS geog_family_size
FROM
    our_sample t1
        INNER JOIN
    tls219_inpadoc_fam t2 ON t2.appln_id = t1.appln_id
        INNER JOIN
    tls219_inpadoc_fam t3 ON t3.inpadoc_family_id = t2.inpadoc_family_id
        INNER JOIN
    tls211_pat_publn t4 ON t4.appln_id = t3.appln_id
WHERE
    t4.publn_auth != 'WO'
GROUP BY t1.appln_id
ORDER BY t1.appln_id;
```

### 6. Counting Patents by Country
```SQL
SELECT 
    person_ctry_code, SUM(tot_in_ctry/tot_in_patent) AS fractional_count
FROM
    (SELECT 
        t.appln_id,
        ifnull(t1.person_ctry_code, '') AS person_ctry_code,
        ifnull(t1.tot_in_ctry, 1) AS tot_in_ctry,
        ifnull(t2.tot_in_patent, 1) AS tot_in_patent
    FROM
        our_sample t
            LEFT OUTER JOIN 
            --> Accounts for missing inventor references in
            tls207_pers_appln table
        (SELECT
            a.appln_id,
            b.person_ctry_code,
            COUNT(b.person_id) AS tot_in_ctry
        FROM
            tls207_pers_appln a
            INNER JOIN tls206_person b ON a.person_id = b.person_id
        WHERE
            a.invt_seq_nr > 0
        GROUP BY a.appln_id, person_ctry_code
        --> Compiles country-level count of inventors per patent 
        ) t1 ON t.appln_id = t1.appln_id
            LEFT OUTER JOIN 
        (SELECT 
            appln_id, MAX(invt_seq_nr) AS tot_in_patent
        FROM
            tls207_pers_appln
        GROUP BY appln_id HAVING MAX(invt_seq_nr) > 0
        --> Compiles total count of inventors per patent
        ) t2 ON t.appln_id = t2.appln_id
    ) our_sample_with_country
GROUP BY person_ctry_code
ORDER BY SUM(tot_in_ctry/tot_in_patent) DESC;
```

### 7. Identifying Patents Resulting from International Collaborations
```SQL
SELECT 
    t1.appln_id,
    COUNT(DISTINCT t3.person_ctry_code) AS nb_locations
FROM
    our_sample t1
        INNER JOIN
    tls207_pers_appln t2 ON t1.appln_id = t2.appln_id
        INNER JOIN
    tls206_person t3 ON t2.person_id = t3.person_id
WHERE
    t3.person_ctry_code IS NOT NULL
        AND t2.invt_seq_nr > 0
GROUP BY t1.appln_id
ORDER BY COUNT(DISTINCT t3.person_ctry_code) DESC , t1.appln_id ASC;

```

### 8. Counting Citations Received
```SQL
SELECT 
    t1.appln_id, COUNT(distinct t3.pat_publn_id) AS cites_3y
FROM
    our_sample t1
        INNER JOIN
    (SELECT 
        appln_id, MIN(publn_date) AS earliest_date
    FROM
        tls211_pat_publn
    GROUP BY appln_id) t2 ON t1.appln_id = t2.appln_id
        INNER JOIN
    tls211_pat_publn t2b ON t2b.appln_id = t2.appln_id
        INNER JOIN
    tls212_citation t3 ON t2b.pat_publn_id = t3.cited_pat_publn_id
        INNER JOIN
    tls211_pat_publn t4 ON t3.pat_publn_id = t4.pat_publn_id
WHERE
    t2b.publn_auth = 'DE'
        AND t4.publn_auth = 'EP'
        AND YEAR(t2.earliest_date) != 9999
        AND YEAR(t4.publn_date) != 9999
        AND t4.publn_date <= DATE_ADD(t2.earliest_date,
        INTERVAL 3 YEAR)
GROUP BY t1.appln_id
ORDER BY COUNT(distinct t3.pat_publn_id) DESC , t1.appln_id;
```

### 9. Obtaining Grant Information
```SQL
SELECT 
    t1.appln_id, MAX(t2.publn_first_grant) AS granted
FROM
    our_sample t1
        INNER JOIN
    tls211_pat_publn t2 ON t1.appln_id = t2.appln_id
WHERE
    t1.appln_auth = 'GB'
        AND t1.appln_kind = 'A'
GROUP BY t1.appln_id
ORDER BY t1.appln_id;
```

### 10. Linking Patstat with Data Provided by National Patent Offices
```SQL
SELECT DISTINCT
    t1.appln_id,
    t2.publn_nr AS publn_nr_patstat,
    CONCAT('GB', RIGHT(t2.publn_nr, 7)) AS publn_nr_ukipo
FROM
    our_sample t1
        INNER JOIN
    tls211_pat_publn t2 ON t1.appln_id = t2.appln_id
WHERE
    t1.appln_auth = 'GB'
        AND t1.appln_kind = 'A'
        AND t2.publn_kind != 'D0'
ORDER BY t1.appln_id;
```