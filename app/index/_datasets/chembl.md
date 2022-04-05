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
schema_fields: '[''withdrawn_flag'', ''parent_id'', ''published_type'', ''std_act_id'',
  ''dosed_ingredient'', ''confidence_score'', ''molecule_type'', ''first_in_class'',
  ''cell_name'', ''published_value'', ''as_id'', ''mol_irac_id'', ''targrel_id'',
  ''usan_substem'', ''organism'', ''entity_id'', ''molfile'', ''parent_molregno'',
  ''warnref_id'', ''product_id'', ''biocomp_id'', ''stem'', ''metref_id'', ''toid'',
  ''warning_type'', ''lle'', ''domain_name'', ''hrac_code'', ''applicant_full_name'',
  ''tax_id'', ''confidence'', ''protein_class_id'', ''target_mapping'', ''uo_units'',
  ''standard_type'', ''bao_format'', ''ddd_admr'', ''relationship'', ''nda_type'',
  ''source'', ''num_lipinski_ro5_violations'', ''related_tid'', ''compsyn_id'', ''standard_value'',
  ''mc_target_name'', ''previous_company'', ''molsyn_id'', ''ref_type'', ''short_name'',
  ''cl_lincs_id'', ''therapeutic_flag'', ''activity_comment'', ''polymer_flag'', ''patent_no'',
  ''dosage_form'', ''level3_description'', ''cx_logd'', ''standard_inchi_key'', ''warning_id'',
  ''assay_organism'', ''level4_description'', ''molecular_mechanism'', ''rtb'', ''class_type'',
  ''isoform'', ''binding_site_comment'', ''doc_id'', ''who_name'', ''domain_description'',
  ''warning_description'', ''synonyms'', ''cell_source_organism'', ''frac_code'',
  ''qudt_units'', ''frac_class_id'', ''version'', ''published_relation'', ''tid_fixed'',
  ''hbd_lipinski'', ''acd_logd'', ''homologue'', ''mol_hrac_id'', ''cell_description'',
  ''first_approval'', ''res_stem_id'', ''l4'', ''qed_weighted'', ''updated_by'', ''warning_class'',
  ''alert_name'', ''parent_type'', ''db_version'', ''mecref_id'', ''country'', ''mc_target_type'',
  ''max_phase_for_ind'', ''parenteral'', ''topical'', ''indication_class'', ''mol_atc_id'',
  ''source_domain_id'', ''drug_record_id'', ''trade_name'', ''syn_type'', ''direct_interaction'',
  ''prediction_method'', ''canonical_smiles'', ''curation_comment'', ''assay_desc'',
  ''subgroup'', ''start_position'', ''num_alerts'', ''site_id'', ''le'', ''submission_date'',
  ''ref_url'', ''helm_notation'', ''parent_go_id'', ''src_id'', ''assay_subcellular_fraction'',
  ''actsm_id'', ''chirality'', ''structure_type'', ''species_group_flag'', ''availability_type'',
  ''chebi_par_id'', ''issue'', ''assay_source'', ''abstract'', ''research_stem'',
  ''mw_freebase'', ''selectivity_comment'', ''doc_type'', ''cidx'', ''l7'', ''year'',
  ''standard_units'', ''aidx'', ''value'', ''relationship_desc'', ''site_residues'',
  ''set_name'', ''active_molregno'', ''relation'', ''pathway_id'', ''domain_id'',
  ''l1'', ''psa'', ''data_validity_comment'', ''assay_type'', ''action_type'', ''indref_id'',
  ''cellosaurus_id'', ''mc_target_accession'', ''usan_stem_id'', ''full_mwt'', ''record_id'',
  ''volume'', ''text_value'', ''level1'', ''journal'', ''oc_id'', ''sequence_md5sum'',
  ''ridx'', ''smarts'', ''enzyme_tid'', ''enzyme_name'', ''parameter_type'', ''status'',
  ''path'', ''level5'', ''label'', ''l2'', ''sei'', ''molecular_species'', ''accession'',
  ''potential_duplicate'', ''log_id'', ''go_id'', ''cell_ontology_id'', ''withdrawn_reason'',
  ''sequence'', ''standard_upper_value'', ''published_units'', ''target_desc'', ''num_ro5_violations'',
  ''acd_most_apka'', ''targcomp_id'', ''drug_product_flag'', ''compound_key'', ''ingredient'',
  ''variant_id'', ''job_id'', ''target_type'', ''l5'', ''assay_strain'', ''comp_class_id'',
  ''met_id'', ''normal_range_max'', ''curated_by'', ''last_active'', ''last_page'',
  ''stem_class'', ''innovator_company'', ''irac_code'', ''clo_id'', ''acd_most_bpka'',
  ''normal_range_min'', ''alogp'', ''assay_test_type'', ''cpd_str_alert_id'', ''downgraded'',
  ''result_flag'', ''substrate_record_id'', ''mutation'', ''cell_source_tax_id'',
  ''mechanism_of_action'', ''efo_id'', ''compd_id'', ''warning_year'', ''route'',
  ''met_comment'', ''molregno'', ''strength'', ''component_id'', ''ddd_units'', ''l8'',
  ''level2_description'', ''ddd_id'', ''assay_tissue'', ''mec_id'', ''mesh_id'', ''usan_year'',
  ''tbl'', ''bao_endpoint'', ''disease_efficacy'', ''major_class'', ''ddd_value'',
  ''bto_id'', ''relationship_type'', ''comments'', ''heavy_atoms'', ''comp_go_id'',
  ''assay_class_id'', ''level2'', ''level3'', ''priority'', ''creation_date'', ''mc_organism'',
  ''compound_name'', ''src_short_name'', ''level4'', ''hrac_class_id'', ''alert_id'',
  ''standard_inchi'', ''patent_expire_date'', ''entity_type'', ''upper_value'', ''hba'',
  ''component_synonym'', ''ad_type'', ''title'', ''smid'', ''rgid'', ''idx'', ''inorganic_flag'',
  ''authors'', ''pathway_key'', ''ref_id'', ''level1_description'', ''mol_frac_id'',
  ''approval_date'', ''prodrug'', ''predbind_id'', ''db_source'', ''protein_class_synonym'',
  ''pchembl_value'', ''who_extra'', ''bao_id'', ''aspect'', ''units'', ''tid'', ''co_stem_id'',
  ''mw_monoisotopic'', ''src_assay_id'', ''drug_substance_flag'', ''standard_relation'',
  ''assay_category'', ''usan_stem_definition'', ''chembl_id'', ''natural_product'',
  ''alert_set_id'', ''prod_pat_id'', ''site_name'', ''definition'', ''hba_lipinski'',
  ''protein_class_desc'', ''class_level'', ''irac_class_id'', ''drugind_id'', ''ddd_comment'',
  ''uberon_id'', ''domain_type'', ''company'', ''full_molformula'', ''name'', ''cell_id'',
  ''updated_on'', ''first_page'', ''active_ingredient'', ''activity_count'', ''cx_most_bpka'',
  ''orig_description'', ''patent_id'', ''annotation'', ''parameter_value'', ''bei'',
  ''sitecomp_id'', ''withdrawn_class'', ''l3'', ''withdrawn_country'', ''ass_cls_map_id'',
  ''oral'', ''black_box_warning'', ''l6'', ''acd_logp'', ''tissue_id'', ''cell_source_tissue'',
  ''usan_stem'', ''pubmed_id'', ''cx_logp'', ''metabolite_record_id'', ''assay_id'',
  ''hbd'', ''activity_id'', ''mechanism_comment'', ''patent_use_code'', ''end_position'',
  ''pref_name'', ''assay_param_id'', ''assay_cell_type'', ''src_compound_id'', ''type'',
  ''efo_term'', ''delist_flag'', ''max_phase'', ''description'', ''mesh_heading'',
  ''formulation_id'', ''doi'', ''ap_id'', ''protclasssyn_id'', ''component_type'',
  ''stat'', ''atc_code'', ''assay_tax_id'', ''withdrawn_year'', ''standard_flag'',
  ''standard_text_value'', ''publication_number'', ''src_description'', ''warning_country'',
  ''mc_tax_id'', ''ro3_pass'', ''caloha_id'', ''cx_most_apka'', ''met_conversion'',
  ''aromatic_rings'']'
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