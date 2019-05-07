## File name key

### Directory structure of Citation_Study_2019
+ API_SEARCH/ = ADS API Search for software aliases
+ XML_Search/ = XML Scraping for sofware aliases
+ READ_ME.md

### XML_SEARCH/
+ XML_PARSER.py = Script used to query the AAS XML files
+ XML_ALIAS_LIST.txt = List of software aliases searched for using the XML_PARSER.py script
+ XML_ANALYSIS/ = Contains scripts used to analyze results of XML scraping

### XML_SEARCH/XML_ANALYSIS/
+ XML_FINAL_ANALYSIS_040419.ipynb = scripts used to analyze XML search results
* XML_CLEAN_INPUT_032519.csv - File resulting from XML_PARSER.py and cleaned by Daniel; imported into XML_FINAL_ANALYSIS_040419.ipynb
* XML_FINAL_ANALYSIS_040419.csv - File used throughout XML_FINAL_ANALYSIS_040419.ipynb
+ XML_RESULTS/ = Contains results of analysis completed 04-04-19

### XML_ANALYSIS/XML_RESULTS/
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




## XML INPUT/RESULTS COLUMN EXPLANATIONS



| Column  | Explanation |
| ------------- | ------------- |
| Alias  | Alias list (See: [XML_ALIAS_LIST.txt](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/XML_SEARCH/XML_ALIAS_LIST.txt))  |
| Software_Package  | Name of software package  |
| Identifier  | 1 = alias is identifier. 0 = alias is not identifier.  |
| Pub_Year  | Year of publication ("pub-date" in XML)  |
| DOI  | Digital object identifier  |
| Journal_Title  | Canonical name of the publication the record appeared in ("journal-title" in XML)  |
| Article_ID  | Identifiers associated with the paper ("article-id" in XML)  |
| File_Name  | Name of XML file alias appeared in  |
| Parent1_Tag  |  Layer 1 of XML Tags surrounding alias (See: [NISO JATS Tag Library](https://jats.nlm.nih.gov/publishing/tag-library/1.2/index.html)) |
| Parent2_Tag  |  Layer 2 of XML Tags surrounding alias (See: [NISO JATS Tag Library](https://jats.nlm.nih.gov/publishing/tag-library/1.2/index.html))|
| Parent3_Tag  |  Layer 3 of XML Tags surrounding alias (See: [NISO JATS Tag Library](https://jats.nlm.nih.gov/publishing/tag-library/1.2/index.html))|
| Parent4_Tag  |  Layer 4 of XML Tags surrounding alias (See: [NISO JATS Tag Library](https://jats.nlm.nih.gov/publishing/tag-library/1.2/index.html))|
| Parent1_Content  |  ≥10000 characters between Layer 1 XML Tags (See: [XML_PARSER.py](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/XML_SEARCH/XML_PARSER.py)) |
| Parent2_Content  |  ≥10000 characters between Layer 2 XML Tags (See: [XML_PARSER.py](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/XML_SEARCH/XML_PARSER.py)) |
| Parent3_Content  |  ≥10000 characters between Layer 3 XML Tags (See: [XML_PARSER.py](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/XML_SEARCH/XML_PARSER.py)) |
| Parent4_Content  |  ≥10000 characters between Layer 4 XML Tags (See: [XML_PARSER.py](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/XML_SEARCH/XML_PARSER.py)) |
| Title  | Title of the record ("article-title" in XML) |
| Author(s)  | List of authors on a paper ("name" in XML)  |
| Publisher  | Publisher of the record ("publisher-name" in XML)  |
| Citation  | TRUE = In-text citation used. FALSE = In-text citation not used. |



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


### API_ANALYSIS/API_RESULTS/ = Contains cleaned up API search results completed 03-25-19
+ API_cite_aliases_040519.csv = All aliases associated with citations for all software packages
+ API_over_time_040519.csv = Number of articles containing aliases for all software packages by year




## API INPUT/RESULTS COLUMN EXPLANATIONS
Refer to [Comprehensive List of Solr Fields & Operators](http://adsabs.github.io/help/search/comprehensive-solr-term-list) for the complete list of methods of querying the ADS system.


| Column  | Explanation |
| ------------- | ------------- |
| Alias  | Alias list (See: [API_ALIAS_LIST.txt](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/API_SEARCH/API_ALIAS_LIST.txt))  |
| Software_Package  | Name of software package  |
| Identifier  | 1 = alias is identifier. 0 = alias is not identifier.  |
| Highlight  | ≥150000 character snippet around alias. (See: [ADS_API_SEARCH_QUERY.py](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/Citation_Study_2019/API_SEARCH/ADS_API_SEARCH_QUERY.py))  |
| Citation  | TRUE = In-text citation used. FALSE = In-text citation not used. |
| Bibcode  | ADS identifier of a paper  |
| Alternate_Bibcode  | List of alternate bibcodes for that document  |
| BibGroup  | Bibliographic group that the bibcode belongs to (curated by staff outside of ADS)  |
| Publisher  | Canonical name of the publication the record appeared in  |
| Article_ID  | Abstract field used to search an array of alternative identifiers for the record. May contain alternative bibcodes, DOIs and/or arxiv ids.  |
| DOI  | Digital object identifier  |
| Pub_Year  | Year of publication  |
| Author  | List of authors on a paper  |
| Title  | Title of the record  |
