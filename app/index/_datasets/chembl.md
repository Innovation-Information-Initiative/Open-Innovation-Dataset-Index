---
layout: default
bigquery: https://console.cloud.google.com/bigquery?p=patents-public-data&d=ebi_chembl&page=dataset
citation: '"The ChEMBL database in 2017." Anna Gaulton, Anne Hersey, Michał Nowotka,
  A Patrícia Bento, Jon Chambers, David Mendez, Prudence Mutowo, Francis Atkinson,
  Louisa J Bellis, Elena Cibrián-Uhalte, Mark Davies, Nathan Dedman, Anneli Karlsson,
  María Paula Magariños, John P Overington, George Papadatos, Ines Smit, Andrew R
  Leach Nucleic acids Research (2017) 45 (Database Issue), D945-D954'
contributors: European Bioinformatics Institute
cost: None
description: ChEMBL Data is a manually curated database of small molecules used in
  drug discovery, including information about existing patented drugs.
documentation: 'schema: https://www.ebi.ac.uk/chembl/db_schema


  '
last_edit: Mon, 04 Apr 2022 19:07:30 GMT
location: https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/chembl
maintained_by: EMBL-EBI, an outstation of European Molecular Biology Laboratory
related_publications: '

  ChEMBL: towards direct deposition of bioassay data.


  Mendez D, Gaulton A, Bento AP, Chambers J, De Veij M, Félix E, Magariños MP, Mosquera
  JF, Mutowo P, Nowotka M, Gordillo-Marañón M, Hunter F, Junco L, Mugumbate G, Rodriguez-Lopez
  M, Atkinson F, Bosc N, Radoux CJ, Segura-Cabrera A, Hersey A, Leach AR.


  — Nucleic Acids Res. 2019; 47(D1):D930-D940. doi: 10.1093/nar/gky1075

  '
schema_fields: '[''patent_id'', ''therapeutic_flag'', ''as_id'', ''domain_type'',
  ''level2'', ''molregno'', ''confidence_score'', ''assay_desc'', ''ref_id'', ''black_box_warning'',
  ''acd_most_apka'', ''priority'', ''drug_record_id'', ''active_molregno'', ''route'',
  ''mol_irac_id'', ''standard_value'', ''variant_id'', ''canonical_smiles'', ''ad_type'',
  ''assay_subcellular_fraction'', ''pubmed_id'', ''protein_class_id'', ''hbd'', ''units'',
  ''activity_count'', ''inorganic_flag'', ''status'', ''predbind_id'', ''indication_class'',
  ''standard_upper_value'', ''standard_inchi'', ''journal'', ''ap_id'', ''prodrug'',
  ''assay_class_id'', ''warning_type'', ''warning_year'', ''psa'', ''l5'', ''target_type'',
  ''standard_type'', ''innovator_company'', ''trade_name'', ''parent_id'', ''drug_product_flag'',
  ''doc_id'', ''rtb'', ''formulation_id'', ''active_ingredient'', ''chembl_id'', ''co_stem_id'',
  ''mutation'', ''l8'', ''usan_stem_definition'', ''short_name'', ''comp_go_id'',
  ''source_domain_id'', ''syn_type'', ''class_level'', ''homologue'', ''site_name'',
  ''sitecomp_id'', ''version'', ''compound_name'', ''site_id'', ''cidx'', ''related_tid'',
  ''set_name'', ''smid'', ''biocomp_id'', ''isoform'', ''target_mapping'', ''drugind_id'',
  ''compsyn_id'', ''published_relation'', ''met_comment'', ''rgid'', ''comp_class_id'',
  ''irac_code'', ''pchembl_value'', ''standard_relation'', ''cell_source_organism'',
  ''relationship_desc'', ''binding_site_comment'', ''res_stem_id'', ''mc_target_type'',
  ''relation'', ''who_extra'', ''molecular_species'', ''atc_code'', ''drug_substance_flag'',
  ''num_alerts'', ''mesh_id'', ''alert_set_id'', ''le'', ''hba_lipinski'', ''updated_on'',
  ''stem'', ''tax_id'', ''normal_range_max'', ''mw_monoisotopic'', ''accession'',
  ''potential_duplicate'', ''value'', ''doc_type'', ''go_id'', ''data_validity_comment'',
  ''actsm_id'', ''level4'', ''company'', ''ridx'', ''tissue_id'', ''selectivity_comment'',
  ''abstract'', ''pathway_id'', ''first_in_class'', ''comments'', ''max_phase'', ''natural_product'',
  ''cell_id'', ''warning_id'', ''mechanism_comment'', ''uberon_id'', ''protein_class_desc'',
  ''stem_class'', ''ddd_id'', ''country'', ''level1_description'', ''hrac_code'',
  ''mc_tax_id'', ''substrate_record_id'', ''lle'', ''molecule_type'', ''last_page'',
  ''previous_company'', ''relationship_type'', ''assay_tissue'', ''warning_description'',
  ''usan_stem'', ''tid'', ''cell_description'', ''protclasssyn_id'', ''oc_id'', ''hba'',
  ''protein_class_synonym'', ''text_value'', ''l7'', ''first_approval'', ''publication_number'',
  ''source'', ''level2_description'', ''end_position'', ''hrac_class_id'', ''efo_term'',
  ''usan_stem_id'', ''assay_test_type'', ''bao_id'', ''standard_flag'', ''assay_source'',
  ''cellosaurus_id'', ''mol_hrac_id'', ''mesh_heading'', ''class_type'', ''parent_molregno'',
  ''normal_range_min'', ''l4'', ''title'', ''curation_comment'', ''tid_fixed'', ''level3_description'',
  ''sequence_md5sum'', ''relationship'', ''full_mwt'', ''cx_most_bpka'', ''withdrawn_class'',
  ''organism'', ''submission_date'', ''standard_units'', ''bao_endpoint'', ''cell_name'',
  ''sei'', ''assay_cell_type'', ''clo_id'', ''tbl'', ''result_flag'', ''disease_efficacy'',
  ''targrel_id'', ''mol_frac_id'', ''mc_target_name'', ''full_molformula'', ''irac_class_id'',
  ''cell_source_tissue'', ''mw_freebase'', ''compound_key'', ''creation_date'', ''indref_id'',
  ''l2'', ''level4_description'', ''annotation'', ''authors'', ''num_lipinski_ro5_violations'',
  ''withdrawn_reason'', ''warning_class'', ''metabolite_record_id'', ''description'',
  ''max_phase_for_ind'', ''bto_id'', ''activity_comment'', ''site_residues'', ''oral'',
  ''chebi_par_id'', ''chirality'', ''db_version'', ''ingredient'', ''parameter_value'',
  ''type'', ''activity_id'', ''species_group_flag'', ''db_source'', ''first_page'',
  ''approval_date'', ''withdrawn_year'', ''molfile'', ''bei'', ''std_act_id'', ''published_units'',
  ''level3'', ''ddd_value'', ''src_id'', ''ddd_admr'', ''cx_logp'', ''parent_go_id'',
  ''entity_type'', ''applicant_full_name'', ''mecref_id'', ''direct_interaction'',
  ''src_assay_id'', ''ddd_comment'', ''job_id'', ''synonyms'', ''start_position'',
  ''year'', ''doi'', ''patent_no'', ''assay_strain'', ''withdrawn_flag'', ''path'',
  ''ddd_units'', ''molsyn_id'', ''parameter_type'', ''who_name'', ''cx_most_apka'',
  ''compd_id'', ''caloha_id'', ''ref_type'', ''assay_tax_id'', ''published_type'',
  ''withdrawn_country'', ''published_value'', ''enzyme_name'', ''enzyme_tid'', ''cell_ontology_id'',
  ''standard_text_value'', ''domain_name'', ''aspect'', ''assay_category'', ''mc_target_accession'',
  ''nda_type'', ''action_type'', ''downgraded'', ''major_class'', ''molecular_mechanism'',
  ''cell_source_tax_id'', ''cl_lincs_id'', ''acd_most_bpka'', ''mec_id'', ''usan_year'',
  ''component_synonym'', ''assay_id'', ''assay_param_id'', ''alogp'', ''component_id'',
  ''helm_notation'', ''standard_inchi_key'', ''availability_type'', ''alert_name'',
  ''hbd_lipinski'', ''topical'', ''dosed_ingredient'', ''strength'', ''target_desc'',
  ''last_active'', ''curated_by'', ''met_conversion'', ''definition'', ''aromatic_rings'',
  ''num_ro5_violations'', ''level5'', ''warning_country'', ''domain_description'',
  ''prod_pat_id'', ''assay_type'', ''entity_id'', ''idx'', ''polymer_flag'', ''src_compound_id'',
  ''uo_units'', ''pathway_key'', ''volume'', ''acd_logp'', ''dosage_form'', ''delist_flag'',
  ''aidx'', ''orig_description'', ''name'', ''mc_organism'', ''heavy_atoms'', ''issue'',
  ''subgroup'', ''met_id'', ''cpd_str_alert_id'', ''frac_class_id'', ''component_type'',
  ''src_short_name'', ''efo_id'', ''l3'', ''cx_logd'', ''level1'', ''stat'', ''targcomp_id'',
  ''mol_atc_id'', ''usan_substem'', ''l6'', ''research_stem'', ''frac_code'', ''patent_use_code'',
  ''product_id'', ''label'', ''log_id'', ''qed_weighted'', ''record_id'', ''confidence'',
  ''parent_type'', ''prediction_method'', ''l1'', ''alert_id'', ''mechanism_of_action'',
  ''parenteral'', ''bao_format'', ''ref_url'', ''ro3_pass'', ''qudt_units'', ''metref_id'',
  ''domain_id'', ''src_description'', ''upper_value'', ''structure_type'', ''sequence'',
  ''toid'', ''assay_organism'', ''patent_expire_date'', ''ass_cls_map_id'', ''acd_logd'',
  ''smarts'', ''updated_by'', ''pref_name'', ''warnref_id'']'
shortname: chembl
tags:
- biotechnology
- health
- chemical
- bioinformatics
- medical
terms_of_use: CC BY-SA 3.0
title: ChEMBL
uuid: e232a192-965c-4ec9-904c-155b6dfe56c5
---