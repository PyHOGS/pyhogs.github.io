Title: Syncing PyHOGS with GitHub
Slug: github_syncing
Date: 2014-12-08 12:40 UTC-07:00
Authors: JPaul Rinehimer, ZB Szuts
Tags: pyhogs, github, sync, update
Summary: A list of steps for syncing your local PyHOGS repository.

# How to sync your local PyHOGS repository with the main repository

To summarize, here are steps to get a locally synced copy of the pyhogs repo.

1. Fork the pyhogs repo to make a personal repo.

2. Clone your forked version of the pyhogs repo to your local repository (the link can be copied from the right hand of YOUR repository's page:

   	 git clone https://github.com/YOUR_USERNAME/pyhogs.github.io
    You should already have done these steps earlier, otherwise there wouldn't be any changes that need to be updated.

3. From your local pyhogs.github.io repo, add remote that points upstream to the original repo (the link can also be copied from the the main pyhogs.github.io page):

   	git remote add upstream https://github.com/PyHOGS/pyhogs.github.io

    To check that your remotes are configured properly, do `git remote -v`

4. At this point, you will only have the `pelican-source` branch. To fetch other branches and new commits, do

        git fetch upstream

    This should retrieve master branch and any other branch we have created.

5. To merge the fetched changes to your pelican-source branch do

        git merge upstream/pelican-source

    You could probably combine this and the previous steps with a single `git pull upstream pelican-source` command, but I prefer to do them separately.

6. At this point you should be all set. If you made changes to repo that you want to relay upstream, first do a fetch/merge (steps 4 and 5) to make sure you're up to date. If there are any conflicts, try to resolve them on your end. When you are ready, push your changes to YOUR github repo then create a pull request from your personal repo to the main repo.

    On our end, we would then accept your pull request, pull those changes to our repo, generate the website (locally, to make sure everything is in order) then do `make github` to make your changes live.


For a more exhaustive treatment, see [this tutorial](http://pyhogs.github.io/pyhogs_github.html).
