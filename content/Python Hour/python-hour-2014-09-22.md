Title: Python Hour - 22 September 2014
slug: python-hour-2014-08-22
date: 2014-09-22 12:00 UTC-07:00
tags: optimal interpolation, strings
summary: Summary of PyHOGs meeting on September 22, 2014
authors: Jesse Anderson, Earle Wilson

+ Earle gave a demo on objective mapping. He plans to clean up the code and share it with the group.

Other things that came up while discussing objective mapping:

+ kriging and its similarities to optimal interpolation.

+ Nearest value assignment as opposed to interpolation.

+ Raw strings. These are strings that are interpreted literally, so they don't require extra backslashes to escape special characters. They come in handy when plotting text labels with LaTeX symbols. To create a raw string, you simply add `r` before the first quote. E.g. `units = r'Temperature ($^{\circ}$C)'`.

+ The `curve_fit` function. `curve_fit`, which is a function from the `scipy.optimize` module. `curve_fit` uses non-linear least squares to fit a function to data. You need to supply good first guesses to ensure that `curve_fit` converges on reasonable solutions.

+ `np.linalg.lstsq` and `np.linalg.solve`. These are a couple options for solving a system of equations in Python. This brought up the [LAPACK](http://www.netlib.org/lapack/#_presentation) and BLAS software libraries. These are old FORTRAN codes, which form the basis of most linear algebra algorithms in use today. 

+ Different ways to close figures:

		:::python 
		plt.close('all')
		plt.close(h) #h is figure handle or instance
