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
schema_fields: '[''chembl_id'', ''molecule_type'', ''class_type'', ''metref_id'',
  ''doi'', ''annotation'', ''hba'', ''comp_go_id'', ''ad_type'', ''log_id'', ''molsyn_id'',
  ''num_ro5_violations'', ''ddd_comment'', ''full_mwt'', ''l4'', ''organism'', ''pref_name'',
  ''standard_upper_value'', ''tissue_id'', ''component_type'', ''drugind_id'', ''label'',
  ''orig_description'', ''availability_type'', ''potential_duplicate'', ''target_type'',
  ''molecular_mechanism'', ''publication_number'', ''qudt_units'', ''active_ingredient'',
  ''published_units'', ''warnref_id'', ''withdrawn_reason'', ''innovator_company'',
  ''assay_category'', ''pathway_key'', ''black_box_warning'', ''std_act_id'', ''domain_description'',
  ''drug_record_id'', ''component_id'', ''withdrawn_year'', ''active_molregno'', ''ref_id'',
  ''protclasssyn_id'', ''year'', ''doc_type'', ''normal_range_min'', ''confidence_score'',
  ''sei'', ''assay_class_id'', ''ddd_admr'', ''assay_test_type'', ''comp_class_id'',
  ''withdrawn_class'', ''normal_range_max'', ''efo_id'', ''stat'', ''rgid'', ''mc_target_accession'',
  ''volume'', ''tax_id'', ''warning_class'', ''mutation'', ''company'', ''published_value'',
  ''first_in_class'', ''last_page'', ''mechanism_comment'', ''description'', ''level2_description'',
  ''bao_id'', ''name'', ''oral'', ''bao_format'', ''db_source'', ''enzyme_name'',
  ''protein_class_synonym'', ''trade_name'', ''hrac_class_id'', ''met_conversion'',
  ''alert_set_id'', ''standard_inchi'', ''mecref_id'', ''homologue'', ''major_class'',
  ''acd_logd'', ''action_type'', ''psa'', ''priority'', ''tbl'', ''level4'', ''patent_use_code'',
  ''warning_country'', ''confidence'', ''data_validity_comment'', ''molregno'', ''ass_cls_map_id'',
  ''upper_value'', ''clo_id'', ''target_mapping'', ''ref_url'', ''usan_stem_definition'',
  ''indref_id'', ''src_assay_id'', ''go_id'', ''ddd_id'', ''class_level'', ''mec_id'',
  ''country'', ''mol_irac_id'', ''atc_code'', ''pathway_id'', ''acd_most_apka'', ''parent_type'',
  ''variant_id'', ''binding_site_comment'', ''relationship'', ''submission_date'',
  ''who_extra'', ''first_page'', ''route'', ''met_comment'', ''cl_lincs_id'', ''assay_tax_id'',
  ''target_desc'', ''cell_id'', ''cpd_str_alert_id'', ''standard_type'', ''db_version'',
  ''aromatic_rings'', ''accession'', ''nda_type'', ''result_flag'', ''level5'', ''job_id'',
  ''ddd_units'', ''usan_stem_id'', ''substrate_record_id'', ''parameter_type'', ''domain_id'',
  ''mol_atc_id'', ''assay_source'', ''warning_year'', ''dosed_ingredient'', ''assay_desc'',
  ''value'', ''disease_efficacy'', ''type'', ''level3_description'', ''activity_id'',
  ''parent_id'', ''smarts'', ''max_phase'', ''product_id'', ''num_lipinski_ro5_violations'',
  ''level1_description'', ''src_id'', ''cell_source_tax_id'', ''structure_type'',
  ''full_molformula'', ''bei'', ''usan_stem'', ''path'', ''source_domain_id'', ''curation_comment'',
  ''cell_name'', ''inorganic_flag'', ''related_tid'', ''idx'', ''withdrawn_flag'',
  ''updated_on'', ''lle'', ''synonyms'', ''mc_target_name'', ''site_id'', ''last_active'',
  ''alogp'', ''relation'', ''as_id'', ''l2'', ''standard_value'', ''enzyme_tid'',
  ''actsm_id'', ''l3'', ''usan_substem'', ''stem'', ''res_stem_id'', ''l5'', ''cx_logp'',
  ''prod_pat_id'', ''mc_target_type'', ''mc_tax_id'', ''src_short_name'', ''component_synonym'',
  ''le'', ''ddd_value'', ''frac_code'', ''curated_by'', ''tid_fixed'', ''l6'', ''site_name'',
  ''targcomp_id'', ''assay_type'', ''cell_source_organism'', ''previous_company'',
  ''parent_molregno'', ''met_id'', ''source'', ''published_type'', ''level2'', ''creation_date'',
  ''standard_flag'', ''standard_inchi_key'', ''patent_id'', ''efo_term'', ''mol_frac_id'',
  ''cidx'', ''molfile'', ''caloha_id'', ''sequence'', ''warning_type'', ''assay_param_id'',
  ''acd_most_bpka'', ''sitecomp_id'', ''end_position'', ''delist_flag'', ''relationship_type'',
  ''drug_product_flag'', ''ridx'', ''doc_id'', ''tid'', ''who_name'', ''standard_text_value'',
  ''approval_date'', ''relationship_desc'', ''published_relation'', ''comments'',
  ''chebi_par_id'', ''protein_class_desc'', ''compsyn_id'', ''uo_units'', ''targrel_id'',
  ''src_description'', ''alert_id'', ''record_id'', ''prodrug'', ''warning_description'',
  ''metabolite_record_id'', ''updated_by'', ''formulation_id'', ''cx_most_bpka'',
  ''level3'', ''cx_most_apka'', ''frac_class_id'', ''assay_tissue'', ''parameter_value'',
  ''cellosaurus_id'', ''ap_id'', ''applicant_full_name'', ''title'', ''compd_id'',
  ''aidx'', ''oc_id'', ''text_value'', ''withdrawn_country'', ''compound_name'', ''bto_id'',
  ''l1'', ''hbd'', ''aspect'', ''entity_id'', ''smid'', ''acd_logp'', ''uberon_id'',
  ''patent_expire_date'', ''research_stem'', ''assay_id'', ''natural_product'', ''site_residues'',
  ''bao_endpoint'', ''irac_class_id'', ''standard_relation'', ''polymer_flag'', ''abstract'',
  ''sequence_md5sum'', ''mesh_heading'', ''num_alerts'', ''patent_no'', ''dosage_form'',
  ''mesh_id'', ''ingredient'', ''downgraded'', ''authors'', ''activity_comment'',
  ''heavy_atoms'', ''biocomp_id'', ''assay_organism'', ''assay_strain'', ''activity_count'',
  ''mw_freebase'', ''definition'', ''cx_logd'', ''version'', ''syn_type'', ''alert_name'',
  ''start_position'', ''therapeutic_flag'', ''src_compound_id'', ''assay_cell_type'',
  ''cell_description'', ''topical'', ''set_name'', ''selectivity_comment'', ''assay_subcellular_fraction'',
  ''co_stem_id'', ''ro3_pass'', ''entity_type'', ''species_group_flag'', ''level4_description'',
  ''hba_lipinski'', ''mol_hrac_id'', ''strength'', ''mc_organism'', ''usan_year'',
  ''prediction_method'', ''cell_source_tissue'', ''standard_units'', ''mechanism_of_action'',
  ''short_name'', ''helm_notation'', ''protein_class_id'', ''canonical_smiles'', ''direct_interaction'',
  ''mw_monoisotopic'', ''parent_go_id'', ''subgroup'', ''cell_ontology_id'', ''max_phase_for_ind'',
  ''level1'', ''predbind_id'', ''status'', ''isoform'', ''rtb'', ''compound_key'',
  ''domain_type'', ''chirality'', ''stem_class'', ''first_approval'', ''domain_name'',
  ''warning_id'', ''units'', ''hbd_lipinski'', ''l7'', ''qed_weighted'', ''indication_class'',
  ''l8'', ''journal'', ''pubmed_id'', ''molecular_species'', ''irac_code'', ''ref_type'',
  ''parenteral'', ''toid'', ''pchembl_value'', ''drug_substance_flag'', ''issue'',
  ''hrac_code'']'
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