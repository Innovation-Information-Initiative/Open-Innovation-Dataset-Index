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
schema_fields: '[''relation'', ''activity_id'', ''chirality'', ''parent_type'', ''downgraded'',
  ''hrac_class_id'', ''cell_ontology_id'', ''assay_param_id'', ''mol_atc_id'', ''prod_pat_id'',
  ''assay_strain'', ''substrate_record_id'', ''acd_most_bpka'', ''prodrug'', ''cell_source_tax_id'',
  ''assay_category'', ''bei'', ''confidence_score'', ''metref_id'', ''smarts'', ''active_ingredient'',
  ''related_tid'', ''assay_source'', ''site_residues'', ''cx_most_bpka'', ''curated_by'',
  ''upper_value'', ''l7'', ''num_alerts'', ''homologue'', ''direct_interaction'',
  ''assay_type'', ''first_approval'', ''approval_date'', ''level3'', ''country'',
  ''source_domain_id'', ''comp_class_id'', ''updated_on'', ''standard_inchi'', ''max_phase_for_ind'',
  ''l6'', ''src_compound_id'', ''protclasssyn_id'', ''efo_id'', ''tissue_id'', ''normal_range_min'',
  ''data_validity_comment'', ''compound_name'', ''compsyn_id'', ''confidence'', ''src_short_name'',
  ''drugind_id'', ''mc_organism'', ''chebi_par_id'', ''src_id'', ''withdrawn_country'',
  ''sequence_md5sum'', ''mol_frac_id'', ''creation_date'', ''tax_id'', ''stem_class'',
  ''indref_id'', ''l5'', ''withdrawn_flag'', ''cx_most_apka'', ''molecular_mechanism'',
  ''relationship_type'', ''heavy_atoms'', ''usan_stem_definition'', ''uberon_id'',
  ''short_name'', ''innovator_company'', ''mec_id'', ''patent_expire_date'', ''entity_type'',
  ''mechanism_comment'', ''hba_lipinski'', ''delist_flag'', ''prediction_method'',
  ''l4'', ''cell_source_tissue'', ''value'', ''acd_logd'', ''mw_freebase'', ''applicant_full_name'',
  ''parent_id'', ''qudt_units'', ''level5'', ''standard_type'', ''alogp'', ''polymer_flag'',
  ''orig_description'', ''psa'', ''molecule_type'', ''definition'', ''parameter_type'',
  ''molfile'', ''go_id'', ''mol_hrac_id'', ''warning_type'', ''log_id'', ''standard_upper_value'',
  ''sitecomp_id'', ''domain_id'', ''cell_id'', ''ridx'', ''who_name'', ''company'',
  ''previous_company'', ''ddd_units'', ''hba'', ''withdrawn_class'', ''volume'', ''comp_go_id'',
  ''usan_stem'', ''natural_product'', ''full_mwt'', ''ddd_comment'', ''cell_source_organism'',
  ''efo_term'', ''selectivity_comment'', ''warning_country'', ''mw_monoisotopic'',
  ''usan_year'', ''cx_logp'', ''bao_format'', ''molregno'', ''cpd_str_alert_id'',
  ''target_mapping'', ''cellosaurus_id'', ''ddd_value'', ''version'', ''withdrawn_reason'',
  ''assay_organism'', ''oc_id'', ''doc_type'', ''product_id'', ''parameter_value'',
  ''compd_id'', ''assay_desc'', ''relationship_desc'', ''frac_code'', ''num_lipinski_ro5_violations'',
  ''who_extra'', ''ad_type'', ''toid'', ''level4'', ''bao_id'', ''assay_cell_type'',
  ''target_type'', ''title'', ''description'', ''aspect'', ''major_class'', ''published_type'',
  ''activity_count'', ''rtb'', ''result_flag'', ''warning_year'', ''mesh_id'', ''journal'',
  ''warning_description'', ''comments'', ''protein_class_id'', ''availability_type'',
  ''species_group_flag'', ''abstract'', ''trade_name'', ''acd_logp'', ''route'', ''molecular_species'',
  ''patent_no'', ''pchembl_value'', ''protein_class_desc'', ''start_position'', ''acd_most_apka'',
  ''binding_site_comment'', ''hrac_code'', ''as_id'', ''mc_target_name'', ''aromatic_rings'',
  ''hbd'', ''sei'', ''bto_id'', ''published_units'', ''src_assay_id'', ''topical'',
  ''entity_id'', ''parent_molregno'', ''num_ro5_violations'', ''pathway_key'', ''l3'',
  ''mesh_heading'', ''irac_code'', ''level2'', ''authors'', ''patent_use_code'', ''standard_units'',
  ''warnref_id'', ''max_phase'', ''mutation'', ''formulation_id'', ''cl_lincs_id'',
  ''caloha_id'', ''mc_target_type'', ''parenteral'', ''drug_product_flag'', ''subgroup'',
  ''ass_cls_map_id'', ''normal_range_max'', ''assay_test_type'', ''usan_substem'',
  ''frac_class_id'', ''disease_efficacy'', ''bao_endpoint'', ''action_type'', ''variant_id'',
  ''pref_name'', ''stem'', ''hbd_lipinski'', ''db_version'', ''alert_id'', ''molsyn_id'',
  ''ddd_admr'', ''mecref_id'', ''syn_type'', ''ingredient'', ''name'', ''standard_flag'',
  ''helm_notation'', ''level1'', ''co_stem_id'', ''year'', ''status'', ''issue'',
  ''set_name'', ''class_type'', ''compound_key'', ''component_synonym'', ''strength'',
  ''curation_comment'', ''targcomp_id'', ''assay_tissue'', ''level4_description'',
  ''potential_duplicate'', ''standard_inchi_key'', ''parent_go_id'', ''withdrawn_year'',
  ''record_id'', ''units'', ''assay_class_id'', ''stat'', ''end_position'', ''nda_type'',
  ''submission_date'', ''predbind_id'', ''annotation'', ''l8'', ''domain_description'',
  ''assay_id'', ''domain_type'', ''actsm_id'', ''source'', ''isoform'', ''ref_type'',
  ''uo_units'', ''warning_class'', ''idx'', ''dosed_ingredient'', ''type'', ''component_type'',
  ''relationship'', ''pathway_id'', ''assay_tax_id'', ''indication_class'', ''tid'',
  ''met_conversion'', ''clo_id'', ''res_stem_id'', ''rgid'', ''db_source'', ''inorganic_flag'',
  ''tbl'', ''mechanism_of_action'', ''published_value'', ''biocomp_id'', ''active_molregno'',
  ''structure_type'', ''smid'', ''dosage_form'', ''job_id'', ''ddd_id'', ''l1'', ''metabolite_record_id'',
  ''met_comment'', ''l2'', ''research_stem'', ''activity_comment'', ''warning_id'',
  ''assay_subcellular_fraction'', ''ref_id'', ''standard_relation'', ''pubmed_id'',
  ''drug_substance_flag'', ''cell_description'', ''standard_text_value'', ''ro3_pass'',
  ''text_value'', ''synonyms'', ''oral'', ''met_id'', ''qed_weighted'', ''tid_fixed'',
  ''alert_name'', ''first_in_class'', ''doi'', ''target_desc'', ''patent_id'', ''class_level'',
  ''alert_set_id'', ''standard_value'', ''site_id'', ''last_page'', ''mc_target_accession'',
  ''level2_description'', ''le'', ''therapeutic_flag'', ''publication_number'', ''path'',
  ''doc_id'', ''level1_description'', ''accession'', ''enzyme_tid'', ''sequence'',
  ''targrel_id'', ''black_box_warning'', ''full_molformula'', ''lle'', ''canonical_smiles'',
  ''updated_by'', ''ref_url'', ''chembl_id'', ''domain_name'', ''site_name'', ''irac_class_id'',
  ''cidx'', ''enzyme_name'', ''component_id'', ''ap_id'', ''level3_description'',
  ''src_description'', ''aidx'', ''label'', ''mc_tax_id'', ''usan_stem_id'', ''last_active'',
  ''cell_name'', ''cx_logd'', ''organism'', ''atc_code'', ''mol_irac_id'', ''protein_class_synonym'',
  ''published_relation'', ''priority'', ''std_act_id'', ''first_page'', ''drug_record_id'']'
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