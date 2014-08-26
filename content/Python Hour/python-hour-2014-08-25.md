Title: Python Hour - 25 August 2014
slug: python-hour-2014-08-25
date: 2014-08-25 12:00 UTC-07:00
tags: permutations, KDTree, debugging, functions
summary: Summary of PyHOGs meeting on August 25, 2014
author: Earle Wilson

+ Parker introduced us to the [itertools.permutations](https://docs.python.org/2/library/itertools.html#itertools.permutations) function. You can use this function to return all possible permutations of an iterable object, such as a list. This apparently comes in handy when designing a python script to play tic-tac-toe. For example, the code snippet below returns a list of all possible permutations of `0,1,2,3`:
	
		:::python
	
		import itertools
		a = range(4)
		a_perm = list(itertools.permutations(a)) 


 
+ Parker also told us about the [`KDTree`](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html) class from the `scipy.spatial` module. KDTree provides efficient methods, e.g. `KDtree.query`, for finding the nearest-neighbors of a point (or a set of points) in a grid of spatial points. This can be useful when trying to interpolate values on a grid where the x and y spacings are different. An example of its usage is provided [here](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.query.html#scipy.spatial.KDTree.query).

+ Earle showed us a couple ways to debug code in ipython. First, there is the magic command `%debug`, which launches a post-mortem debugging session after an exception is thrown. That is, if a script crashes, `%debug` activates the [python debugger (pbd)](https://docs.python.org/2/library/pdb.html) at the line *before* the error occurred. A pdb session is similar to the MATLAB debugger session. Another alternative is the [Tracer](http://ipython.org/ipython-doc/dev/api/generated/IPython.core.debugger.html#classes) object from the `IPython.core.debugger` module. The Tracer object can be used to activate a pdb session anywhere in your code. Once in pdb, you can use the command line to explore the code and set new breakpoints. Therefore, you can essentially use it as breakpoint. For example:

		:::python	
		
		from IPython.core.debugger import Tracer
		debug_here = Tracer()
	
		#later in code
		debug_here() #code stops here and pdb is launched.
   	 	

+ We briefly talked about keyword arguments and the different ways we can supply inputs to a function. Most of what we discussed is covered in [Section 4.7](https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments) on this python doc page. With keyword arguments, we can specify function arguments in any order, provided the right keyword is used. Keyword arguments are particularly useful for setting [default argument values](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values). Here is an example:

		:::python
		
		def fun(x,y, a=10, b=12)
			#statements
			#statements
		
		#some good ways to call the function
		fun(2,3) 
		fun(1, 5, a=20) 
		fun(2, 5, 12, 5) #a=12, b=5
		fun(x=2, y=10) #using x and y as keywords
		fun(b=50, x=10, a=-20, y=0) #order of keyword arguments does not matter
		
		#bad ways to call the function
		fun(2) #need at least two arguments
		fun(5,10,c=10) #c is not a defined keyword
		fun(2,4) #if you intend x=2 and y=4


	





