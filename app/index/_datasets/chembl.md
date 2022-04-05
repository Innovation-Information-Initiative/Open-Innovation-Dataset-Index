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
schema_fields: '[''targcomp_id'', ''target_type'', ''type'', ''component_type'', ''src_assay_id'',
  ''rtb'', ''route'', ''bao_id'', ''withdrawn_flag'', ''cell_description'', ''l1'',
  ''stem_class'', ''pref_name'', ''assay_cell_type'', ''sequence'', ''max_phase'',
  ''actsm_id'', ''cellosaurus_id'', ''authors'', ''uberon_id'', ''alert_name'', ''synonyms'',
  ''enzyme_tid'', ''tbl'', ''metref_id'', ''heavy_atoms'', ''biocomp_id'', ''cx_logp'',
  ''molfile'', ''species_group_flag'', ''efo_id'', ''assay_test_type'', ''trade_name'',
  ''journal'', ''abstract'', ''ref_id'', ''le'', ''warning_type'', ''ass_cls_map_id'',
  ''sei'', ''subgroup'', ''job_id'', ''mw_monoisotopic'', ''num_alerts'', ''lle'',
  ''curation_comment'', ''end_position'', ''tissue_id'', ''site_residues'', ''syn_type'',
  ''assay_desc'', ''protein_class_id'', ''usan_stem_definition'', ''drugind_id'',
  ''who_name'', ''db_version'', ''withdrawn_country'', ''frac_class_id'', ''uo_units'',
  ''normal_range_min'', ''mol_irac_id'', ''met_conversion'', ''assay_param_id'', ''std_act_id'',
  ''variant_id'', ''num_lipinski_ro5_violations'', ''usan_substem'', ''drug_substance_flag'',
  ''withdrawn_class'', ''withdrawn_reason'', ''homologue'', ''level3_description'',
  ''bao_endpoint'', ''compound_key'', ''text_value'', ''aidx'', ''standard_units'',
  ''qed_weighted'', ''year'', ''approval_date'', ''accession'', ''protclasssyn_id'',
  ''normal_range_max'', ''tax_id'', ''mechanism_comment'', ''res_stem_id'', ''alogp'',
  ''name'', ''first_in_class'', ''standard_upper_value'', ''mc_organism'', ''cidx'',
  ''irac_code'', ''short_name'', ''cx_most_bpka'', ''updated_by'', ''ingredient'',
  ''level2'', ''source'', ''site_id'', ''volume'', ''met_id'', ''l8'', ''inorganic_flag'',
  ''toid'', ''l6'', ''relation'', ''alert_set_id'', ''ap_id'', ''set_name'', ''dosed_ingredient'',
  ''cl_lincs_id'', ''mc_target_accession'', ''formulation_id'', ''go_id'', ''irac_class_id'',
  ''chirality'', ''cell_name'', ''sitecomp_id'', ''entity_id'', ''result_flag'', ''atc_code'',
  ''db_source'', ''assay_subcellular_fraction'', ''predbind_id'', ''published_units'',
  ''black_box_warning'', ''standard_text_value'', ''country'', ''site_name'', ''pathway_key'',
  ''mesh_heading'', ''as_id'', ''published_type'', ''metabolite_record_id'', ''data_validity_comment'',
  ''level1'', ''action_type'', ''domain_description'', ''relationship_desc'', ''src_description'',
  ''submission_date'', ''patent_id'', ''oc_id'', ''comp_class_id'', ''patent_expire_date'',
  ''cx_logd'', ''downgraded'', ''mutation'', ''product_id'', ''component_id'', ''cpd_str_alert_id'',
  ''selectivity_comment'', ''qudt_units'', ''publication_number'', ''smid'', ''compound_name'',
  ''bto_id'', ''mec_id'', ''standard_flag'', ''innovator_company'', ''level3'', ''research_stem'',
  ''entity_type'', ''topical'', ''l4'', ''related_tid'', ''definition'', ''record_id'',
  ''prediction_method'', ''path'', ''isoform'', ''active_molregno'', ''relationship_type'',
  ''l7'', ''aspect'', ''full_molformula'', ''mw_freebase'', ''disease_efficacy'',
  ''level5'', ''patent_no'', ''previous_company'', ''active_ingredient'', ''molsyn_id'',
  ''ddd_value'', ''protein_class_synonym'', ''efo_term'', ''cx_most_apka'', ''hrac_code'',
  ''ad_type'', ''hbd'', ''assay_strain'', ''natural_product'', ''title'', ''priority'',
  ''hba'', ''sequence_md5sum'', ''cell_ontology_id'', ''parameter_value'', ''tid'',
  ''assay_id'', ''organism'', ''protein_class_desc'', ''frac_code'', ''doc_type'',
  ''label'', ''description'', ''polymer_flag'', ''relationship'', ''prod_pat_id'',
  ''met_comment'', ''prodrug'', ''company'', ''bei'', ''warnref_id'', ''usan_stem_id'',
  ''molregno'', ''molecular_mechanism'', ''mol_frac_id'', ''mc_target_type'', ''pchembl_value'',
  ''pubmed_id'', ''target_desc'', ''max_phase_for_ind'', ''availability_type'', ''parent_type'',
  ''molecular_species'', ''mechanism_of_action'', ''updated_on'', ''parent_molregno'',
  ''pathway_id'', ''ddd_units'', ''warning_class'', ''warning_year'', ''mol_atc_id'',
  ''doi'', ''domain_type'', ''warning_description'', ''canonical_smiles'', ''last_active'',
  ''chembl_id'', ''nda_type'', ''binding_site_comment'', ''acd_logd'', ''level1_description'',
  ''ref_type'', ''compd_id'', ''delist_flag'', ''comp_go_id'', ''mesh_id'', ''units'',
  ''assay_class_id'', ''acd_logp'', ''value'', ''src_short_name'', ''parameter_type'',
  ''parent_id'', ''start_position'', ''class_type'', ''src_compound_id'', ''assay_type'',
  ''full_mwt'', ''usan_stem'', ''ref_url'', ''cell_source_tissue'', ''cell_source_organism'',
  ''tid_fixed'', ''dosage_form'', ''acd_most_apka'', ''src_id'', ''level4'', ''level4_description'',
  ''alert_id'', ''caloha_id'', ''ridx'', ''l5'', ''domain_id'', ''mecref_id'', ''mc_tax_id'',
  ''num_ro5_violations'', ''last_page'', ''compsyn_id'', ''parent_go_id'', ''patent_use_code'',
  ''activity_comment'', ''enzyme_name'', ''upper_value'', ''confidence_score'', ''class_level'',
  ''indication_class'', ''hba_lipinski'', ''assay_organism'', ''co_stem_id'', ''molecule_type'',
  ''bao_format'', ''clo_id'', ''activity_count'', ''standard_inchi'', ''standard_type'',
  ''idx'', ''indref_id'', ''strength'', ''hrac_class_id'', ''cell_id'', ''drug_record_id'',
  ''version'', ''ddd_admr'', ''curated_by'', ''substrate_record_id'', ''doc_id'',
  ''published_value'', ''published_relation'', ''source_domain_id'', ''stem'', ''component_synonym'',
  ''level2_description'', ''target_mapping'', ''standard_value'', ''aromatic_rings'',
  ''log_id'', ''ddd_comment'', ''oral'', ''withdrawn_year'', ''l3'', ''targrel_id'',
  ''ddd_id'', ''confidence'', ''therapeutic_flag'', ''assay_tax_id'', ''orig_description'',
  ''rgid'', ''potential_duplicate'', ''mc_target_name'', ''status'', ''assay_tissue'',
  ''cell_source_tax_id'', ''helm_notation'', ''assay_source'', ''domain_name'', ''usan_year'',
  ''direct_interaction'', ''standard_relation'', ''applicant_full_name'', ''acd_most_bpka'',
  ''parenteral'', ''stat'', ''first_approval'', ''hbd_lipinski'', ''smarts'', ''warning_id'',
  ''standard_inchi_key'', ''issue'', ''who_extra'', ''annotation'', ''assay_category'',
  ''structure_type'', ''mol_hrac_id'', ''psa'', ''activity_id'', ''comments'', ''creation_date'',
  ''l2'', ''ro3_pass'', ''major_class'', ''drug_product_flag'', ''chebi_par_id'',
  ''warning_country'', ''first_page'']'
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