Title: Using GitHub for PyHOGS
Slug: pyhogs_github
Date: 2014-12-01 12:25 UTC-07:00
Authors: ZB Szuts
Tags: pyhogs, website, posting, github
Summary: A tutorial of how to use GitHub for contributing to the PyHOGS repository.


# How to post to PyHOGS

This is a basic tutorial describing how to setup up PyHOGS on GitHub and perform basic maintenance of your personal repositories.  The general flow of GitHub is shown by this analog graphic:
![Connectivity of PyHOGS repositories](/images/pyhogs_github_connectivity2_mod.gif "Connectivity of PyHOGS repositories") where double-lined arrows indicate installation steps and single-lined arrows indicate working operations (pushing/pulling).

JPaul and Earle created [a repository for PyHOGS](https://github.com/PyHOGS/pyhogs.github.io "PyHOGS on GitHub") on GitHub (upper right) as a convenient way to archive and share our discussions.  As the maintainers of this repository, they have the necessary privileges (and expertise) to keep everything working smoothly.  For contributors like me, we proceed by forking this repository to create our own version (top left).  Your personal version of PyHOGS, however, lives on the web.  To copy the files to your computer, you clone your personal version to your computer (bottom left).

Your local version is where you do all of your work.  Any local changes are then pushed to your personal public repository, from which you create a pull request to ask the maintainers to accept your changes into the main repository.  Since others will contribute to the main repository, you will also need to periodically update or sync your personal repositories with the master.  This is done from the main repository to your local files, which then gets pushed to your personal repository.


## Setting up PyHOGS on GitHub

1. The first step is to make an account on GitHub, say from the [PyHOGS repository](https://github.com/PyHOGS/pyhogs-code "PyHOGS on GitHub").  
2. Return to PyHOGS and make a fork of it, but make sure to fork both parts of it (pyhogs.github.io and pyhogs-code).
3. Copy (`clone`) your private repository to your computer.  Copy the `_HTTPS_ clone URL` on the bottom right and run `git clone [URL]` from the command line.  Run the command from the directory you want to be the base directory of the pyhogs clone.  I followed JPaul's recommendation and made a directory `~/Documents/pyhogs/` into which I cloned both parts of the PyHOGS repository.

There are further installation details given on the main page of the PyHOGS repository (at the bottom).

### Comments

I found it confusing at first that the master and private repositories have very similar webpages, so it's hard to tell where you are.  The url is an easiest indicator: if you're on the master it shows `https://github.com/PyHOGS/pyhogs-code`, while if you're on your private version it includes your user name `https://github.com/zszuts/pyhogs-code` (for me).  Getting to the master is easy, just follow any of the links.  To get to your private version, click on your user name and then select your personal forked repositories.


## Add changes to your personal repositories

Your local changes need to be propagated (pushed) to your private repository and then to the master repository, following the flow diagram at top.  It's important to make sure your distribution and local copy are fully up to date/synced with the master repository before the steps below are followed (see below), otherwise you generate more work for yourself and the maintainers.

The steps are

1. add the file to the local repository, `git add [FILENAME]`
1. record the change to the local repository, `git commit -m "[DESCRIPTION] [FILENAME]"` (filename is optional, and otherwise will apply to all files added since the latest commit)
1. push the changes to your GitHub personal repository, `git push`
1. generate a pull request from your personal GitHub repository to merge your changes into the main repository


## Keeping your repositories up to date

One of the features of GitH is version tracking, which is designed into the software by requiring each user make a private repository that can push or pull changes to the master.  If you're working from an old version or branch of the repository when you generate a pull request for new files, then the automatic update system needs manual intervention by the master admins to determine how to merge divergent branches of the repository.  The merging of divergent branches can get complicated if the same files have changed in the master and your branch, and there's the potential for mutually incompatible or antagonistic changes.  (This is a problem with ipython notebook files.  They have a string at the beginning of the file that changes everytime the python code is executed, including after the file is added to the main repository.  Thus, pushing a revised notebook file will run into problems because the file in the main repository will have conflicting changes with the revised file.)   The process of merging branches is called [rebasing](http://rypress.com/tutorials/git/rebasing.html "Rebasing tutorial for GitHub").  It's easier to just avoid this and sync your local and private repositories before adding files and generating pull requests.

To sync your repository, I found [the last comment in this link](http://stackoverflow.com/questions/7244321/how-to-update-github-forked-repository "Updating forked repositories") to be very helpful.  Below is how I implemented those changes.

First, you need to link your local clone with the master repository, which you do by adding the URL of the master to your tracked repositories.  For simplicity, call it upstream.  In the directory of one of your repositories (~/Documents/pyhogs/pyhogs-code/ for me), enter

    git remote add upstream https://github.com/PyHOGS/pyhogs.github.io

Verify that you now can fetch and push from the master repository with `git remote -v`.  Then you can 

    git fetch upstream

to download any upstream changes to a separate branch in your local files.  To combine the master branch with your own run

    git merge upstream/master
    
Assuming everything is in order, unlike for me, this should happen quickly.  If there are any conflicts you will have to change them before redoing the merge (the error messages are more helpful than usual).

[N.B. I haven't yet gotten this method for updating my local repository to work]


## Additional comments

You can check the status of your local repository by typing

    git status

This shows how your local repository and your online private repository align, whether any of them have changes that need to be pushed/pulled/synced with the other.  A list of all changes you have made to your repository (using the `git` command) is obtainable with

    git log

If you've set up you private and local repositories properly, the output of

    git remote -v

gives

    origin	https://github.com/zszuts/pyhogs-code.git (fetch)
    origin	https://github.com/zszuts/pyhogs-code.git (push)
    upstream	https://github.com/PyHOGS/pyhogs-code.git (fetch)
    upstream	https://github.com/PyHOGS/pyhogs-code.git (push)

showing the available targets for pushing or fetching.  The upstream or master repository can't accept pushes, however, and so it should only be used for updating your local files and your cloned GitHub repository.

To obtain info on the various git commands, use

   git help
   man git-remote

and etc.