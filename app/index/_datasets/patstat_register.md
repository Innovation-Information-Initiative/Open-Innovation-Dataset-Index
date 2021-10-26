---
layout: default
code: https://github.com/gderasse/patstat_register
cost: € 1.420,00 - € 1.460,00
description: 'This database contains bibliographic and legal event data on published
  European and Euro-PCT patent applications.


  Like the core PATSTAT database, it is maintained by the EPO, however PATSTAT Register
  only contains information about patent applications at the European Patent Ofﬁce
  (EPO). The information in PATSTAT Register is, however, considerably deeper and
  more detailed.'
documentation: https://www.epo.org/searching-for-patents/business/patstat.html
location: https://www.epo.org/searching-for-patents/business/patstat.html
maintained_by: EPO
record_creation_timestamp: 10/04/2021
shortname: patstat_register
tags:
- Europe
- ' patents'
- ' legal'
- ' citations'
terms_of_use: Requires a subscription to access
title: Patstat Register
uuid: eb43fc38-8786-4b0f-b3b8-b9d610f456ed
---

This database contains bibliographic and legal event data on published European and Euro-PCT patent applications.

Like the core PATSTAT database, it is maintained by the EPO, however PATSTAT Register only contains information about patent applications at the European Patent Ofﬁce (EPO). The information in PATSTAT Register is, however, considerably deeper and more detailed.

Their example queries are reproduced below, and are also available [on GitHub](https://github.com/gderasse/patstat_register).


### 1. Identification of Patents by Technology Field

```sql
CREATE TABLE wind_patents AS 
SELECT 
   DISTINCT t1.appln_id 
FROM
   tls201_appln t1
      INNER JOIN
   tls209_appln_ipc t9 ON t1.appln_id = t9.appln_id
WHERE
   t1.appln_auth = 'EP'
      AND (t1.appln_kind = 'A' OR t1.appln_kind = 'W')
      AND year(t1.appln_filing_date) BETWEEN 2000 AND 2010
      AND t9.ipc_class_symbol LIKE 'F03D%'
```

### 2. Identification of Patents by Technology Field

```sql
SELECT 
   r101.id, r101.appln_id, 
   count(DISTINCT t212.cited_pat_publn_id) AS n_cit
FROM
   tls212_citation t212 
      INNER JOIN
   tls211_pat_publn t211 ON t211.pat_publn_id = t212.pat_publn_id
      INNER JOIN
   wind_patents wp ON wp.appln_id = t211.appln_id
      INNER JOIN
   reg101_appln r101 ON r101.appln_id = wp.appln_id
WHERE
   t212.pat_citn_seq_nr > 0
GROUP BY r101.id, r101.appln_id 
ORDER BY n_cit DESC;
```
### 3. Identification of Patents by Technology Field

```sql
SELECT
   r101.id, r101.appln_id,
   count(DISTINCT r112.licensee_country) AS nb_lic_ctry
FROM
   wind_patents wp
      INNER JOIN  
   reg101_appln r101 ON wp.appln_id = r101.appln_id
      INNER JOIN  
   reg112_licensee_states r112 ON r101.id = r112.id
GROUP BY
   r101.id, r101.appln_id
ORDER BY nb_lic_ctry DESC;
```

### 4. 

```sql
SELECT
   r101.id, r101.appln_id, max(r107.set_seq_nr) AS nb_changes
FROM
   wind_patents wp
      INNER JOIN  
   reg101_appln r101 ON wp.appln_id = r101.appln_id
      INNER JOIN
   reg107_parties r107 ON r101.id = r107.id
WHERE 
   r107.type = 'A'
GROUP BY 
   r101.id, r101.appln_id    
ORDER BY 
   nb_changes DESC, r101.id ASC;
```

### 5.

```sql
SELECT
   r101.id, r101.appln_id, r101.appln_filing_date, 
   r301.event_date AS exam_date, 
   datediff(r301.event_date, r101.appln_filing_date) 
   AS days_to_exam 
FROM
   wind_patents wp
      INNER JOIN  
   reg101_appln r101 ON wp.appln_id = r101.appln_id
      INNER JOIN 
   reg301_event_data r301 ON r101.id = r301.id
WHERE 
   event_code = '0009185'
ORDER BY 
   days_to_exam ASC;
```

### 6.

```sql
SELECT 
   r107.id, p.appln_id, r107.bulletin_year, r107.bulletin_nr,
   r107.name
FROM
   reg107_parties r107
      INNER JOIN 
   (SELECT r102.id, r101.appln_id, 
           min(concat(cast(bulletin_year AS CHAR),
                      cast(bulletin_nr AS CHAR))) 
           AS bulletin_first_publication
   FROM 
      reg102_pat_publn r102
         INNER JOIN 
      reg101_appln r101 ON r101.id = r102.id
         INNER JOIN 
      wind_patents wp ON wp.appln_id = r101.appln_id
   GROUP BY 
      r102.id, r101.appln_id) p 
   ON r107.id = p.id 
      AND concat(cast(r107.bulletin_year AS CHAR),
                 cast(r107.bulletin_nr AS CHAR))
          = p.bulletin_first_publication
WHERE 
   type = 'R'
ORDER BY 
   r107.id;
```

### 7.
```sql
SELECT
   r101.id, r101.appln_id, count(r301.id) AS nb_events
FROM
   wind_patents wp 
      INNER JOIN
   reg101_appln r101 ON wp.appln_id = r101.appln_id
      INNER JOIN
   reg301_event_data r301 ON r101.id = r301.id
WHERE 
   r301.event_code IN('0008299OPPO','0009260','EPIDOSCLIM1',
   'EPIDOSCRVR1','EPIDOSCRVR6','EPIDOSNLIM1','EPIDOSNRVR1',
   'EPIDOSNRVR6')
GROUP BY 
   r101.id, r101.appln_id
ORDER BY 
   nb_events DESC;
```

### 8.

```sql
SELECT
   r101.id, r101.appln_id,
   count(DISTINCT l501ep) AS nb_validated_states
FROM
   reg101_appln r101 
      INNER JOIN
   wind_patents wp ON r101.appln_id = wp.appln_id
      INNER JOIN
   tls221_inpadoc_prs t221 ON r101.appln_id = t221.appln_id
WHERE 
   prs_code = 'PGFP'
GROUP BY 
   r101.id, r101.appln_id
ORDER BY 
   nb_validated_states DESC, r101.id ASC;
```

### 9.

```sql
SELECT
   DISTINCT r107.name,
   round(count(*) / count(DISTINCT r201.id), 2) AS avg_proc_steps
FROM  
   wind_patents wp
      INNER JOIN 
   reg101_appln r101 ON wp.appln_id = r101.appln_id
      INNER JOIN
   reg201_proc_step r201 ON r101.id = r201.id
      INNER JOIN
   reg107_parties r107 ON r107.id = r201.id
WHERE 
   r107.type = 'A' 
      AND r107.is_latest = 'Y'
GROUP BY 
   r107.name
ORDER BY 
   avg_proc_steps DESC, 
   r107.name;
```