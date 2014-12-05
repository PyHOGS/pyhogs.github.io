Title: Intro to the netCDF4 module
Slug: into_netcdf4
Date: 2014-12-04 12:25 UTC-07:00
Authors: Earle Wilson
Tags: netCDF, netCDF4
Summary: A quick intro to the netCDF4 module


## What is NetCDF?

[NetCDF](http://www.unidata.ucar.edu/software/netcdf/) stands for Network Common Data Format and refers to a "set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data". The software is maintained by developers at [Unidata](http://www.unidata.ucar.edu/software/netcdf/), which is a subsidary of [UCAR](http://www2.ucar.edu/). 

NetCDF offers many tools to handle large, complex datasets. For this reason, netCDF is now widely used within the geoscience community. 

## Using NetCDF in Python

There are three main versions of NetCDF currently in use: *netCDF-classic*, *netCDF 64-bit* and *netCDF-4*. As you might expect, each version comes in different flavors as well. netCDF-classic is the original format and probably the most commonly used version. It's main limitation is that it can only store up 2 gigabits of data. netCDF 64-bit is basically netCDF-classic with a much larger data capacity. netCDF-4 is the latest generation netCDF data format. It combines the data storage capabilities of netCDF 64-bit with some enhanced features from [HDF5](http://docs.h5py.org/en/2.3/) data format. You can learn more each version [here](https://www.unidata.ucar.edu/software/netcdf/docs/netcdf-tutorial/Versions.html).  

The scipy package includes a [scipy.io.netcdf](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.io.netcdf.netcdf_file.html) module to read and create netCDF files, but it can only work with the netCDF-classic files. The netCDF4 module can handle all netCDF versions, so I will focus on the netCDF4 module from here on.

The netCDF4 module is available from the [Python Package Index (PyPi)](https://pypi.python.org/pypi). You can install it by typing `pip install netCDF4` from a terminal shell. If you are using Python distribution such as Anaconda or Canopy, you may already have netCDF4 installed. 


## Storing data in a netCDF dataset

To create and store data in a netCDF file, you need to do the follow steps:

1. Open/create a netCDF dataset.
2. Define the dimensions of the data.
3. Construct variable objects using the previously defined dimensions.
4. Pass data into the netCDF variables.
5. Add attributes to the variables (optional but recommended).
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

Here, I created a numpy array representing fake temperature data for some latitude, longitude at several different of depth levels. The shape of the data array is (28,22,20) representing (lon, lat, z). For concreteness, let's assume that this represents data for one day.


#### Creating a dataset
To create a netCDF dataset, you use the `Dataset` method:

    :::python
    import netCDF4 as nc4

	f = nc4.Dataset('sample.nc','w', format='NETCDF4') #'w' stands for write

The above line creates a netCDF file called "sample.nc" in your current folder. `f` is a netCDF Dataset object that provides methods for storing data to the file. `f` also doubles as your *root group*. A netCDF group is basically a directory or folder within the netCDF dataset. This allows you to organize data as you would in a unix file system. Let's create a group for the heck of it:

	:::python
	tempgrp = f.createGroup('Temp_data')


#### Specifying dimensions

The next step is to specify the **dimensions** that describe the data. In this example, the dimensions are spatial and temporal:

	:::python
	tempgrp.createDimension('lon', len(lon))
	tempgrp.createDimension('lat', len(lat))
	tempgrp.createDimension('z', len(z))
	tempgrp.createDimension('time', None)

The first argument for the `createDimension` method is a string specifying the name of the dimension. The second argument is an integer that specifies the dimension's length. In the last line, by using `None`, I have made `time` an *unlimited* dimension. By making the time dimension unlimited, I can append data to that dimension indefinitely. This is in anticipation of receiving more data in the future. The netCDF-4 format permits multiple unlimited dimensions, but older versions allow only one.

#### Building variables
Next, I create netCDF **variables** using the dimensions I just created:

	:::python
	
    longitude = tempgrp.createVariable('Longitude', 'f4', 'lon')
    latitude = tempgrp.createVariable('Latitude', 'f4', 'lat')	
	levels = tempgrp.createVariable('Levels', 'i4', 'z')
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'))
	time = tempgrp.createVariable('Time', 'i4', 'time')
	
This step essentially pre-allocates variables for data storage. The first argument is the name of the variable, the second argument sets the [datatype](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)[^1] and the third argument sets the shape. The shape of the variable is specified using the dimension names that were previously defined.  To create a scalar variable, one would omit the third argument.

Let's look at what we have done so far,

{% notebook examples/intro-netcdf4-module.ipynb cells[14:16]%}

By using the print function[^2], one can get information about a dataset or group. It's worth noting that **netCDF dimensions and variables are indestructible**. That is, there is no method to delete a variable or dimension once they are created; you may modify the contents of a variable but you can't get rid off the variable all together.

#### Passing data into variables

This step is easy. One simply uses the varibles instance created earlier to pass in the data:

	:::python
	longitude[:] = lon
	latitude[:] = lat
	levels[:] = z
	temp[0,:,:,:] = temp_data
	
	#get time in days since Jan 01,01
	from datetime import datetime
	today = datetime.today()
	time_num = today.toordinal()
	time[0] = time_num

The "[:]" at the end of the variable instance is necessary. The important thing here is to use proper indexing when assigning data to variables - just like you would a numpy array.

#### Adding attributes

NetCDF attributes can be used to provide additional information about the dataset (i.e. metadata). You can add attributes to variables, groups and the dataset itself. This is also simple:

	:::python
	#Add global attributes
	f.description = "Example dataset containing one group"
	f.history = "Created " + today.strftime("%d/%m/%y")
	
	#Add local attributes to variable instances
	longitude.units = 'degrees east'
	latitude.units = 'degrees north'
	time.units = 'days since Jan 01, 0001'
	temp.units = 'degrees K'
	levels.units = 'meters'
	temp.warning = 'This data is not real!'

Adding attributes is optional but considered good practice. 

#### Closing the dataset

	:::python	
	f.close()

This is an important step as it completes the data writing process and permanently saves the data to disk.


## Reading a netCDF dataset

To open in a netCDF file, you again use the Dataset method:

	:::python
	f = nc4.Dataset('sample.nc','r')
	tempgrp = f.groups['Temp_data']

If you didn't create the dataset, the first thing you might want to do find out what's in it. The print function comes in handy here (if the data is in netCDF4 format):

{% notebook examples/intro-netcdf4-module.ipynb cells[23:24]%}

Alternatively, you can query for a list of the variables:

{% notebook examples/intro-netcdf4-module.ipynb cells[24:25]%}	

As evidenced by the use of the `keys()` method, netCDF variables are stored in a dictionary. Here is how you would read the data stored in 'levels' into a new numpy array:

	:::python
	zlvls = tempgrp.variables['Levels'][:]

Again, '[:]' at the end is necessary. Even though I have opened the dataset, I have yet not loaded its contents into memory. **The really cool thing about netCDF files is that you can read in a subset of a dataset.**  This is hugely advantageous when working with large datasets. So if I only want the wanted temperature data from the first depth level, I would do:

	:::python
	temp_0z = tempgrp.variables['Temperature'][0,:,:,0]

You can slice into the netCDF variable as you would a numpy array. 

## Other neat features
#### Data compression
NetCDF4 provides easy methods to compress data. Back when we created the variables, we could have turned on the compression using `zlib=True` keyword argument:

	:::python
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True)

The `complevel` keyword argument toggles the compression ratio and speed. Options range from 1 to 9 (1 being the fastest but with the least compression and 9 being the slowest but with the most compression. Default is 4). Additionally, you can also specify the precision of your data using the `least_significant_digit` keyword argument. Floats are generally stored with higher precision than the data it represents. Let's look at a value from the temperature data we created:

{% notebook examples/intro-netcdf4-module.ipynb cells[27:28]%}	

Those trailing digits take up a lot of space and in most cases serve no practical value. By specifying the least significant digit, you can further enhance the data compression. Knowing that temperature is only accurate to about 0.005 degrees K, I can chose to keep 4 significant digits.

	:::python
	temp = tempgrp.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True, least_significant_digit=4)
	
Recreating the dataset using the above line instead of the one I used earlier results in file size reduction from 4.8MB to 4.3MB. In this case, I didn't save much space, but using these same compression options on large datasets can result in huge file size reductions[^3]. For more info, visit the [official docs](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html).

#### Multi-file dataset
The MFDataset class provides a method to read in multiple data files at once. This is only available for NETCDF3_64BIT, NETCDF3_CLASSIC or NETCDF4_CLASSIC formats. If I have multiple files that have the same variable and the same unlimited dimension, I can read them in simultaneous using MFDataset. See the [official docs](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html) for a nice example.

##References (and futher reading)
* [http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
* [http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf](http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf)





[^1]: According to the [official netCDF4 documentation](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html): Valid datatype specifiers include: 'f4' (32-bit floating point), 'f8' (64-bit floating point), 'i4' (32-bit signed integer), 'i2' (16-bit signed integer), 'i8' (64-bit singed integer), 'i1' (8-bit signed integer), 'u1' (8-bit unsigned integer), 'u2' (16-bit unsigned integer), 'u4' (32-bit unsigned integer), 'u8' (64-bit unsigned integer), or 'S1' (single-character string). The old Numeric single-character typecodes ('f','d','h', 's','b','B','c','i','l'), corresponding to ('f4','f8','i2','i2','i1','i1','S1','i4','i4'), will also work.

[^2]: Apparently, this only works for the netCDF4 format.

[^3]: I once reduced a ~48MB data set to only 9MB!










