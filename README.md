UWOcnPyUsers.github.io
======================

Website for University of Washington Oceanography Python Users Group.

Branches
----------
* `master`: built, static website files live here.
* `website`: source files for website live here.

Organization and user repos require the website to live in the master branch.
We'll use a separate branch (`website`) for the source files.

Getting the code
-----------------
Requirements:
* Pelican
* ipython
* All other modules required by above (numpy, etc).


    git clone https://github.com/UWOcnPyUsers/UWOcnPyUsers.github.io.git
    cd UWOcnPyUsers.github.io
    git checkout website
    git submodule init  #Not sure if this is needed...
    git submodule update

Testing the site
------------------
    git checkout website
    make html
    make devserver

In theory, the `devserver` target will make generate the html content as well,
but the errors from `make html` are generally easier to spot.


Updating the site
-------------------
    git checkout website
    make github

The github target generates the website content (using the `publishconf.py`),
imports the generated files to the `master` branch and then pushs the changes
to github, all in one go.

Alternatively, we could set up a post-commit hook to run `make github`
after each successful commit.


TODO
-------------
* [ ] Add RSS feeds.
* [ ] Add Disqus comments.
* [ ] Add search bar.
* [ ] Update instructions for interacting with Github (clone, push, pull).
* [ ] Fix summaries so they look nice.
* [ ] Convert ipython notebook includes to css (in plugin repo).
* [ ] Upgrade sidebar or get rid of it...
* [ ] Figure out how to get `README.md` to push with gph-import.
