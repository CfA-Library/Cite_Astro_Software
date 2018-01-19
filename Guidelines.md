
# "Guidelines" for Sharing Software in Astronomy 
## Cosiderations and concrete things you can do right now to work toward implementing the [FORCE11 Software Citation Principles](https://doi.org/10.7717/peerj-cs.86)

Software can be a single script or package up to full application or
system.  For smaller items a paper may not be merited but you may
still want a DOI to refer to your software.

*There are details in here which are not meant for the associated paper, but
for the actual associated code and what it takes to get results from this code.*


##  Algorithm or system

The algorithm or system needs to be clearly described in the paper, and ideally
in the code as well. A good compromise is that the paper *source code*
is part of the code repo.

The uniqueness of the algorithm should be described. 
If it has competing algorithms a comparison should be provided.

If there is a paper it should refer to the specific version of the software.
 
*How do we deal with the living software problem - living papers?*
`Living papers can be updated with new sections added and author list updated`
See [slide 12](https://www.slideshare.net/chrislintott/software-publishing-in-aas-journals) from Chris Lintott (Jan 2016).

## Basic User Manual examples and where to get full docs

Though a paper should not be the user manual it should contain some indication of how the code is used
and where to get the full documentation.  Building the manual (if this is required) should follow the same
guidelines as installation (see below).

Ideally if there are plots and examples in the paper the recipe to reproduce those plots should be in the paper - 
this could be an appendix if it is more than a line or two or a link to a script if it is quite complex. 

There should at least be some demonstration of why the system/package is really great. 


## Obtaining the software

There should be a clear way to obtain source code. 
The code should come with a [LICENSE](https://help.github.com/articles/licensing-a-repository/). 

Plenty of common examples are in use how to get the code:
wget, curl, http, ftp, git, hg, rsync, to name a few.

    curl -O  <url>
    wget <url>


## Installation

Usually installation requires the user to pick (or better yet:
automatically detect) the computing environment, such that code can be
properly compiled (if need be). The most common ones are *autoconf*
and *cmake*, and in the case of python the *setuptools* (using the
common setup.py file). Examples have been seen where a hand-crafted
**configure.py** script was written that emulates the autoconf (bash)
version. That's quite acceptable too, but the obvious question is how well
this works in the future.

If the code has dependencies, list those (e.g. pgplot, wcslib). Would
be nice to list examples how those packages are installed in a few
common operating systems, e.g.

	     brew install pgplot  ... (check)
	     apt install pgplot5 wcslib-dev
	     yum install pgplot wcslib-devel  (check)

It goes without saying that if documentation builds (e.g. sphinx, latex)
are part of the code, they should follow the same guidelines.

## Tests

Regression or Baseline test: create a test where one (or more)
number(s) that is produced gives a result that was obtained before. 

If a code takes a long long time to run, there should be an option to
create a smaller sized test, that one can check computationally,
although it may not have any astrophysical value.

Even if the software automatically builds on something like Travis,
this still is generally not accessible to a user of the code, so there
should be someting in the code that a user can reproduce an feel
comfortable that the code will give good/expected results on his/her
computing environment.


## Publishing

To ensure proper citation, referencing a URL in the paper or a
footnote is not sufficient. ADS recommends a DOI (e.g. via [Zenodo](https://guides.github.com/activities/citable-code/))
and/or registering via [ASCL](http://ascl.net/).

We also recommend you add your own preferred bibtex entry in a small
file in the root directory of your code. ASCL will also publish this,
but best is to keep this as close to the code as possible. This file should ideally be named CITATION.md
  
Including a file documenting the elements recommended by the *[CodeMeta](https://github.com/codemeta/codemeta)* project is also recommended.

## See also 
[AAS Policy Statement on Software](http://journals.aas.org/policy/software.html)

## More Advanced or Optional?

Could there be advanced properties of code submission that are nice to
have, but we absolutely don't care about? Here is a grab bag of such
items, some of which we may want to promote to the *required*

### Code coverage

Even if we would recommend it, what fraction of code should be
covered. 80% ? 90% ? Should only the regression/baseline tests cover
100% of the code? After all, this is where it really counts.

### Decisions....

Discussion/analysis of decisions made: why did the authors do X? what
can others learn from the experience of developing X?

### Living paper issues

This will become more active in the near future as publishers accept living
papers. What ramifications does it have for the workflow. See above.
