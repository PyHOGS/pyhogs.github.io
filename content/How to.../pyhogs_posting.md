Title: Write a post for PyHOGS
Slug: pyhogs-posting
Date: 2014-12-01 12:25 UTC-07:00
Authors: ZB Szuts
Tags: pyhogs, website, posting, notebook, ipython
Summary: A tutorial of how to post to the PyHOGS website: making an iPython Notebook and supporting files and adding them to the PyHOGS GitHub repository.


# How to post to PyHOGS

This is a basic tutorial describing how to create a post for the PyHOGS website using iPython Notebooks and Markdown. There is a recent [Nature Toolbox article](http://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261 "Nature Toolbox: interactive notebooks sharing the code") on iPython Notebooks that may be of interest.  See the companion post [How to... Use GitHub with PyHOGS]({filename}/How to.../pyhogs_github.md) for more details on setting up and using GitHub.  

All posts for the website are written in [Markdown](http://daringfireball.net/projects/markdown/syntax) and can contain an optional [iPython notebook](http://ipython.org/notebook.html).  Markdown is a simplified markup language designed for conversion to other formats such as HTML. iPython Notebooks allow the interactive evaluation of Python code, the display of figures and equations, the integration of Python code and Markdown, and easy publishing of code and results to HTML.

Most posts (e.g. see  [here](https://raw.githubusercontent.com/PyHOGS/pyhogs.github.io/pelican-source/content/How%20to.../colormaps.md) and [here](https://github.com/PyHOGS/pyhogs.github.io/blob/pelican-source/pyhogs-code/notebooks/examples/Colormap_examples.ipynb)) are written using an iPython Notebook and a Markdown stub.  This allows Python code to be executed when the webpage is created to show Python examples.  Posts can also be written in Markdown alone and don't require an iPython notebook.  [This post](https://raw.githubusercontent.com/PyHOGS/pyhogs.github.io/pelican-source/content/How%20to.../pyhogs_posting.md), for example, is written solely in Markdown, since no Python output needs to be displayed.  

The easiest way to add content is to create a iPython notebook or Markdown webpage and email it directly to J. Paul or Earle, who maintain the PyHOGS GitHub repository, and can quickly incorporate it into the website. This method is easy, best for the one-time poster, and doesn't require setting up a Github account and a Git repository.

Alternatively, if you want to learn new software, or want to contribute more regularly, you can learn how to work with GitHub.  This is the pathway I describe here.  The steps involved are:

* Write the notebook in iPython Notebook (Only needed if evaulating Python code).[^1]
* Generate the post in Markdown.
* Add and commit the notebook and post to your local personal repository.
* Push your local changes to your PyHOGS GitHub repository.
* Create a pull request to the PyHOGS main repository to ask the maintainers to add your additions.

## Making an iPython Notebook

Having installed the Enthought Canopy version of python on my computer (OS 10.8), I simply run

    ipython notebook &

to open the notebook editor in the active browser window.  The directory the command is run from is the base directory for the ipython notebook session.  To add or edit notebooks for the website, run the above command in the `pyhogs.github.io/pyhogs-code/notebooks` directory where `pyhogs.github.io` points to the base directory of the Github repository.  Create a new notebook to start editing.

Notebooks are arranged as cells, where each cell is either a block of Markdown formatted text or a series of input commands for iPython.  You can create new cells (under the menu item Insert), and the pull-down menu lets you change between code or markdown.  By running a cell (the play button, or press shift+enter), the commands are processed: either for markdown formatting or to run the python code and display the output (if any) at the end of the cell.

To get started with Markdown, here are a few commands:

- `#` generates a header, and using two `##` (or three, ...) makes subheaders.
- Unordered lists are generated by multiple lines beginning with `-` or `+` or `*`. A blank line is needed before the list.
- Ordered (i.e. numbered) lists are generated by starting lines with `1.`, `2.`, etc.  The actual number doesn't matter and the correct ordering will be generated when code is converted to html.  Again, a blank line is needed before the list starts.
- emphasis/italics is made by `_xxx_` or `*xxx*`.
- bold is made by `__xxx__` or `**xxx**`.
- in-text code is bracketed by backward apostrophe, e.g. `` `command` `` gives `command`
- multiple lines of block code is made by lines starting with a tab (the entire block preceded by a blank line)

Additional nice features are that it understands LaTeX math formatting (through [an extension](http://nbviewer.ipython.org/github/ipython/ipython/blob/2.x/examples/Notebook/Typesetting%20Math%20Using%20MathJax.ipynb)) and can include links and images.  The [official Markdown page](http://daringfireball.net/projects/markdown/syntax "markdown formatting") has information on more syntax and features.

Assume that you've now written up a test notebook `sample.ipynb` and want to get it onto the PyHOGS website.  Make sure it is located in the notebook folder of the PyHOGS repository (`pyhogs.github.io/pyhogs-code/notebooks/examples/`).  If you started `ipython notebook` in this directory, your notebook will be located there by default.

## Files for the PyHOGS website

Though the PyHOGS repository can take notebooks directly, to add a webpage a wrapper file is needed to supply metadata for the post.

For tutorials in the [how-to section](http://pyhogs.github.io/category/how-to.html "PyHOGS website How To"), these wrapper files are in `pyhogs.github.io/content/How\ to.../`.  They are written in Markdown (`.md`) and one example [pyhogs.github.io/content/How\ to.../colormap_bathy.md](https://github.com/PyHOGS/pyhogs.github.io/blob/pelican-source/content/How%20to.../colormaps.md) looks like this

    Title: Colormap example for bathymetry
    Slug: colormap-bathymetry
    Date: 2014-11-04 13:12 UTC-07:00
    Authors: ZB Szuts
    Tags: color, colormap, jet, bathymetry
    Summary: An example of making a map with filled bathymetric contours in matplotlib.

    {% literal notebook examples/Colormap_bathy.ipynb %}

Either copy an existing file or use the [template]({filename}/static/post-template.md "Template for markdown wrapper for PyHOGS post"), also located in `pyhogs.github.io/content/static/post-template.md`.  Call it `sample.md` (or the name of your post) and put it in `pyhogs.github.io/content/How\ to.../` Actually, any subdirectory below `content` works - the subdirectory just specifies the category for the website post.

## Contributing to the PyHOGS repository

Your local changes need to be propagated (*pushed*) to your personal, public repository and then to the main repository.  It's important to make sure your distribution and local copy are fully up to date/synced with the main repository before the steps below are followed.  (See companion post [How to... Use GitHub with PyHOGS]({filename}/How to.../pyhogs_github.md).)

The steps are

1. Add the file(s) to your local repository.
2. Commit the changes in your local repository.
3. Push the file from the local repository to your online (Github) personal repository.
4. Create a pull request to ask the maintainers to add the changes to the main repository.

The add step needs to be done for all new files.  For this example, that includes the notebook and the wrapper files.

    cd ~/Documents/pyhogs/pyhogs.github.io/pyhogs-code/notebooks/examples/
    git add sample.ipynb
    cd ~/Documents/pyhogs/pyhogs.github.io/content/How\ to.../
    git add sample.md
    git commit -m "Add a notebook and wrapper"

The `-m` switch (for `--message`) with `git commit` attaches a quick description of the file/changes, which is especially useful for others (e.g. the maintainers).  The commit can cover multiple files, or it can be done after each one.  This message is critical, since it is archived in the repository's history.  It's better practice to add the notebook before the wrapper file, since the notebook is stand-alone but the wrapper requires the notebook.  Thus there won't be the potential for errors if only the first addition makes it through a merge.

On commit messages, J. Paul adds: "While there's lots of rules and conventions on commit messages (just google "git commit messages" for some of them), the only one we really need to follow is this: The first line should always be 50 characters or less. If needed, this summary line is then followed by a blank line and additional, in-depth information.  This is because the first line is used for `git log` commands and it truncates it to 50(?) characters. I think longer (up to maybe 80) is just fine, but the idea is to keep it short, sweet, and to the point."


The third step

    git push

pushes all committed changes from your local repository to your personal version on GitHub.

Now go online to your personal repository.  Click the Pull Request button to ask the maintainers to accept your change.  It's good practice to add a comment that describes the new files or the changes, but this comment is less critical than the one made by `git commit`.  It's worth noting any peculiarities to the maintainers, such as images whose paths/directories may need to be changed, etc.  Once your pull request is accepted, your content will be added to the PyHOGS website!


[^1]: If you don't need any Python execution, then you can simply write in Markdown (as done for this post).  This is in fact preferable, since it makes for cleaner code and avoids some difficulties with using notebook files.  [reStructured Text (.rst)](http://docutils.sourceforge.net/rst.html) is also suitable for submission, but you (currently) cannot include iPython notebook files with .rst files due to limitations in the [website parsing program](http://docs.getpelican.com/en/3.5.0/) and its extensions.