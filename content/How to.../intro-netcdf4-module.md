Title: Create and read netCDF files
Slug: intro_netcdf4
Date: 2014-12-04 12:25 UTC-07:00
Authors: Earle Wilson
Tags: netCDF, netCDF4
Summary: An introduction to netCDF and the netCDF4 python module. 

## What is netCDF?

[NetCDF](http://www.unidata.ucar.edu/software/netcdf/) is a data storage format commonly used within the geoscience community. The acronym stands for Network Common Data Format and it refers to a "set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data"[^0].The software is maintained by developers at [Unidata](http://www.unidata.ucar.edu/software/netcdf/), which is a subsidary of [UCAR](http://www2.ucar.edu/). 

One of the main advantages of using NetCDF is that it has a built-in hierarchical structure that facilitates better organization and documentation of data. It is well suited to handle large numerical datasets as it allows users to access portions of a dataset without loading its entirety into memory. 

## Versions of netCDF 

There are several [versions](https://www.unidata.ucar.edu/software/netcdf/docs/netcdf-tutorial/Versions.html) of NetCDF currently in use: *netCDF3_classic*, *netCDF3_64-bit* and *netCDF4_classic* and *netCDF4*. NetCDF3_classic uses the original netCDF binary format and has been in use for the past 20 years. It is probably still the most common NetCDF version despite being superseded by more recent versions. Its main limitation is that it can only store up 2GB of data. This limitation was lifted with the release of NetCDF3_64-bit. NetCDF4 is the most recent version and represents a departure for the the classic netCDF format. It is built on top of the [HDF5](http://docs.h5py.org/en/2.3/) data structure, which allows for the creation of groups that give users more freedom to organize their data. Like its predecesor, NetCDF4 can also handle files that take up more than 2GB of disc space.

## Using netCDF in Python
The traditional python interface for netCDF is the [scipy.io.netcdf](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.io.netcdf.netcdf_file.html) module. This module is able to read and create netCDF files, but does not support the newer netCDF4 format. The [netCDF4 python module](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html) supports all current netCDF versions and will be the focus of this post.

The netCDF4 module is available from the [Python Package Index (PyPi)](https://pypi.python.org/pypi). You can install it by typing `pip install netCDF4` from a terminal shell. If you are using Python distribution such as Anaconda or Canopy, you may already have netCDF4 installed. 


## Storing data in a netCDF dataset

Here is how you would normally create and store data in a netCDF file:

1. Open/create a netCDF dataset.
2. Define the dimensions of the data.
3. Construct netCDF variables using the defined dimensions.
4. Pass data into the netCDF variables.
5. Add attributes to the variables and dataset (optional but recommended).
6. Close the netCDF dataset.

Each step is discussed below. But first, let's make up some data:

	:::python
	import numpy as np

	lon = np.arange(45,101,2)
	lat = np.arange(-30,25,2.5)
	z = np.arange(0,200,10)
	x = np.random.randint(10,25, size=(len(lon), len(lat), len(z)))
	noise = np.random.rand(len(lon), len(lat), len(z))
	temp_data = x+noise

Here, I create a numpy array representing fake temperature data for some latitude, longitude at several depth levels. The shape of the data array is (28,22,20) representing (lon, lat, z). For concreteness, let's assume that this data represents one snapshot in time.


#### Creating a dataset
To create a **netCDF dataset**, you use the `Dataset` method:

    :::python
    import netCDF4 as nc4

	f = nc4.Dataset('sample.nc','w', format='NETCDF4') #'w' stands for write

The above line creates a netCDF file called "sample.nc" in the current folder. `f` is a netCDF Dataset object that provides methods for storing data to the file. `f` also doubles as the *root group*. A netCDF group is basically a directory or folder within the netCDF dataset. This allows you to organize data as you would in a unix file system. Let's create a group for the heck of it:

	:::python
	tempgrp = f.createGroup('Temp_data')


#### Specifying dimensions

The next step is to specify the **dimensions** of the data. If you plan to save a multidimensional array of data, each dimension of that array needs to be given a name and a length:

	:::python
	tempgrp.createDimension('lon', len(lon))
	tempgrp.createDimension('lat', len(lat))
	tempgrp.createDimension('z', len(z))
	tempgrp.createDimension('time', None)

The first and second arguments of the `createDimension` method are the dimension's name and length, respectively. In the last line, I added created time a dimension. This gives me the option of constructing a four dimensional array with time as the extra dimension. By using `None` as the second argument, I have made `time` an *unlimited* dimension. An unlimited dimension is one that can grow indefinitely; the other dimensions, with their specified lengths, are locked into their current size. The netCDF4 format permits multiple unlimited dimensions, but older formats allow only one.

#### Building variables
This step essentially pre-allocates NetCDF **variables** for data storage. NetCDF variables are very similar to numpy arrays. To construct them, you use the `createVariable` method:

	:::python
	
    longitude = tempgrp.createVariable('Longitude', 'f4', 'lon')
    latitude = tempgrp.createVariable('Latitude', 'f4', 'lat')	
	levels = tempgrp.createVariable('Levels', 'i4', 'z')
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'))
	time = tempgrp.createVariable('Time', 'i4', 'time')
	
The first argument supplies the name of the variable, the second argument sets the [datatype](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html) and the third argument sets the shape. "f4" specifies a 32 bit float and "i4" represents a 32 bit integer[^1]. The shapes of the variables are specified using the dimension names.  To create a scalar variable, one would omit the third argument.

Let's look at what we have done so far[^2],

{% notebook examples/intro-netcdf4-module.ipynb cells[14:16]%}

Note that all the dimensions and variables were defined for `tempgrp`. The root group `f` has no variables.  It's also worth noting that **netCDF dimensions and variables are indestructible**. That is, there is no method to delete a variable or dimension once they are created; you may modify the contents of a variable but you can't get rid off the variable all together. 


#### Passing data into variables

Here, you simply pass your data into the variables you just created:

	:::python
	longitude[:] = lon #The "[:]" at the end of the variable instance is necessary
	latitude[:] = lat
	levels[:] = z
	temp[0,:,:,:] = temp_data
	
	#get time in days since Jan 01,01
	from datetime import datetime
	today = datetime.today()
	time_num = today.toordinal()
	time[0] = time_num

The important thing here is to use proper indexing when passing values into the variables - just like you would a numpy array.

#### Adding attributes

NetCDF attributes can be used to provide additional information about the dataset (i.e. metadata). You can add attributes to variables, groups and the dataset itself. This is optional but considered good practice:

	:::python
	#Add global attributes
	f.description = "Example dataset containing one group"
	f.history = "Created " + today.strftime("%d/%m/%y")
	
	#Add local attributes to variable instances
	longitude.units = 'degrees east'
	latitude.units = 'degrees north'
	time.units = 'days since Jan 01, 0001'
	temp.units = 'Kelvin'
	levels.units = 'meters'
	temp.warning = 'This data is not real!'

You can add attributes any way you see fit, but you should be aware of the different [attribute conventions](http://www.unidata.ucar.edu/software/netcdf/conventions.html) that already exist. Most notable are the [COARDS](http://ferret.wrc.noaa.gov/noaa_coop/coop_cdf_profile.html) and [Climate Forecast (CF)](http://cfconventions.org/) conventions. Even if you choose not to conform to any existing standard, I highly recommend creating a convenient and consistent naming system for yourself. For example, I ensure that all my variables have `units` and `long_name` attributes.


#### Closing the dataset

	:::python	
	f.close()

This final step is important as it completes the data writing process and permanently saves the data to disk.


## Reading a netCDF dataset

To open in a netCDF file, you again use the Dataset method:

	:::python
	f = nc4.Dataset('sample.nc','r')
	tempgrp = f.groups['Temp_data']

Here I read in the dataset I created earlier. If you didn't create the dataset, the first thing you might want to do find out what's in it. The print function comes in handy here (if the data is in netCDF4 format):

{% notebook examples/intro-netcdf4-module.ipynb cells[23:24]%}

Alternatively, you can query for a list of the variables:

{% notebook examples/intro-netcdf4-module.ipynb cells[24:25]%}	

As evidenced by the use of the `keys()` method, netCDF variables are stored in a dictionary. If inquire the attributes of a variable, you can do:

{% notebook examples/intro-netcdf4-module.ipynb cells[25:26]%}	

If a variable has many attributes, you can use a simple loop to display all its metadata:

{% notebook examples/intro-netcdf4-module.ipynb cells[26:27]%}

Accessing data from a variable is simple. Below, I read in the data stored in 'levels' into a new numpy array:

	:::python
	zlvls = tempgrp.variables['Levels'][:]

Again, the '[:]' at the end is necessary. Even though I have opened the dataset, I have not yet loaded its contents into memory. **The really cool thing about netCDF files is that you can read in a subset of a dataset.**  This is hugely advantageous when working with large datasets. So if I only want the wanted temperature data from the first depth level, I would do:

	:::python
	temp_0z = tempgrp.variables['Temperature'][0,:,:,0]

You can slice into the netCDF variable as you would a numpy array. 

## Other neat features
#### Data compression
NetCDF4 provides easy methods to compress data. Back when I created the variables, I could have turned on data compression by setting the keyword argument `zlib=True`:

	:::python
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True)

The `complevel` keyword argument toggles the compression ratio and speed. Options range from 1 to 9 (1 being the fastest with least compression and 9 being the slowest with most compression. Default is 4). Additionally, you may also specify the precision of your data using the `least_significant_digit` keyword argument. Floats are generally stored with much higher precision than the data it represents. Let's look at a value from the temperature data array:

{% notebook examples/intro-netcdf4-module.ipynb cells[29:30]%}	

Those trailing digits take up a lot of space and in most cases serve no practical value. By specifying the least significant digit, you can further enhance the data compression. This just gives netCDF more freedom when it packs the data into your harddrive. Knowing that temperature is only accurate to about 0.005 degrees K, it makes sense to just preserve the first 4 digits:

	:::python
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True, least_significant_digit=4)
	
Recreating the dataset using the above line, instead of the one I used earlier, results in file size reduction from 4.8MB to 4.3MB. In this case, I didn't save much space, but using these same compression techniques on large datasets can result in dramatic size reductions[^3]. For more info, visit the [official docs](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html).

#### Multi-file dataset
If you have multiple files that have the same variable and the same unlimited dimension, you can read them in simultaneous using `MFDataset`. This is only available for NETCDF3_64BIT, NETCDF3_CLASSIC or NETCDF4_CLASSIC formats.  This is a neat feature but I've encountered problems when I try to open too many files at once. For my computer, the upper limit seems to be a couple hundred files. 

See the [official docs](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html) for a nice example of how to use `MFDataset`.

##References (and futher reading)
* [Official Documention](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html). The official doc offers more examples and introduces other features that I did not mention here.  
* [http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf](http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf)



[^0]: [http://www.unidata.ucar.edu/software/netcdf/](http://www.unidata.ucar.edu/software/netcdf/)

[^1]: From the [official netCDF4 documentation](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html): Valid datatype specifiers include: 'f4' (32-bit floating point), 'f8' (64-bit floating point), 'i4' (32-bit signed integer), 'i2' (16-bit signed integer), 'i8' (64-bit singed integer), 'i1' (8-bit signed integer), 'u1' (8-bit unsigned integer), 'u2' (16-bit unsigned integer), 'u4' (32-bit unsigned integer), 'u8' (64-bit unsigned integer), or 'S1' (single-character string). The old Numeric single-character typecodes ('f','d','h', 's','b','B','c','i','l'), corresponding to ('f4','f8','i2','i2','i1','i1','S1','i4','i4'), will also work.

[^2]: Apparently, the print function only displays metadata is the dataset is in the netCDF4 format.

[^3]: I once reduced a ~48MB data set to only 9MB!










