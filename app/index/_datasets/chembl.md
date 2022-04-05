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
schema_fields: '[''caloha_id'', ''smarts'', ''chirality'', ''l3'', ''applicant_full_name'',
  ''entity_type'', ''res_stem_id'', ''acd_most_apka'', ''syn_type'', ''mutation'',
  ''prodrug'', ''tbl'', ''innovator_company'', ''component_type'', ''sei'', ''ro3_pass'',
  ''class_level'', ''mc_target_type'', ''usan_stem'', ''alert_name'', ''hba_lipinski'',
  ''warnref_id'', ''db_version'', ''drug_product_flag'', ''cell_ontology_id'', ''cx_logp'',
  ''patent_id'', ''curation_comment'', ''helm_notation'', ''end_position'', ''hrac_class_id'',
  ''met_conversion'', ''molregno'', ''metabolite_record_id'', ''last_page'', ''tid'',
  ''num_alerts'', ''qudt_units'', ''prediction_method'', ''src_compound_id'', ''standard_upper_value'',
  ''mesh_id'', ''standard_units'', ''num_ro5_violations'', ''label'', ''canonical_smiles'',
  ''assay_organism'', ''src_id'', ''ref_id'', ''l4'', ''path'', ''enzyme_name'', ''disease_efficacy'',
  ''targrel_id'', ''assay_subcellular_fraction'', ''relationship_type'', ''pref_name'',
  ''level4'', ''usan_substem'', ''start_position'', ''level3_description'', ''level4_description'',
  ''acd_logp'', ''compd_id'', ''source_domain_id'', ''tax_id'', ''qed_weighted'',
  ''l5'', ''patent_expire_date'', ''cx_most_apka'', ''ref_url'', ''compound_key'',
  ''type'', ''title'', ''delist_flag'', ''l1'', ''strength'', ''black_box_warning'',
  ''component_id'', ''binding_site_comment'', ''status'', ''product_id'', ''cell_id'',
  ''parent_go_id'', ''relation'', ''assay_id'', ''issue'', ''confidence_score'', ''protein_class_desc'',
  ''db_source'', ''ddd_admr'', ''ad_type'', ''description'', ''cell_description'',
  ''country'', ''stem'', ''bto_id'', ''standard_inchi_key'', ''selectivity_comment'',
  ''uo_units'', ''molecular_species'', ''first_page'', ''smid'', ''oc_id'', ''assay_param_id'',
  ''pathway_id'', ''updated_on'', ''src_assay_id'', ''mol_irac_id'', ''published_type'',
  ''dosed_ingredient'', ''irac_code'', ''molecule_type'', ''organism'', ''bao_format'',
  ''rtb'', ''withdrawn_flag'', ''submission_date'', ''idx'', ''mol_hrac_id'', ''assay_source'',
  ''full_mwt'', ''cell_name'', ''pathway_key'', ''isoform'', ''src_short_name'', ''ingredient'',
  ''parameter_value'', ''abstract'', ''drug_record_id'', ''doc_id'', ''src_description'',
  ''level1'', ''availability_type'', ''drug_substance_flag'', ''standard_type'', ''efo_id'',
  ''variant_id'', ''set_name'', ''site_residues'', ''downgraded'', ''mc_target_name'',
  ''cpd_str_alert_id'', ''research_stem'', ''parenteral'', ''entity_id'', ''irac_class_id'',
  ''comp_class_id'', ''withdrawn_reason'', ''class_type'', ''first_approval'', ''rgid'',
  ''doc_type'', ''ap_id'', ''units'', ''aspect'', ''bei'', ''mol_atc_id'', ''substrate_record_id'',
  ''level2_description'', ''ridx'', ''molecular_mechanism'', ''activity_count'', ''metref_id'',
  ''max_phase_for_ind'', ''withdrawn_year'', ''related_tid'', ''publication_number'',
  ''sitecomp_id'', ''indication_class'', ''compsyn_id'', ''molsyn_id'', ''standard_value'',
  ''hba'', ''mol_frac_id'', ''usan_stem_id'', ''toid'', ''num_lipinski_ro5_violations'',
  ''dosage_form'', ''biocomp_id'', ''published_units'', ''route'', ''withdrawn_country'',
  ''level1_description'', ''synonyms'', ''cell_source_organism'', ''alert_set_id'',
  ''efo_term'', ''tissue_id'', ''natural_product'', ''site_id'', ''published_relation'',
  ''hbd'', ''inorganic_flag'', ''target_desc'', ''species_group_flag'', ''mesh_heading'',
  ''domain_name'', ''annotation'', ''parent_molregno'', ''sequence_md5sum'', ''acd_most_bpka'',
  ''assay_class_id'', ''tid_fixed'', ''cell_source_tissue'', ''mecref_id'', ''component_synonym'',
  ''target_mapping'', ''assay_strain'', ''ddd_value'', ''mw_freebase'', ''enzyme_tid'',
  ''activity_comment'', ''log_id'', ''updated_by'', ''bao_endpoint'', ''assay_type'',
  ''parameter_type'', ''warning_id'', ''homologue'', ''standard_flag'', ''last_active'',
  ''hbd_lipinski'', ''ass_cls_map_id'', ''acd_logd'', ''protclasssyn_id'', ''full_molformula'',
  ''result_flag'', ''oral'', ''usan_stem_definition'', ''short_name'', ''normal_range_min'',
  ''parent_type'', ''cx_logd'', ''mec_id'', ''active_molregno'', ''comments'', ''previous_company'',
  ''atc_code'', ''version'', ''therapeutic_flag'', ''published_value'', ''structure_type'',
  ''stat'', ''aromatic_rings'', ''who_extra'', ''withdrawn_class'', ''as_id'', ''site_name'',
  ''priority'', ''activity_id'', ''first_in_class'', ''warning_type'', ''warning_country'',
  ''ddd_id'', ''actsm_id'', ''active_ingredient'', ''level3'', ''compound_name'',
  ''alogp'', ''prod_pat_id'', ''value'', ''stem_class'', ''volume'', ''domain_type'',
  ''protein_class_synonym'', ''definition'', ''patent_no'', ''authors'', ''mechanism_comment'',
  ''journal'', ''usan_year'', ''psa'', ''aidx'', ''uberon_id'', ''go_id'', ''frac_class_id'',
  ''assay_desc'', ''formulation_id'', ''l8'', ''cidx'', ''trade_name'', ''level5'',
  ''normal_range_max'', ''l6'', ''warning_class'', ''potential_duplicate'', ''mc_tax_id'',
  ''pubmed_id'', ''approval_date'', ''nda_type'', ''accession'', ''heavy_atoms'',
  ''warning_description'', ''frac_code'', ''cl_lincs_id'', ''hrac_code'', ''le'',
  ''company'', ''name'', ''target_type'', ''domain_id'', ''domain_description'', ''assay_tax_id'',
  ''major_class'', ''warning_year'', ''assay_tissue'', ''co_stem_id'', ''assay_test_type'',
  ''doi'', ''molfile'', ''creation_date'', ''sequence'', ''assay_cell_type'', ''chembl_id'',
  ''polymer_flag'', ''cell_source_tax_id'', ''l7'', ''ref_type'', ''standard_relation'',
  ''alert_id'', ''pchembl_value'', ''lle'', ''mw_monoisotopic'', ''ddd_comment'',
  ''max_phase'', ''mc_organism'', ''comp_go_id'', ''data_validity_comment'', ''protein_class_id'',
  ''text_value'', ''curated_by'', ''confidence'', ''topical'', ''upper_value'', ''met_id'',
  ''mc_target_accession'', ''who_name'', ''cellosaurus_id'', ''orig_description'',
  ''l2'', ''mechanism_of_action'', ''year'', ''standard_inchi'', ''direct_interaction'',
  ''met_comment'', ''assay_category'', ''clo_id'', ''drugind_id'', ''level2'', ''patent_use_code'',
  ''std_act_id'', ''parent_id'', ''job_id'', ''targcomp_id'', ''action_type'', ''relationship'',
  ''indref_id'', ''chebi_par_id'', ''relationship_desc'', ''cx_most_bpka'', ''record_id'',
  ''subgroup'', ''bao_id'', ''standard_text_value'', ''ddd_units'', ''predbind_id'',
  ''source'']'
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