## A Twenty Year Case Study on Software Citation Practices in Astronomy 
[Daina Bouquin](https://github.com/dbouquin), [Daniel Chivvis](https://github.com/danielchivvis)

This folder contains files relevant to an on-going case study examining software citation practices in Astronomy. 

### Methods:

CfA Library staff identified eleven software packages developed in whole or in part at the CfA. The packages selected represent codes with varying degrees of complexity and would be expected to be cited across different timeframes within a 20 year period.

Software packages included in the study:
1. [AstroBlend](http://www.astroblend.com/)
2. [AstroPy](http://www.astropy.org/)
3. [BEANS](https://beanscode.net/)
4. [DS9](http://ds9.si.edu/site/Home.html)
5. [PlasmaPy](http://www.plasmapy.org/)
6. [RADMC-3D](http://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/)
7. [spec2d](http://deep.ps.uci.edu/spec2d/0)
8. [Stingray](https://stingraysoftware.github.io/)
9. [Tardis](https://tardis.readthedocs.io/en/latest/)
10. [WCSTools](http://tdc-www.harvard.edu/software/wcstools/)
11. [ytini](http://ytini.com/index.html)

Library staff gathered "aliases" for the selected software packages through interviews with developers and online searches to build a list of search terms that could be used to refer to the software packages in articles. Staff also added identifiers and links associated with each package to the aliases list; associated identifiers and links include those tied to ADS bibcodes, Zenodo records, ASCL records, arXiv eprints, and URLs to many different types of websites. Preferred citations were also noted when they exist. 

Final edits are being made to the list of aliases: spreadsheet containing current alias list is [here](https://docs.google.com/spreadsheets/d/1DrGeb3XiVzMesHPJ9bfW_d7nkR7JqxqRvpQNNQdTKKM/edit#gid=1696232166) (working document). 

### Search Phase 1: AAS XML

The final aliases will be used to search XML files representing 20 years of articles published in AAS Journals (1997-2017).
  * If any software aliases are found in a given XML file (AAS article) we will perform the following tasks:
     * identify where the alias is appearing in the file (e.g. references section, abstract, in a table, etc.) by extracting associated XML tags
     * count the number of unique aliases used to identify the software in the file
       * AstroBlend, 10.1016/j.ascom.2016.02.002, ascl:1512.007 all showing up in one XML file would be 3 total aliases
   * if the software package alias appears in the references section of a file:
      * identify which aliases were found in the references section (e.g. DOI, URL of some kind, bibcode, software name, etc.)

After searching across all XML files for all software packages, we will aggregate the following for each software package:
   * total number of XML files containing at least one software alias
   * total number of unique aliases representing the software package across the entire corpus of files over time 
     * represents all of the ways article authors have mentioned the software
   * total number of unique XML tags associated with software aliases across the entire corpus of files 
      * represents the contexts in which article authors are mentioning the software package
    * maximum number of unique aliases representing the software package in a given file 
      * represents variability within articles
    * total number of aliases found in References sections of files
      * represents attempt by the article authors to formally cite the software package
    * find proportion: files containing aliases in references vs. total number of files containing aliases
      * represents how often article authors acknowledge software in an article but do not try to formally cite the software
    * total number of aliases found in References sections where the alias is an identifier 
      * identifiers: DOIs for articles, bibcodes, Zenodo DOIs, arXiv IDs, and ASCL IDs
    * total number of software aliases found in References sections of articles where a Zenodo DOI was cited
      * represents citation to archived code (maybe)
        * in practice we see examples where a software record in Zenodo is actually a paper ([10.5281/zenodo.1211397](https://doi.org/10.5281/zenodo.1211397))
        * in practice we have seen examples where the software authors have provided a preferred citation method ([10.5281/zenodo.163752](https://doi.org/10.5281/zenodo.163752)) requesting that article authors cite a Zenodo DOI for something other than the code ([10.5281/zenodo.1238132](https://doi.org/10.5281/zenodo.1238132)); this has been true even when a Zenodo DOI for the code exists ([10.5281/zenodo.1436012](https://doi.org/10.5281/zenodo.1436012)).

The above aggregates will help demonstrate how article authors have historically cited software in their papers and the degree to which those practices diverge from the practices that enable ADS and others to identify software citations. A follow up could be done repeating these searches annually to see how [AAS software policies](https://journals.aas.org/policy-statement-on-software/) impact software citation practices. 

The results of this case study could also be used to:
* develop more comprehensive reviewer and editor guidelines/inform policy development among publishers
* develop training and other resources for article authors and software developers to improve software citation practices
* inform the prioritization and development of tools that could be used to support software citation

### Search Phase 2: ADS API

Library staff will query the ADS API for the same software aliases over the same period of time covered by the AAS XML files. For each software package we will find:

* total number of articles containing aliases across all publications indexed by ADS
* total number of articles containing aliases across only AAS publications; the degree to which results from this ADS API search and the direct XML search match (i.e. proportion of matching bibcodes) will indicate the degree of confidence we have in our ability to use the ADS API to identify software aliases in non-AAS publications

We will compare the total number of articles containing aliases to the total number of articles that ADS would be able to identify as containing software citations (i.e. Zenodo DOIs). This will give us a better understanding of software citation practices for non-AAS publications.
