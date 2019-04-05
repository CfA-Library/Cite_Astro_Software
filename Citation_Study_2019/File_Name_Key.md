## File Name Key

### Directory structure of Citation_Study_2019
+ ADS API Search = API_SEARCH/
+ XML Scraping = XML_Search/
+ READ_ME.md

### API_SEARCH/
Contains the following:
+ ADS_API_SEARCH_QUERY.py = Script used to query the ADS API
+ API_ALIAS_LIST.txt = List of software aliases searched for using the ADS API
+ API_ANALYSIS/ = contains scripts used to analyse results of API query
+ API_ANALYSIS/API_RESULTS/ = contains cleaned up API search results completed 03-25-19

### XML_SEARCH/
Contains the following:
+ XML_PARSER.py = Script used to query the AAS XML files
+ XML_ALIAS_LIST.txt = List of software aliases searched for using the XML_PARSER.py script
+ XML_ANALYSIS/ = contains scripts used to analyse results of XML scraping
+ XML_ANALYSIS/XML_RESULTS/ = contains final cleaned up XML results completed 03-25-19; also contains results of analysis completed 04-04-19

#### XML_ANALYSIS/XML_RESULTS/
* AstroBlend_Tags_040419.csv - All unique XML tags for AstroBlend found in AAS XML 
* AstroPy_Tags_040419.csv - All unique XML tags for AstroPy found in AAS XML 
* RADMC3D_Tags_040419.csv - All unique XML tags for RADMC3D found in AAS XML 
* SAOImageDS9_Tags_040419.csv - All unique XML tags for SAOImageDS9 found in AAS XML 
* Spec2d_Tags_040419.csv - All unique XML tags for Spec2d found in AAS XML 
* Stingray_Tags_040419.csv - All unique XML tags for Stingray found in AAS XML 
* TARDIS_Tags_040419.csv - All unique XML tags for TARDIS found in AAS XML 
* WCSTools_Tags_040419.csv - All unique XML tags for WCSTools found in AAS XML 
* XML_ack_aliases_040419.csv - All aliases used in acknowledgements for all software packages 
* XML_all_tags_040419.csv - All unique XML tags for all software packages 
* XML_CLEAN_RESULTS_032519.csv - File resulting from XML_PARSER.py and cleaned by Daniel; imported into XML_RESULTS/XML_FINAL_ANALYSIS_040419.ipynb
* XML_fn_aliases_040419.csv - All aliases used in footnotes for all software packages 
* XML_over_time_040419.csv - Number of files containing aliases for all software packages by year
* XML_ref_aliases_040419.csv - All aliases used in references for all software packages 
* XML_RESULTS_FINAL_040419.csv - File used throughout XML_RESULTS/XML_FINAL_ANALYSIS_040419.ipynb