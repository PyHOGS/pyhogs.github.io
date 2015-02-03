Title: Python Hour - 02 February 2015
Slug: python-hour-2015-02-02
Date: 2015-02-02 12:00 UTC-07:00
tags: power spectra, matrix operations, broadcasting rules
Summary: Built-in functions to compute power spectral density, numpy broadcasting rules versus matrix operations.
Author: Earle Wilson


##Summary

####Methods for computing frequency power spectra
Earle asked about built-in Python functions to compute power spectra. JPaul recommended the [psd()](http://matplotlib.org/api/mlab_api.html#matplotlib.mlab.psd) function, from the mlab module, which estimates the power spectral density of a time series using the [Welch's average periodogram method](http://en.wikipedia.org/wiki/Welch%27s_method). The function uses a Hamming window to split a time series into segments, then averages the power spectrum for each segment to obtain a power spectral density estimate for the full timeseries. By splitting the original time series into smaller segements, we get more degrees of freedom for our spectral estimate. The `psd()` function is somewhat equivalent to MATLAB's [pwelch](http://www.mathworks.com/help/signal/ref/pwelch.html) function. 

As a side note, the [fftpack documentation](http://docs.scipy.org/doc/scipy-dev/reference/tutorial/fftpack.html#id8) has some for examples for computing power spectra using the fast fourier transform. 

####The climate variability diagnostics package
The subject of empirical orthogonal functions came up and Parker introduced us to the [climate variability diagnostics package (CVDP)](http://www2.cesm.ucar.edu/working-groups/cvcwg/cvdp). The website provides statistical analyses of archived CMIP5 model runs. In particular, the website features dozens, if not hundreds, of plots comparing the EOFs and PCs of various output fields with actual data. The results are impressive and disheartening all at the same time. 


####Array versus matrix operations in Numpy
We also discussed the differences between how MATLAB and Python treat array multplication. In general, operations involving Numpy arrays are element-wise and are subject to [broadcasting rules](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html). Broadcasting rules determine if/how arrays can be "expanded" to perform element-wise operations. For example, a 1x4 dimensional Numpy array multiplied by a 4x1 array gives a 4x4 array. In contrast, MATLAB treats 2-D arrays as matrixes and interpets `A*B` to mean the inner-product of `A` and `B`. So, in MATLAB, a 1x4 array "multiplied" by a 4*1 array yields a scalar value.
	
In essence, `A*B` in Numpy is similar to `A.*B` in MATLAB except that Numpy is more flexible in accepting arrays of different shapes, provided they are compatible via the Numpy broadcasting rules. For example:

	:::python	
	data = np.random.rand(12,40,50) #(t, x, y)
	data_tmean = data.mean(axis=0) #data_tmean.shape = (40,50)
	data_anom = data - data_tmean #no need to expand data_tmean to match the shape of data
 
To carry out matrix operations in Python, the best solution is to use numpy matrices. The `numpy.matrix()` converts numpy arrays into numpy matrices. Another alternative is to use the `np.dot()` function to take the inner product of two 2-D arrays.





