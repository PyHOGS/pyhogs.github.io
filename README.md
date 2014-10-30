PyHOGS.github.io
======================

Website for University of Washington Python Hour for Oceanography and GeoSciences.

Branches
----------
* `master`: built, static website files live here.
* `pelican-source`: source files for website live here.

This site is generated using the static-site generator [Pelican](http://docs.getpelican.com).
The source files for the site, mainly in Python and Markdown, are in the 
`pelican-source` branch. These files are then processed by `pelican` and
uploaded to [Github](https://github.com/PyHOGS/pyhogs.github.io) on the `master`
branch. Github pages requires that the website content is stored on the `master`
branch for Organization and User websites. 

Getting the code
-----------------
Requirements:

* Pelican, webassets, requests, markdown, ghp-import
* ipython
* All other modules required by above (numpy, etc)

The following command should install all dependancies through `pip`. Run it in
a suitable [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/).

    pip install pelican webassets requests markdown ipython ghp-import

After the dependancies are installed, get the site code via:

    git clone https://github.com/PyHOGS/pyhogs.github.io.git
    cd pyhogs.github.io
    git checkout pelican-source
    git submodule init  #Not sure if this is needed...
    git submodule update

Testing the site
------------------
    git checkout pelican-source
    make html
    make serve

In theory, the `devserver` target will make generate the html content as well,
but the errors from `make html` are generally easier to spot.


Updating the site
-------------------
    git checkout pelican-source # Make sure you're on the correct branch.
    make github

The github target generates the website content (using the `publishconf.py`),
imports the generated files to the `master` branch and then pushs the changes
to github, all in one go.


Current TODO
-------------
* [ ] Add RSS feeds.
* [X] Add Disqus comments.
* [ ] Add search bar.
* [ ] Update instructions for interacting with Github (clone, push, pull).
* [ ] Fix summaries so they look nice.
* [X] Convert ipython notebook includes to css (in plugin repo).
* [X] Upgrade sidebar or get rid of it...
* [X] Figure out how to get `README.md` to push with gph-import.
* [ ] Add calendar
