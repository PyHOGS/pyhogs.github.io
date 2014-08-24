Title: Getting Started
slug: getting-started
date: 2014-08-23 14:52:31 UTC-07:00
author: Earle Wilson
tags: python


If you are completely new to Python, this is a good place to start. Here you will find instructions on how to install Python and all the important add-on packages for doing scientific research. If you don't want to read this entire post, just scroll to the bottom.

###Getting Python
The standard way is to get Python is to download the source code from the main website <https://www.python.org/>. The installation instructions are straight forward and should only take a few minutes. If you are using a Mac, you probably already have Python installed on your computer. To check, open up a Terminal window and type `Python`. If you have Python, doing this should bring up a Python welcome message and a new prompt denoted by `>>`. Note that this pre-installed version of Python may not be the most up to date. 

Once you have Python installed, all you need is a text editor and you are good to go. However, at this point, you will only have access to the Python Standard Library and not any of the important scientific computational packages. 

###Getting important scientific packages

The [SciPy Stack](http://www.scipy.org/about.html) is a curated collection of the major scientific packages available for Python. The SciPy Stack includes **NumPy, Scipy and Matplotlib**, which are the fundamental Python packages for numerical computation and data visualization. Also included in the SciPy Stack is [Ipython](http://ipython.org/), which offers a powerful interactive shell and a browser based Notebook that allows supports code, mathematical expressions and markdown language. IPython is a *major* upgrade over the standard Python command line interface.

There are a number of ways to install the SciPy Stack. Instructions for doing so are available [here](http://www.scipy.org/install.html). The site recommends that you install the SciPy Stack via one of several Python distributions. Most of these distributions come with their own version of Python, which will be installed separately from any pre-installed Python, all the packages from the SciPy Stack and some sort of Integrated Development Environment (IDE). 

The [Enthought Canopy](https://www.enthought.com/products/canopy/) distribution seems to be a favorite among users in our group. In addition to having all the key scientific packages, Canopy has an easy-to-use (Matlab-like) IDE and uses Ipython as the default command line interface. IPython Notebooks can be hosted within the Canopy IDE as well. Enthought also has an excellent series of video tutorials. Be sure to request an [academic license](https://store.enthought.com/#canopy-academic). This gives you access to all of Canopy's features for free. 

####Getting the Seawater toolbox
This section is just for oceanographers. If you are coming from MATLAB, you are probably already familiar with the seawater toolbox. This toolbox is available in Python as well. Instructions for installing the Gibbs SeaWater toolbox and the older CSIRO toolbox can be found in this [PyHOGs meeting summary](python-hour-2014-08-18) post.


###Learning more
There are many excellent (free) Python tutorials available online. For simple explanations of basic Python features, <http://www.learnpython.org/> and <http://www.tutorialspoint.com/python/index.htm> are good starting points. When you are ready to dive into Python's scientific computing capabilities, Enthought's Python [video lectures](https://training.enthought.com/#/courses) are excellent learing tools. The videos are geared towards scientists and engineers and offer overviews of iPython, Numpy, SciPy and Matplotlib. 

For more earth science specific help, there is this website (of course) and the other websited listed in the useful links side bar on the left.

It's worth noting that Python has a large and active user community. Most google queries about a Python-related question tend to bring up results from the [Stack Overflow](http://stackoverflow.com/questions/tagged/python) forum. If you have are having difficulties trying to do something in Python, it's very likely that someone else had a similiar problem and had it resolved on that forum. 

For everything else there is PyHOGs! Please come to our meetings with any questions you may have. For updates and meeting notices, please join our [mailing list](https://mailman1.u.washington.edu/mailman/listinfo/pyhogs)

###Too long; didn't read
Want to start doing research using Python in 5 minutes or less? Install [Canopy](https://www.enthought.com/products/canopy/).





