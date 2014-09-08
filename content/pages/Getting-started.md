Title: Getting Started
slug: getting-started
date: 2014-08-23 14:52:31 UTC-07:00
author: Earle Wilson
tags: python


If you are completely new to Python, this is a good place to start. Here you will find instructions for installing Python and all the important add-on packages for doing scientific analysis.

###Quick start
To install Python with minimal effort, download [Canopy](https://www.enthought.com/products/canopy/). Canopy comes with all the major scientific and numerical packages you will need to start doing research with Python. Be sure to request an [academic license](https://store.enthought.com/#canopy-academic). To learn more about the tools you get with Canopy and other ways of setting up Python, continue reading.

###Getting Python
The standard way to get Python is to download the source code from the main website: <https://www.python.org/>. You will have a choice between Python 2 and Python 3. Python 3 is billed as an improvement to Python 2, but [the scientific community has been slow in adopting that upgrade](http://jakevdp.github.io/blog/2013/01/03/will-scientists-ever-move-to-python-3/). The biggest issue is that Python 3 is not backwards compatible, but for new users, this should not be a problem.  For now, choosing either Python 2 or 3 should be fine, but be aware of their [differences](https://docs.python.org/3/whatsnew/3.0.html) and realize that you will likely have to switch to Python 3 in the future. The installation instructions for either are straight forward and should only take a few minutes. 

If you are using a Mac, you probably already have Python installed on your computer. To check, open up a Terminal window and type `Python`. If you have Python, doing this should bring up a Python welcome message and a new prompt denoted by `>>`. Note that this pre-installed version of Python is (likely) verison 2.x. 

Once you have Python installed, all you need is a text editor and you are good to go. However, at this point, you will only have access to the Python Standard Library and not any of the important scientific computational packages. 

###The SciPy Stack

The [SciPy Stack](http://www.scipy.org/about.html) is a curated collection of the major scientific packages available for Python. The SciPy Stack includes **NumPy, Scipy and Matplotlib**, which are the fundamental Python packages for numerical computation and data visualization. Also included in the SciPy Stack is [Ipython](http://ipython.org/), which offers a powerful interactive shell and a browser based Notebook for sharing code. IPython is a *major* upgrade over the standard Python command line interface.

There are a number of ways to install the SciPy Stack. Instructions for doing so are available on the [SciPy Stack install page](http://www.scipy.org/install.html). The site recommends that you install the SciPy Stack via one of several Python distributions. Most of these distributions come with their own version of Python, which will be installed separately from any pre-installed Python, the SciPy Stack and a well-equiped Integrated Development Environment (IDE). The [Enthought Canopy](https://www.enthought.com/products/canopy/) distribution seems to be a favorite among users in our group. Also note that, as of September 2014, Canopy still runs on Python 2.

####Getting the Seawater toolbox
This section is just for oceanographers. If you are coming from MATLAB, you are probably already familiar with the seawater toolbox. This toolbox is available in Python as well. Instructions for installing the [Gibbs SeaWater](http://www.teos-10.org/software.htm) toolbox and the older [CSIRO Seaweater](http://www.cmar.csiro.au/datacentre/ext_docs/seawater.htm) toolbox can be found in this [PyHOGs meeting summary](../python-hour-2014-08-18) post.


###Learning more
There are many excellent (free) Python tutorials available online. For simple explanations of basic Python features, <http://www.learnpython.org/> and <http://www.tutorialspoint.com/python/index.htm> are good starting points. We also have a [Python basics review](python-basics-review) on our website. When you are ready to dive into Python's scientific computing capabilities, Enthought's Python [video lectures](https://training.enthought.com/#/courses) are excellent learing tools. The videos are geared towards scientists and engineers and offer overviews of iPython, Numpy, SciPy and Matplotlib. 

For everything else there is google! Google queries about a Python-related question tend to bring up results from the [Stack Overflow](http://stackoverflow.com/questions/tagged/python) forum. If you have are having difficulties trying to do something in Python, it's very likely that someone else had a similiar problem and had it resolved on that forum. 







