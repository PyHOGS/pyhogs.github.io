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


 
+ Parker also told us about the [`KDTree`](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html) class from the `scipy.spatial` module. KDTree provides efficient methods, e.g. `KDtree.query`, for finding the nearest-neighbors of a point (or a set of points) in a grid of spatial points. This can be useful when trying to interpolate values on a grid where the x and y spacings are different. An example of its usage [here](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.query.html#scipy.spatial.KDTree.query).

+ Earle showed us some of the code debugging tools available in ipython. First, there is the magic command `%debug`, which launches a post-mortem debugging session after an exception is thrown. That is, if a script crashes, `%debug` launches a [python debugger (pbd)](https://docs.python.org/2/library/pdb.html) session at the line *before* the error occurred. Another alternative is the [Tracer](http://ipython.org/ipython-doc/dev/api/generated/IPython.core.debugger.html#classes) object from the `IPython.core.debugger` module. The Tracer object can be used to activate a pdb session anywhere in your code. Example:

		:::python	
		
		from IPython.core.debugger import Tracer
		debug_here = Tracer()
	
		#later in code
		debug_here() #code stops here and pdb is launched.
   	 	

+ We briefly talked keyword arguments in functions and how they differ from positional arguments. With positional arguments, the order of the inputs is important. Keyword arguments, on the other hand, can be specified in any order, provided we use the right keyword. Keyword arguments are especially useful for setting [default argument values](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values). For example, in `def fun(x, y=10)`, `y` is a keyword argument and has a default of 10. When calling the function, we have the option of changing this value. Most of what we discussed is covered in [Section 4.7](https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments) on the python doc page.





