# Guidelines

This document attempts to list the code properties we recommend
authors and referees can check for, to give admitted codes (works?)
some uniformity in quality etc.

The intention here is to provide guidelines for Editors and Reviewers
and thereby let authors know what is needed in a paper or software
package.


*There are details in here which are not meant for the associated paper, but
for the actual code and what it takes to get results.*


##  Algorithm 

The algorithm needs to be clearly described in the paper, and ideally
in the code as well. A good compromise is that the paper *source code*
is part of the code repo.


## Basic User Manual examples and where to get full docs



## Obtaining the software

There should be a clear way how to obtain the source code. The code should
come with one of the standard LICENSEs. 

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

## Tests

Regression or Baseline test: create a test where one (or more)
number(s) that is produced gives a result that was obtained before. 

If a code takes a long long time to run, there should be an option to
create a smaller sized test, that one can check computationally,
although it may not have any astrophysical value.


## Publishing

To ensure proper publishing, referencing a URL in the paper or a
footnote is not sufficient. ADS recommends a DOI (e.g. via Zenodo)
and/or registring via ASCL. *reference more here*

We also recommend you add your own preferred bibtex entry in a small
file in the root directory of your code. ASCL will also publish this,
but best is to keep this as close to the code as possible. The
*codemeta* project may in the end have the vehicle to contain such
metadata.

## More Advanced or Optional?

Could there be advanced properties of code submission that are nice to
have, but we absolutely don't care about? Here is a grab bag of such
items, some of which we may want to promote to the *required*

### Code coverage

Even if we would recommend it, what fraction of code should be
covered. 80% ? 90% ? Should only the regression tests cover 100% of
the code?

### Decisions....

Discussion/analysis of decisions made: why did the authors do X? what
can others learn from the experience of developing X?

### Living paper issues

This will become more active in the near future as publishers accept living
papers. What ramifications does it have for the workflow.
