Title: Use Github with PyHOGS
Slug: pyhogs-github
Date: 2014-12-01 12:25 UTC-07:00
Authors: ZB Szuts
Tags: pyhogs, website, posting, github
Summary: A tutorial of how to use GitHub for contributing to the PyHOGS repository.


# How to use GitHub for PyHOGS

This is a basic tutorial describing how to setup up PyHOGS on GitHub and perform basic maintenance of your personal repositories.  The general flow of GitHub is shown by this analog-sourced graphic:
![Connectivity of PyHOGS repositories](/images/pyhogs_github_connectivity2_mod.gif "Connectivity of PyHOGS repositories"), where double-lined arrows indicate installation steps and single-lined arrows indicate working operations (pushing/pulling).

JPaul and Earle created [a repository for PyHOGS][PyHOGS] on GitHub (upper right) as a convenient way to archive and share our discussions.  As the maintainers of this repository, they have the necessary privileges (and expertise) to keep everything working smoothly.  For contributors like me, we proceed by **forking** this repository to create our own version (top left).  Your personal version of PyHOGS, however, lives on the web.  To copy the files to your computer, you **clone** your personal version to your computer (bottom left).

Your local version is where you do all of your work.  Any local changes are then **pushed** to your personal, public repository (on Github), from which you create a **Pull Request** to ask the maintainers to accept your changes into the main repository.  Since others will contribute to the main repository, you will also need to periodically update or sync your personal repositories with the main.  To do this you **fetch** upstream changes and then **merge** them into your local files. which then gets **pushed** back to your personal repository on Github.


## Setting up PyHOGS on GitHub

1. The first step is to [make an account on GitHub](https://github.com/join).
2. Once logged-in, navigate to the [PyHOGS][PyHOGS] repository (or *repo* for
    short).  If you're new to GitHub, explore the site, look at the files in
    the repo, and check out the Issues Page where you can submit problems or
    request improvements.
3. Near the upper-right corner of the [PyHOGS Project Page][PyHOGS] there is a
    link to *fork* the project. Make a fork of the PyHOGS repo by clicking the `
    Fork` button.

    This creates your own personal copy of the  repo in your account. This copy
    lives online and mostly just mirrors the  changes you have made locally on
    your computer.  You can use this copy to  send a [Pull
    Request](https://help.github.com/articles/using-pull-requests/) which tells
    the site maintainers that you would like them to incorporate your changes.

4. `clone` (i.e. copy) your personal repository on GitHub to your computer.
    Copy the `HTTPS clone URL` on the bottom right of the forked repository
    page and run `git clone [URL]` from the command line.  Run the command
    from the directory you want     to be the parent directory of your
    repository.  I used `~/Documents/`.  

    For example:

        cd ~/Documents
        git clone https://github.com/zszuts/pyhogs.github.io.git
        # Replace the above URL with the one in the box HTTPS clone URL

There are further installation details given on the [main page of the PyHOGS repository][PyHOGS] (at the bottom).

### Comments

I found it confusing at first that the main and personal repositories have very similar webpages, so it's hard to tell where you are.  The url is an easy indicator: if you're on the main it shows `https://github.com/PyHOGS/pyhogs.github.io`, while if you're on your personal version it includes your user name `https://github.com/zszuts/pyhogs.github.io` (for me).  Getting to the main is easy, just follow any of the links.  To get to your personal version, click on your user name and then select your personal forked repositories.


## Add changes to your personal repositories

Your local changes need to be propagated (pushed) to your personal repository and then to the main repository, following the flow diagram at top.  It's important to make sure your distribution and local copy are fully up to date/synced with the main repository before the steps below are followed (see below), otherwise you generate more work for yourself and the maintainers. However, if for some reason you run into *merge conflicts* at this stage, feel free to email the maintainers for help.

The steps are

1. Add the file (or files) to the local repository, `git add [FILENAME]`
2. Record the change to the local repository, `git commit -m "[DESCRIPTION]"`
3. Push the changes to your GitHub personal repository, `git push`.
4. Generate a pull request from your personal GitHub repository to merge your
    changes into the main repository


## Keeping your repositories up to date

One of the features of GitHub is branch tracking, which is designed into the software by requiring each user make a personal repository that can push or pull changes to the main.  If you're working from an old version or branch of the repository when you generate a pull request for new files, then the automatic update system needs manual intervention by the admins to determine how to merge divergent branches of the repository.  The merging of divergent branches can get complicated if the same files have changed in the main branch and your branch, and there's the potential for mutually incompatible or antagonistic changes$^1$.   The preferred process of merging branches is called [rebasing](http://rypress.com/tutorials/git/rebasing.html "Rebasing tutorial for GitHub").  It's easier to just avoid this and sync your local and personal repositories before adding files and generating pull requests.  On the other hand, it's probably inevitable that the website will change before you've finished your changes...

[A list of steps for syncing is available](http://pyhogs.github.io/pyhogs_syncing.html "Steps to sync local PyHOGS repo"), which summarizes the tutorial below.

To sync your repository, I found [the last comment in this link](http://stackoverflow.com/questions/7244321/how-to-update-github-forked-repository "Updating forked repositories") to be very helpful.  Below is how I implemented those changes, with many pointers from JPaul and Earle.

To update your local repository with changes from the main site:

1. First, you need to link your local clone with the main repository, which you
    do by adding the URL of the main repo as a `remote` of your local repo.  For
    simplicity, call it `upstream`.  In the directory of your
    repository (`~/Documents/pyhogs/pyhogs.github.io/`` for me), enter

        git remote add upstream https://github.com/PyHOGS/pyhogs.github.io

2. You can verify the remote repos with `git remote -v`.  If you've set up you
    personal and local repositories properly, you should see:

        $git remote -v
        origin	https://github.com/zszuts/pyhogs.github.io.git (fetch)
        origin	https://github.com/zszuts/pyhogs.github.io.git (push)
        upstream	https://github.com/PyHOGS/pyhogs.github.io.git (fetch)
        upstream	https://github.com/PyHOGS/pyhogs.github.io.git (push)

    showing the available targets for `push`ing or `fetch`ing.  The `upstream`
    or main repository can't accept pushes, however, and so it should only be
    used for updating your local files and your cloned GitHub repository. Also
    note the `origin` remote. This was automatically created when you
    `git clone`'d the repository and points to the online version on Github.

3. Then you need to download any upstream changes.  The "main" branch of the
    repo is `pelican-source`$^2$.  This holds all of the website content and
    configuration settings to generate the site. It should be the default local
    and remote branch.  To access the version of this branch on upstream, you
    use `upstream/pelican-source`.

    Download the upstream changes and incorporate them with

        $git fetch upstream  #Downloads changes
        $git status  # Displays status.  
        # At this point you can dig around a bit to see what's changed before
        # you actually make the changes to your files
        $git merge upstream/pelican-source # Merges upstream changes into your version.

    Assuming everything is in order, this should happen quickly.  If there are
    any conflicts you will have to change them before committing the merge.

From JPaul: "An alternate to calling `git fetch` and `git merge` is to use `git pull` (namely `git pull upstream pelican-source` for this example) to do both at once.  When you're updating your repository from a remote you'll usually want to make sure it does a fast-forward merge so that the history doesn't require messy merge commits.  This should usually happen by default . (Although... see this argument for [why you should do the fetch and merge separately](http://longair.net/blog/2009/04/16/git-fetch-and-merge/).)

Alternatively, you can use a GUI like [SourceTree](http://www.sourcetreeapp.com/) to do these operations. It provides a graphical view of changes that you and others have made and provides a relatively simple, yet powerful, interface to `git`.

## Additional comments

You can check the status of your local repository by typing

    git status

This shows how your local repository and your online personal repository align, whether any of them have changes that need to be pushed/pulled/synced with the other.  A list of all changes you have made to your repository (using the `git` command) is obtainable with

    git log

To obtain info on the various git commands, use

   git help
   man git-remote

and etc.

To undo failed merges, you can do either

   git reset --hard <previous_commit>

where the last commit ID needed for `<previous_commit>` can be found with `git log --oneline`, or

    git merge --abort

(for Git versions 1.7.4 or later).

To learn more about branches and merging, [here](http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging "Git Branching and Merging") is a good place to start.

[PyHOGS]: https://github.com/PyHOGS/pyhogs.github.io "PyHOGS on GitHub"

#### Footnotes

$^1$ iPython notebooks can be a real problem due to a SHA1 hash string at the beginning of the file that changes every time the notebook is executed.  Thus, pushing a revised notebook file will run into problems because the file in the main repository will have conflicting changes with the revised file.  In general, just use the latest version of the notebook, but browse through it to make sure no other
changes have been made.

$^2$ Why do you only use `upstream/pelican-source`?  From JPaul:  "The 'main' branch for pyhogs.github.io is `pelican-source` and not the usual `master`.  This is because of the way github-pages works - the actual website content has to be on the master branch for an organization's website.  No one needs to directly interact with the master branch - it's automatically generated via `make github` and `ghp-import`.  If you fork and clone from the website, the default branch should be properly set to `pelican-source`."
