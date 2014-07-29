UWOcnPyUsers.github.io
======================

Website for University of Washington Oceanography Python Users Group.

Branches
----------
* `master`: built, static website files live here.
* `website`: source files for website live here.

Organization and user repos require the website to live in the master branch.
We'll use a separate branch (`website`) for the source files.

Testing the site
------------------
    git branch website
    make html
    make devserver

In theory, the `devserver` target will make generate the html content as well,
but the errors from `make html` are generally easier to spot.


Updating the site
-------------------
    git branch website
    make github

The github target generates the website content (using the `publishconf.py`),
imports the generated files to the `master` branch and then pushs the changes
to github, all in one go.

Alternatively, we could set up a post-commit hook to run `make github`
after each successful commit.
