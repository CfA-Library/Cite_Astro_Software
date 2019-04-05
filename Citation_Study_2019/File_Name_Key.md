## File name key

### Directory structure of Citation_Study_2019
+ API_SEARCH/ = ADS API Search for software aliases
+ XML_Search/ = XML Scraping for sofware aliases
+ READ_ME.md

### XML_SEARCH/
+ XML_PARSER.py = Script used to query the AAS XML files
+ XML_ALIAS_LIST.txt = List of software aliases searched for using the XML_PARSER.py script
+ XML_ANALYSIS/ = Contains scripts used to analyze results of XML scraping

#### XML_SEARCH/XML_ANALYSIS/
+ XML_FINAL_ANALYSIS_040419.ipynb = scripts used to analyze XML search results
* XML_CLEAN_INPUT_032519.csv - File resulting from XML_PARSER.py and cleaned by Daniel; imported into XML_FINAL_ANALYSIS_040419.ipynb
* XML_FINAL_ANALYSIS_040419.csv - File used throughout XML_FINAL_ANALYSIS_040419.ipynb
+ XML_RESULTS/ = Contains results of analysis completed 04-04-19

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
* XML_fn_aliases_040419.csv - All aliases used in footnotes for all software packages 
* XML_over_time_040419.csv - Number of files containing aliases for all software packages by year
* XML_ref_aliases_040419.csv - All aliases used in references for all software packages 

### API_SEARCH/
+ ADS_API_SEARCH_QUERY.py = Script used to query the ADS API
+ API_ALIAS_LIST.txt = List of software aliases searched for using the ADS API
+ API_ANALYSIS/ = Contains scripts used to analyze results of API query

### API_SEARCH/API_ANALYSIS/
+ API_ANALYSIS_031919.py = draft analysis scritpts by Daniel
+ API_CLEAN_INPUT_040519.csv = File resulting from ADS_API_SEARCH_QUERY.py and cleaned by Daniel; imported into API_FINAL_ANALYSIS_040519.ipynb
+ API_FINAL_ANALYSIS_040519.ipynb = scripts used to analyze API search results
+ API_FINAL_ANALYSIS_040519.csv = File used throughout API_FINAL_ANALYSIS_040519.ipynb
+ API_RESULTS/ = Contains results of analysis completed 04-05-19


#### API_ANALYSIS/API_RESULTS/ = Contains cleaned up API search results completed 03-25-19
+ API_cite_aliases_040519.csv = All aliases associated with citations for all software packages
+ API_over_time_040519.csv = Number of articles containing aliases for all software packages by year

