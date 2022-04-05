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
schema_fields: '[''ass_cls_map_id'', ''enzyme_tid'', ''aromatic_rings'', ''applicant_full_name'',
  ''num_lipinski_ro5_violations'', ''assay_id'', ''go_id'', ''relation'', ''activity_id'',
  ''cx_logp'', ''enzyme_name'', ''acd_most_bpka'', ''synonyms'', ''level3_description'',
  ''publication_number'', ''warning_class'', ''indication_class'', ''warning_description'',
  ''src_description'', ''source_domain_id'', ''mc_tax_id'', ''targrel_id'', ''level1_description'',
  ''relationship_type'', ''rtb'', ''last_page'', ''irac_code'', ''max_phase_for_ind'',
  ''company'', ''trade_name'', ''hba'', ''confidence'', ''binding_site_comment'',
  ''acd_logp'', ''definition'', ''mol_atc_id'', ''hbd_lipinski'', ''abstract'', ''alert_name'',
  ''patent_use_code'', ''src_short_name'', ''variant_id'', ''hrac_class_id'', ''published_relation'',
  ''entity_type'', ''ap_id'', ''availability_type'', ''molsyn_id'', ''innovator_company'',
  ''entity_id'', ''num_alerts'', ''molecular_mechanism'', ''record_id'', ''withdrawn_class'',
  ''cellosaurus_id'', ''assay_test_type'', ''src_id'', ''standard_inchi_key'', ''active_ingredient'',
  ''idx'', ''compound_key'', ''therapeutic_flag'', ''tbl'', ''updated_on'', ''nda_type'',
  ''ddd_id'', ''source'', ''path'', ''approval_date'', ''l1'', ''cx_most_apka'', ''drugind_id'',
  ''frac_class_id'', ''smarts'', ''homologue'', ''comp_class_id'', ''tissue_id'',
  ''bto_id'', ''protclasssyn_id'', ''curation_comment'', ''standard_value'', ''published_units'',
  ''l7'', ''met_comment'', ''cell_ontology_id'', ''mc_target_type'', ''disease_efficacy'',
  ''cpd_str_alert_id'', ''comp_go_id'', ''target_mapping'', ''ddd_admr'', ''component_type'',
  ''relationship'', ''target_desc'', ''warning_type'', ''standard_type'', ''published_value'',
  ''ddd_value'', ''chembl_id'', ''mol_frac_id'', ''mc_organism'', ''num_ro5_violations'',
  ''volume'', ''formulation_id'', ''set_name'', ''mutation'', ''domain_type'', ''cl_lincs_id'',
  ''drug_product_flag'', ''component_id'', ''activity_comment'', ''submission_date'',
  ''substrate_record_id'', ''class_level'', ''potential_duplicate'', ''alert_set_id'',
  ''molecular_species'', ''who_name'', ''research_stem'', ''cell_description'', ''src_compound_id'',
  ''comments'', ''year'', ''molecule_type'', ''type'', ''parameter_value'', ''res_stem_id'',
  ''predbind_id'', ''warning_year'', ''irac_class_id'', ''label'', ''cell_id'', ''std_act_id'',
  ''mesh_id'', ''protein_class_desc'', ''db_source'', ''site_name'', ''canonical_smiles'',
  ''inorganic_flag'', ''oral'', ''start_position'', ''assay_subcellular_fraction'',
  ''product_id'', ''met_conversion'', ''l2'', ''assay_tissue'', ''journal'', ''mechanism_of_action'',
  ''hbd'', ''l6'', ''withdrawn_country'', ''molfile'', ''annotation'', ''parenteral'',
  ''title'', ''upper_value'', ''sitecomp_id'', ''stem_class'', ''major_class'', ''data_validity_comment'',
  ''published_type'', ''met_id'', ''patent_expire_date'', ''ad_type'', ''alert_id'',
  ''molregno'', ''level2'', ''mec_id'', ''src_assay_id'', ''ingredient'', ''curated_by'',
  ''structure_type'', ''direct_interaction'', ''usan_stem'', ''targcomp_id'', ''usan_substem'',
  ''protein_class_synonym'', ''cell_source_tax_id'', ''hrac_code'', ''mechanism_comment'',
  ''mw_monoisotopic'', ''rgid'', ''site_id'', ''max_phase'', ''selectivity_comment'',
  ''first_approval'', ''normal_range_min'', ''accession'', ''assay_strain'', ''version'',
  ''metabolite_record_id'', ''cell_source_organism'', ''sequence_md5sum'', ''cell_name'',
  ''drug_record_id'', ''standard_units'', ''tax_id'', ''qed_weighted'', ''stat'',
  ''organism'', ''usan_stem_definition'', ''withdrawn_flag'', ''delist_flag'', ''parent_go_id'',
  ''standard_upper_value'', ''toid'', ''mc_target_accession'', ''ref_url'', ''caloha_id'',
  ''doc_id'', ''isoform'', ''oc_id'', ''natural_product'', ''ridx'', ''status'', ''l8'',
  ''priority'', ''prediction_method'', ''component_synonym'', ''description'', ''withdrawn_year'',
  ''prodrug'', ''indref_id'', ''tid'', ''l5'', ''log_id'', ''ref_id'', ''drug_substance_flag'',
  ''value'', ''helm_notation'', ''doi'', ''mol_irac_id'', ''topical'', ''parameter_type'',
  ''level2_description'', ''assay_source'', ''text_value'', ''alogp'', ''ddd_units'',
  ''active_molregno'', ''patent_id'', ''sei'', ''standard_inchi'', ''domain_name'',
  ''domain_id'', ''as_id'', ''strength'', ''cidx'', ''heavy_atoms'', ''smid'', ''mecref_id'',
  ''relationship_desc'', ''stem'', ''assay_type'', ''country'', ''syn_type'', ''warning_id'',
  ''activity_count'', ''pathway_key'', ''previous_company'', ''efo_id'', ''name'',
  ''job_id'', ''patent_no'', ''dosed_ingredient'', ''orig_description'', ''bao_id'',
  ''units'', ''warnref_id'', ''downgraded'', ''compound_name'', ''acd_most_apka'',
  ''aspect'', ''uberon_id'', ''level4'', ''ddd_comment'', ''l4'', ''level5'', ''black_box_warning'',
  ''class_type'', ''cx_logd'', ''assay_desc'', ''chirality'', ''first_page'', ''uo_units'',
  ''pubmed_id'', ''acd_logd'', ''pchembl_value'', ''metref_id'', ''assay_cell_type'',
  ''full_molformula'', ''route'', ''tid_fixed'', ''authors'', ''cx_most_bpka'', ''level3'',
  ''polymer_flag'', ''usan_stem_id'', ''frac_code'', ''creation_date'', ''subgroup'',
  ''assay_class_id'', ''protein_class_id'', ''parent_molregno'', ''ref_type'', ''assay_category'',
  ''confidence_score'', ''warning_country'', ''actsm_id'', ''atc_code'', ''bao_format'',
  ''ro3_pass'', ''hba_lipinski'', ''end_position'', ''dosage_form'', ''mol_hrac_id'',
  ''related_tid'', ''pref_name'', ''db_version'', ''action_type'', ''usan_year'',
  ''pathway_id'', ''l3'', ''standard_text_value'', ''site_residues'', ''parent_type'',
  ''first_in_class'', ''mc_target_name'', ''cell_source_tissue'', ''mw_freebase'',
  ''who_extra'', ''clo_id'', ''result_flag'', ''psa'', ''short_name'', ''lle'', ''level1'',
  ''prod_pat_id'', ''full_mwt'', ''species_group_flag'', ''biocomp_id'', ''normal_range_max'',
  ''mesh_heading'', ''compd_id'', ''parent_id'', ''le'', ''doc_type'', ''standard_flag'',
  ''level4_description'', ''efo_term'', ''standard_relation'', ''assay_organism'',
  ''bei'', ''last_active'', ''sequence'', ''domain_description'', ''assay_param_id'',
  ''aidx'', ''chebi_par_id'', ''bao_endpoint'', ''target_type'', ''co_stem_id'', ''issue'',
  ''assay_tax_id'', ''updated_by'', ''compsyn_id'', ''qudt_units'', ''withdrawn_reason'']'
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