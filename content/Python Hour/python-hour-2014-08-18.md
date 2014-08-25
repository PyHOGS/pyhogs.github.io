Title: Python Hour - 18 August 2014
slug: python-hour-2014-08-18
date: 2014-08-18 12:00 UTC-07:00
tags: github, Mercurial, SeaWater toolbox, figures
author: Earle Wilson


+ **We spent the first 15 minutes or so talking about `git` and how it's different from other version control software, specifically Mercurial.**\* After the meeting, I found this short [wiki](http://www.wikivs.com/wiki/Git_vs_Mercurial) that does a nice comparison of the two. One of the main differences is that git uses a two-step commit process, whereas Mercurial uses a single step. Using git, you first have to add new changes to what is called an "index" or "staging area" before you can commit those changes to your local repository. So, in git, your workflow might be like:

    -->Make changes to file.
    
    -->Add changes (all at once or piecemeal) to staging area using [git add](http://git-scm.com/docs/git-add). 
    
    -->Commit changes, stored in staging area, to local repository using [git commit](http://git-scm.com/docs/git-commit).
    
    Having this staging area gives you more control over the commit process. JPaul showed us that you can use `git add` to split new changes into what are known as "hunks" and commit those hunks individually - rather than all at once . This [ blog article](http://alblue.bandlem.com/2011/10/git-tip-of-week-interactive-adding.html) gives a nice example of how and why you would stage and commit hunks. Whether or not you find this feature useful will depend on your workflow. If you prefer to work for long stretches without committing and/or need to keep a detailed log the changes you're making to a file, you will probably find the `git add` feature useful. Otherwise, you might find it to be unneccesary and somewhat annoying.
    
    \* *In case you're wondering why we keep talking about git, it's because we have a [github repository](https://github.com/UWOcnPyUsers/uwocnpyusers) set up for the group. The hope is that we will one day use it to share and work on Python code among ourselves.*


+ **We also talked about [SourceTree](http://www.sourcetreeapp.com/)**, which is a neat graphical user interface for managing Git and Mercurial. SoureTree is probably a lot more user friendly than the command line. Parker and JPaul seem to like it.


+ **JPaul showed us how to install the Gibbs SeaWater toolbox into Canopy.** In case you don't know, the [Gibbs SeaWater Oceanographic Toolbox](http://www.teos-10.org/pubs/gsw/html/gsw_contents.html) is a library of routines for computing different thermodynamic properties of seawater, such as density, potential temperature and buoyancy frequency. The organization that maintains SeaWater also has similar libraries for computing ice and air properties. Canopy does not come with the Gibbs SeaWater Toolbox, but you can install it manually using [pip](https://pypi.python.org/pypi/pip). 

    `Pip` is the official python package manager and it is automatically installed when you install Canopy. **To install a python package that is not included in Canopy, you first open up a Canopy terminal then type `pip install name_of_package` at the prompt.** You can open a Canopy terminal window by going to `Tools` in the Canopy menubar. If Canopy is your default Python environment, you can do `pip install` from a regular terminal window. `Pip` then searches the [PyPI](https://pypi.python.org/pypi/) database for the package and installs it into Canopy. PyPI is the official Python Package Index.
      
    So, to install the Gibbs SeaWater toolbox all you need to do is: `pip install gsw` from the terminal command line. To use it in python, you need to import it via `import gsw`. Similarly, you can get the older [CSIRO seawater toobox](https://pypi.python.org/pypi/seawater/) by doing `pip install seawater`.


+ **Parker introduced us to the `np.choose` method.** `np.choose` is another way of pulling values from an array. It's useful when trying to index a N-dimensional array; Parker used `np.choose` in a routine that maps sigma coordinates to z-level coordinates. It's usage is somewhat complicated - perhaps unnecessarily so. (You can tell that the person who wrote the help documentation is pretty frustrated with everyone's confusion.) A related numpy method is `np.take`.



+ **We briefly talked about some different ways to set up a figure.** Here are a few examples (use help for learn about more options):
	
	
``` python

import matplotlib.pyplot as plt
	
fig = plt.figure() #makes a new figure and returns handle.
	
fig = plt.figure(figsize = (10,8)) #same as above but fixes the fig. window to be 10'' by 8''
	
ax = fig.add_axes() #creates axes in figure (named fig) and returns handle
	
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #same as above but now specifying the location and size. 

ax = plt.subplot(111) #makes a single subplot into current figure and returns axes handle.
	
ax = plt.subplot(1,1,1) #another way of doing the above.
	
ax = plt.subplot(2,2,1) #similar to the above but creates the first plot for a 2x2 subplot.
	
fig,(ax1,ax2,ax3,ax4) = plt.subplots(2,2) #creates a new figure with a 2x2 subplot. returns handles for each.	

#For the simplest of plots, you can choose to do none of the above and just create the plot. For example, doing something like plt.plot(x,y) will create a figure and an axes by default. Also useful are the get current axes and figure methods:

ax = plt.gca() #gets handle for current axes
	
fig = plt.gcf() #gets handle for current figure
```