
# AAS Journals Software Policies and Author Guidelines

## Software Papers and Citation Policy

In original form: [journals.aas.org:Policies:Software](http://journals.aas.org/policy/software.html) (released 1 January 2016)

Quick summary for software papers: *If a piece of novel software is important to published research then it is likely appropriate to describe it in such a paper.*

The "paper" policy goes on to summarize expected contents (*description of the software, its novel features and its intended use*) and recommendations (*open source licensing and archival versioning*) for software papers.

The expectations for citation are specific (*citing the paper describing the software and citing a DOI for the software*) to achieve the dual purpose of extending credit to authors and  giving the reader access to the exact version of the software used in the project. 

The software policy statement also introduced the `LaTeX` tag 

    \software{Astropy \citep{http://dx.doi.org/10.1051/0004-6361/201322068}}   

which provides context free mentions (and citations) for code used in a paper. 



## Guidelines: Software papers & Source Code

Presently we do not provide detailed guidelines on the expected contents of a "software paper." The [general requirements](http://journals.aas.org/authors/manuscript.html) stand as do those mentioned above in the original policy. 

We do, however, have guidelines on the inclusion of source code in Journal articles. That material can be found here: [journals.aas.org:Data Guide](http://journals.aas.org/authors/data.html#Code). In summary source codes should be archived in a persistent repository and cited in the references to the paper. 

Also provided is a GitHub based tutorial ([AASJournals/Tutorials:Repositories](https://github.com/AASJournals/Tutorials/tree/master/Repositories)) for authors using persistent repositories. We include a [curation workflow](https://github.com/AASJournals/Tutorials/blob/master/Repositories/UsingRepositories.md#curating-your-repository), which is admittedly difficult to keep aligned with all the archives' current features/UIs.


## Guidelines: Citation

In original form:  
* [journals.aas.org:Preparation:References](http://journals.aas.org/authors/references.html#Software);
* [journals.aas.org:AASTeX:Software]( http://journals.aas.org/authors/aastex/aasguide.html#software)
* [journals.aas.org:AASTeX:Citing DOIs](http://journals.aas.org/authors/aastex/aasguide.html#softwareandthirdparty)

Detailed guidelines are provided for adding persistent (software) repositories to a journal article, including markup and BiBTeX. Our current BiBTeX style ([`aasjournal.bst`](http://journals.aas.org/authors/aastex/aasjournal.bst)) expects software DOIs to be encoded with `version` and `publisher` information. A citation tutorial is provided on GitHub ([AASJournals/Tutorials:Citing Repositories](https://github.com/AASJournals/Tutorials/blob/master/Repositories/CitingRepositories.md)).
