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
schema_fields: '[''src_assay_id'', ''prediction_method'', ''irac_code'', ''nda_type'',
  ''tbl'', ''mecref_id'', ''bei'', ''description'', ''irac_class_id'', ''ad_type'',
  ''dosed_ingredient'', ''sei'', ''src_compound_id'', ''smid'', ''issue'', ''class_type'',
  ''compound_key'', ''go_id'', ''clo_id'', ''accession'', ''publication_number'',
  ''patent_id'', ''compd_id'', ''assay_param_id'', ''first_in_class'', ''mc_tax_id'',
  ''syn_type'', ''site_residues'', ''src_id'', ''warning_class'', ''frac_code'', ''class_level'',
  ''cellosaurus_id'', ''type'', ''component_id'', ''drugind_id'', ''doc_id'', ''cx_logd'',
  ''hrac_class_id'', ''met_id'', ''mechanism_comment'', ''assay_tax_id'', ''mw_freebase'',
  ''assay_class_id'', ''ddd_id'', ''end_position'', ''molsyn_id'', ''curation_comment'',
  ''bto_id'', ''warning_country'', ''std_act_id'', ''actsm_id'', ''mechanism_of_action'',
  ''ridx'', ''hba'', ''usan_stem'', ''stem'', ''assay_source'', ''active_molregno'',
  ''innovator_company'', ''assay_subcellular_fraction'', ''metabolite_record_id'',
  ''efo_id'', ''applicant_full_name'', ''site_name'', ''domain_name'', ''tid'', ''helm_notation'',
  ''binding_site_comment'', ''mol_hrac_id'', ''compound_name'', ''warning_year'',
  ''hba_lipinski'', ''level5'', ''ap_id'', ''efo_term'', ''topical'', ''route'', ''job_id'',
  ''pubmed_id'', ''standard_type'', ''predbind_id'', ''aspect'', ''species_group_flag'',
  ''hbd'', ''mc_target_type'', ''toid'', ''frac_class_id'', ''parent_id'', ''parent_type'',
  ''path'', ''parent_molregno'', ''annotation'', ''protein_class_synonym'', ''warning_id'',
  ''mc_target_name'', ''withdrawn_class'', ''level3'', ''patent_use_code'', ''domain_type'',
  ''organism'', ''withdrawn_reason'', ''activity_id'', ''action_type'', ''authors'',
  ''level4_description'', ''idx'', ''usan_year'', ''assay_category'', ''acd_most_bpka'',
  ''assay_test_type'', ''natural_product'', ''chirality'', ''related_tid'', ''site_id'',
  ''who_name'', ''mc_organism'', ''priority'', ''molecular_mechanism'', ''full_mwt'',
  ''activity_count'', ''strength'', ''curated_by'', ''met_conversion'', ''parent_go_id'',
  ''domain_description'', ''units'', ''biocomp_id'', ''pathway_key'', ''structure_type'',
  ''sequence_md5sum'', ''cell_name'', ''tissue_id'', ''uberon_id'', ''withdrawn_year'',
  ''acd_logp'', ''standard_inchi'', ''subgroup'', ''company'', ''indref_id'', ''cell_id'',
  ''co_stem_id'', ''mutation'', ''aidx'', ''volume'', ''start_position'', ''component_type'',
  ''max_phase'', ''delist_flag'', ''year'', ''src_description'', ''enzyme_tid'', ''standard_text_value'',
  ''db_source'', ''title'', ''data_validity_comment'', ''patent_no'', ''entity_type'',
  ''mec_id'', ''alert_id'', ''availability_type'', ''cell_source_organism'', ''black_box_warning'',
  ''mol_frac_id'', ''level1_description'', ''num_alerts'', ''direct_interaction'',
  ''abstract'', ''parameter_type'', ''alogp'', ''drug_product_flag'', ''heavy_atoms'',
  ''orig_description'', ''full_molformula'', ''product_id'', ''parameter_value'',
  ''published_units'', ''cell_ontology_id'', ''standard_units'', ''pchembl_value'',
  ''result_flag'', ''bao_endpoint'', ''definition'', ''usan_stem_id'', ''pathway_id'',
  ''therapeutic_flag'', ''l4'', ''qudt_units'', ''warnref_id'', ''num_lipinski_ro5_violations'',
  ''disease_efficacy'', ''chembl_id'', ''bao_id'', ''psa'', ''ddd_value'', ''ro3_pass'',
  ''usan_stem_definition'', ''le'', ''enzyme_name'', ''targrel_id'', ''oc_id'', ''metref_id'',
  ''cl_lincs_id'', ''indication_class'', ''status'', ''formulation_id'', ''l3'', ''ass_cls_map_id'',
  ''ingredient'', ''ddd_admr'', ''cx_logp'', ''updated_on'', ''comp_go_id'', ''smarts'',
  ''uo_units'', ''sequence'', ''cx_most_apka'', ''cell_source_tissue'', ''polymer_flag'',
  ''who_extra'', ''l2'', ''src_short_name'', ''first_approval'', ''molecule_type'',
  ''inorganic_flag'', ''mw_monoisotopic'', ''level2_description'', ''comments'', ''rgid'',
  ''target_type'', ''assay_type'', ''relationship'', ''tax_id'', ''variant_id'', ''dosage_form'',
  ''set_name'', ''mesh_id'', ''doi'', ''doc_type'', ''pref_name'', ''ddd_comment'',
  ''component_synonym'', ''comp_class_id'', ''version'', ''compsyn_id'', ''mc_target_accession'',
  ''normal_range_max'', ''l1'', ''acd_logd'', ''protein_class_id'', ''active_ingredient'',
  ''selectivity_comment'', ''withdrawn_flag'', ''standard_flag'', ''assay_id'', ''canonical_smiles'',
  ''mesh_heading'', ''major_class'', ''assay_organism'', ''cell_source_tax_id'', ''label'',
  ''assay_strain'', ''substrate_record_id'', ''source'', ''oral'', ''protclasssyn_id'',
  ''log_id'', ''molfile'', ''mol_atc_id'', ''l5'', ''mol_irac_id'', ''standard_relation'',
  ''l7'', ''standard_upper_value'', ''downgraded'', ''cell_description'', ''ref_id'',
  ''bao_format'', ''as_id'', ''l8'', ''activity_comment'', ''submission_date'', ''withdrawn_country'',
  ''prod_pat_id'', ''potential_duplicate'', ''level2'', ''atc_code'', ''usan_substem'',
  ''journal'', ''stat'', ''max_phase_for_ind'', ''source_domain_id'', ''ref_type'',
  ''targcomp_id'', ''standard_inchi_key'', ''confidence'', ''acd_most_apka'', ''hrac_code'',
  ''published_relation'', ''level4'', ''approval_date'', ''ref_url'', ''aromatic_rings'',
  ''upper_value'', ''rtb'', ''normal_range_min'', ''parenteral'', ''met_comment'',
  ''published_type'', ''country'', ''relation'', ''alert_name'', ''confidence_score'',
  ''homologue'', ''target_desc'', ''molregno'', ''assay_tissue'', ''standard_value'',
  ''warning_type'', ''lle'', ''molecular_species'', ''name'', ''chebi_par_id'', ''cpd_str_alert_id'',
  ''target_mapping'', ''previous_company'', ''level1'', ''level3_description'', ''cx_most_bpka'',
  ''qed_weighted'', ''last_page'', ''first_page'', ''res_stem_id'', ''published_value'',
  ''ddd_units'', ''creation_date'', ''db_version'', ''alert_set_id'', ''assay_cell_type'',
  ''text_value'', ''domain_id'', ''patent_expire_date'', ''stem_class'', ''l6'', ''cidx'',
  ''assay_desc'', ''sitecomp_id'', ''tid_fixed'', ''research_stem'', ''caloha_id'',
  ''relationship_type'', ''last_active'', ''warning_description'', ''isoform'', ''protein_class_desc'',
  ''trade_name'', ''drug_substance_flag'', ''entity_id'', ''synonyms'', ''drug_record_id'',
  ''prodrug'', ''record_id'', ''num_ro5_violations'', ''hbd_lipinski'', ''updated_by'',
  ''relationship_desc'', ''value'', ''short_name'']'
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