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
schema_fields: '[''assay_class_id'', ''l8'', ''confidence_score'', ''action_type'',
  ''cl_lincs_id'', ''protein_class_desc'', ''previous_company'', ''published_value'',
  ''oc_id'', ''smid'', ''withdrawn_reason'', ''bao_endpoint'', ''isoform'', ''metref_id'',
  ''version'', ''hbd'', ''activity_count'', ''compd_id'', ''max_phase_for_ind'', ''availability_type'',
  ''entity_type'', ''enzyme_tid'', ''lle'', ''usan_year'', ''publication_number'',
  ''molregno'', ''pchembl_value'', ''upper_value'', ''who_name'', ''assay_organism'',
  ''bao_id'', ''cx_logd'', ''level3_description'', ''withdrawn_year'', ''activity_id'',
  ''authors'', ''cell_name'', ''relationship_type'', ''doi'', ''mecref_id'', ''level1_description'',
  ''parent_id'', ''ref_type'', ''l5'', ''label'', ''research_stem'', ''caloha_id'',
  ''potential_duplicate'', ''assay_param_id'', ''downgraded'', ''ddd_admr'', ''prodrug'',
  ''standard_value'', ''doc_type'', ''src_description'', ''domain_id'', ''hbd_lipinski'',
  ''published_units'', ''protein_class_id'', ''alogp'', ''variant_id'', ''site_name'',
  ''black_box_warning'', ''targcomp_id'', ''patent_expire_date'', ''l1'', ''approval_date'',
  ''standard_type'', ''pubmed_id'', ''assay_cell_type'', ''psa'', ''product_id'',
  ''source_domain_id'', ''active_ingredient'', ''alert_set_id'', ''sequence'', ''drug_record_id'',
  ''abstract'', ''class_type'', ''l4'', ''parent_go_id'', ''level1'', ''activity_comment'',
  ''level5'', ''irac_class_id'', ''patent_use_code'', ''helm_notation'', ''binding_site_comment'',
  ''toid'', ''met_conversion'', ''l7'', ''stem'', ''tbl'', ''comp_go_id'', ''parent_type'',
  ''mw_monoisotopic'', ''set_name'', ''domain_type'', ''substrate_record_id'', ''tid_fixed'',
  ''enzyme_name'', ''bei'', ''accession'', ''log_id'', ''src_id'', ''alert_id'', ''compound_key'',
  ''published_relation'', ''drug_product_flag'', ''pathway_id'', ''updated_on'', ''withdrawn_country'',
  ''warning_id'', ''target_type'', ''met_comment'', ''warning_description'', ''natural_product'',
  ''assay_tissue'', ''creation_date'', ''applicant_full_name'', ''hba_lipinski'',
  ''molecular_species'', ''warnref_id'', ''acd_most_bpka'', ''mc_tax_id'', ''journal'',
  ''l3'', ''path'', ''acd_logd'', ''usan_substem'', ''hrac_code'', ''mol_frac_id'',
  ''ref_id'', ''company'', ''actsm_id'', ''level3'', ''acd_logp'', ''assay_tax_id'',
  ''mutation'', ''doc_id'', ''updated_by'', ''assay_strain'', ''chirality'', ''metabolite_record_id'',
  ''cell_source_organism'', ''entity_id'', ''active_molregno'', ''innovator_company'',
  ''title'', ''units'', ''level4_description'', ''ad_type'', ''pref_name'', ''polymer_flag'',
  ''rtb'', ''num_ro5_violations'', ''canonical_smiles'', ''le'', ''src_short_name'',
  ''parenteral'', ''confidence'', ''l2'', ''patent_no'', ''prod_pat_id'', ''status'',
  ''warning_year'', ''irac_code'', ''result_flag'', ''cx_most_apka'', ''warning_type'',
  ''mc_target_type'', ''drug_substance_flag'', ''targrel_id'', ''clo_id'', ''uberon_id'',
  ''mesh_id'', ''heavy_atoms'', ''last_page'', ''component_id'', ''full_molformula'',
  ''orig_description'', ''syn_type'', ''volume'', ''chebi_par_id'', ''chembl_id'',
  ''cidx'', ''first_page'', ''as_id'', ''qudt_units'', ''organism'', ''cpd_str_alert_id'',
  ''frac_class_id'', ''last_active'', ''co_stem_id'', ''bao_format'', ''mol_atc_id'',
  ''dosed_ingredient'', ''text_value'', ''formulation_id'', ''res_stem_id'', ''parameter_type'',
  ''submission_date'', ''class_level'', ''standard_units'', ''species_group_flag'',
  ''short_name'', ''standard_inchi_key'', ''stem_class'', ''met_id'', ''max_phase'',
  ''dosage_form'', ''atc_code'', ''selectivity_comment'', ''parameter_value'', ''direct_interaction'',
  ''sei'', ''stat'', ''first_in_class'', ''idx'', ''sequence_md5sum'', ''tid'', ''subgroup'',
  ''assay_id'', ''related_tid'', ''mw_freebase'', ''description'', ''molecular_mechanism'',
  ''homologue'', ''parent_molregno'', ''delist_flag'', ''name'', ''component_synonym'',
  ''compound_name'', ''cell_ontology_id'', ''who_extra'', ''level2'', ''assay_source'',
  ''mc_target_name'', ''domain_description'', ''efo_term'', ''std_act_id'', ''ingredient'',
  ''molecule_type'', ''definition'', ''indref_id'', ''mc_organism'', ''curation_comment'',
  ''rgid'', ''target_mapping'', ''standard_relation'', ''site_residues'', ''curated_by'',
  ''biocomp_id'', ''comments'', ''full_mwt'', ''aromatic_rings'', ''hrac_class_id'',
  ''usan_stem'', ''ridx'', ''l6'', ''country'', ''usan_stem_definition'', ''alert_name'',
  ''normal_range_min'', ''molsyn_id'', ''mechanism_comment'', ''cx_most_bpka'', ''trade_name'',
  ''db_version'', ''major_class'', ''strength'', ''pathway_key'', ''level2_description'',
  ''assay_type'', ''synonyms'', ''domain_name'', ''ddd_id'', ''predbind_id'', ''end_position'',
  ''standard_flag'', ''start_position'', ''ddd_value'', ''bto_id'', ''warning_country'',
  ''assay_test_type'', ''qed_weighted'', ''tissue_id'', ''molfile'', ''site_id'',
  ''compsyn_id'', ''mechanism_of_action'', ''first_approval'', ''mesh_heading'', ''aidx'',
  ''mc_target_accession'', ''standard_upper_value'', ''source'', ''acd_most_apka'',
  ''target_desc'', ''ap_id'', ''disease_efficacy'', ''comp_class_id'', ''relationship'',
  ''record_id'', ''relation'', ''ro3_pass'', ''job_id'', ''normal_range_max'', ''route'',
  ''efo_id'', ''usan_stem_id'', ''mol_irac_id'', ''uo_units'', ''prediction_method'',
  ''drugind_id'', ''assay_subcellular_fraction'', ''aspect'', ''src_assay_id'', ''withdrawn_class'',
  ''patent_id'', ''standard_text_value'', ''year'', ''src_compound_id'', ''component_type'',
  ''num_lipinski_ro5_violations'', ''inorganic_flag'', ''published_type'', ''smarts'',
  ''sitecomp_id'', ''tax_id'', ''num_alerts'', ''topical'', ''ref_url'', ''go_id'',
  ''protclasssyn_id'', ''mec_id'', ''standard_inchi'', ''value'', ''ddd_comment'',
  ''nda_type'', ''structure_type'', ''cx_logp'', ''data_validity_comment'', ''level4'',
  ''frac_code'', ''issue'', ''cellosaurus_id'', ''hba'', ''warning_class'', ''priority'',
  ''ass_cls_map_id'', ''ddd_units'', ''cell_source_tissue'', ''protein_class_synonym'',
  ''assay_desc'', ''relationship_desc'', ''cell_description'', ''assay_category'',
  ''therapeutic_flag'', ''mol_hrac_id'', ''cell_id'', ''annotation'', ''cell_source_tax_id'',
  ''db_source'', ''type'', ''indication_class'', ''withdrawn_flag'', ''oral'']'
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