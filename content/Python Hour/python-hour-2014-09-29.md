Title: Python Hour - 29 September 2014
slug: python-hour-2014-08-29
date: 2014-09-29 12:00 UTC-07:00
tags: netcdf, sets
summary: We discussed issues that can arise when creating netcdf files and some nuances of using Python sets.
authors: Earle Wilson


+ Parker brought our attention to a programming book called [Introduction to Computation and Programming Using Python](http://mitpress.mit.edu/books/introduction-computation-and-programming-using-python), by John Guttag. The book is based on a course offered on MIT's OpenCourseWare.

+ We spent the some time talking about what happens when you try to create a netcdf file that already exists. By default, when you open a netcdf dataset with `mode='w'` (i.e., in writing mode) it should over-write any existing file. You can change this behavior with the "clobber" keyword option, which can raise an exception if the file already exists:

		:::python
		import netCDF4 as nc
		
		#create new netcdf file and over-write any pre-existing file with same name
		h = nc.Dataset('filename.nc', mode='w') 
		
		#create new netcdf file but throw an error if the file already exists
		h = nc.Dataset('filename.nc', mode='w', clobber=False)
		

+ We also learned that it is possible extract a subset of a netcdf file stored on a remote [THREDDS](http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html) data server WITHOUT downloading the entire file. You simply supply the url path to the netcdf file and extract data as you would normally.

+ Jim spoke about some of the advantages and disadvantages of using a Python set. A Python [set](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset) is an unordered collection of unique objects. This is in contrast to a Python list, which is an ordered sequence of objects that may contain duplicates. One advantage of using a set over a list is that a set is substantially faster at determining if an object is in it. For example, performing `if x in set` is generally faster than doing `if x in list`. One disadvantage of using sets is that they have no intrinsic order:

		:::python
		s = set("aoihf")	
		for n in s:
		    print n	
		#output: 
		a i f o h
 
 This will cause problems if you are iterating over a set and the order in which the set's items are accessed is important.




