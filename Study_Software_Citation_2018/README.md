### A Twenty Year Case Study on Software Citation Practices in Astronomy 

This folder contains files relevant to an on-going case study examining software citation practices in Astronomy. 

Methods:

CfA Library staff identified eleven software packages developed in whole or in part at the CfA. The packages selected represent codes with varying degrees of complexity and would be expected to be cited across different timeframes within a 20 year period.

Software packages included in the study:
1. [AstroBlend](http://www.astroblend.com/)
2. [AstroPy](http://www.astropy.org/)
3. [BEANS](https://beanscode.net/)
4. [DS9](http://ds9.si.edu/site/Home.html)
5. [ytini](http://ytini.com/index.html)
6. [PlasmaPy](http://www.plasmapy.org/)
7. [RADMC-3D](http://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/)
8. [spec2d](http://deep.ps.uci.edu/spec2d/0
9. [Tardis](https://tardis.readthedocs.io/en/latest/)
10. [WCSTools](http://tdc-www.harvard.edu/software/wcstools/)
11. [Stingray](https://stingraysoftware.github.io/)

* Library staff gathered "aliases" for the selected software packages through interviews and online searches to develop a list of search terms that could be used to refer to the software packages in article texts. Staff also added identifiers and links associated with each package to the search terms list; associated identifiers and links include those tied to ADS bibcodes, Zenodo records, ASCL records, arXiv preprints, and URLs to many different types of websites. 
  * Final edits are being made to the list of aliases: spreadsheet containing current alias list is [here](https://docs.google.com/spreadsheets/d/1DrGeb3XiVzMesHPJ9bfW_d7nkR7JqxqRvpQNNQdTKKM/edit#gid=1696232166) (working document). 
-------
Phase 1: AAS XML search

The final aliases will be used to search XML files representing 20 years of articles published in AAS Journals
  * If any of the software aliases are found in a given XML file (AAS article):
     * We identify where the alias is showing up in the article (e.g. references section, in text, in a table, etc.)
     * We count the number of unique aliases used to identify the software in the article
       * AstroBlend, 10.1016/j.ascom.2016.02.002, ascl:1512.007 all showing up in one XML file would be 3 total search terms
   * If the software package alias appears in the references section:
      * We identify which aliases were found in the references section (e.g. DOI, URL of some kind, bibcode to a paper, etc.)

After searching across all XML for all software, we will aggregate
  * For each software package:
    * Total number of articles identified as containing an alias
    * Total number of unique aliases representing the software package across the entire corpus of articles over time 
      * represents all of the ways article authors have mentioned the software
    * Total number of unique locations where the software aliases were found across the entire corpus of articles (e.g. paragraphs, abstracts, references)
      * represents all of the contexts in which article authors are mentioning the software
    * Maximum number of unique aliases representing the software package in a given article 
      * represents degree of variability within articles
    * Total number of aliases found in References sections of articles
      * represents attempt by the article authors to cite the software package
      * articles containing search terms found in references vs. all articles containing search terms
        * represents how often article authors acnowledge software in writing but do not list it in references
    * Total number of software aliases found in References sections of articles where a DOI was cited
      * represents citation to a paper or a Zenodo record
    * Total number of software aliases found in References sections of articles where a Zenodo DOI was cited
      * represents citation to archived code (in theory)
        * in practice we see examples where the Zenodo software record is actually a paper ([10.5281/zenodo.1211397)](https://doi.org/10.5281/zenodo.1211397) or the software authors have given a preferred citation ([10.5281/zenodo.163752
](https://doi.org/10.5281/zenodo.163752)) that is a Zenodo record containing a presentation ([10.5281/zenodo.1238132](https://doi.org/10.5281/zenodo.1238132)) rather than code even when there is a Zenodo record for the code ([10.5281/zenodo.1436012](https://doi.org/10.5281/zenodo.1436012)).

These aggregates will help demonstrate how article authors have included software in their papers and the degree to which those practices diverge from the practices that enable ADS and other to identify software citations.

----------
Phase 1: ADS API search

After searching with the above degree of granularity through the AAS XML, Library staff will query the ADS API for the same software aliases. 

The degree to which the results from the ADS API search and the direct XML search match for AAS publications for the same period of time will indicate the accuracy of the ADS API full text search as it pertains to a search for these software aliases in non-AAS publications (i.e. proportion of matching bibcodes).

For each software package we will find the total number of articles identified across all publications indexed by ADS that contain software aliases. We will compare those totals to the total number of articles that ADS would identify as containing software citations.
