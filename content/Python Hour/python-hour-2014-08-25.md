Title: Python Hour - 25 August 2014
slug: python-hour-2014-08-25
date: 2014-08-25 12:00 UTC-07:00
tags: permutations, KDTree, debugging, functions
summary: We discussed the itertool and KDTree modules, ways to debug code, and keyword arguments.
author: Earle Wilson

+ Parker introduced us to the [itertools.permutations](https://docs.python.org/2/library/itertools.html#itertools.permutations) function. You can use this function to return all possible permutations of an iterable object, such as a list. For example, the code snippet below returns a list of all the permutations of `0,1,2`:
	
		:::python
	
		import itertools
		a = range(3)
		a_perm = list(itertools.permutations(a)) 
		print a_perm

	This will print:
	
		:::python
		
		[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
		
 
	
	This apparently comes in handy when designing a python script to play tic-tac-toe.
	
	
+ Parker also told us about the [`KDTree` class](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html) from the `scipy.spatial` module. KDTree provides efficient methods for finding the nearest-neighbors of a point (or a set of points) in a grid of spatial points. In particular, `KDTree.query` is useful when trying to interpolate values on a grid where the spacings are uneven. An example of its usage is provided [here](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.query.html#scipy.spatial.KDTree.query).

+ We discussed a few ways to debug code in ipython. First, there is the magic command `%debug`, which launches a post-mortem [debugging session](http://ipython.org/ipython-doc/1/interactive/tutorial.html#debugging) after an exception is thrown. That is, if a script crashes, running `%debug` activates the [python debugger (pbd)](https://docs.python.org/2/library/pdb.html) and brings you to the line in the script where the error happened. The pdb gives you a special command line interface to explore the namespace of the code, execute commands and [set breakpoints](https://docs.python.org/2/library/pdb.html#debugger-commands). Another alternative is the [Tracer](http://ipython.org/ipython-doc/dev/api/generated/IPython.core.debugger.html#classes) object from the `IPython.core.debugger` module. The Tracer object can be used to activate a pdb session from anywhere in a script, which means you can use it as a breakpoint. For example:

		:::python	
		
		from IPython.core.debugger import Tracer
		debug_here = Tracer()
		
		
		
		#later in code
		debug_here() #code stops here and pdb is launched.



+ We briefly talked about keyword arguments and the different ways we can supply inputs to a function. Most of what we discussed is covered in [Section 4.7](https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments) on this python doc page. With keyword arguments, we can specify function arguments in any order, provided that the right keyword is used. Keyword arguments are particularly useful for setting [default argument values](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values). Here is an example:

		:::python
		
		def fun(x,y, col='r', lw=2):
			import matplotlib.pyplot as plt
			plt.figure()
			plt.plot(x, y, color=col, linewidth=lw)
			plt.show()
		
		
		#some good ways to call the function
		a = arange(10)
		b = a**2
		
		fun(a,b) 
		fun(a, b, color='violet') 
		fun(a, b, 'orange', 3) 
		fun(x=a, y=b) #using x and y as keywords
		fun(col='crimson', x=a, lw=3, y=b) #order of keyword arguments does not matter

	

	





