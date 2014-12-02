Title: Python Hour - 11 August 2014
slug: python-hour-2014-08-11
date: 2014-08-11 12:00 UTC-07:00
tags: x-ray, pickle, axes, git
summary: Setting plot aspect ratios, saving data to your hard drive and much more...
author: Earle Wilson

+ **Cim mentioned there is a Python toolbox called [x-ray](https://pypi.python.org/pypi/xray/0.1.0) (short for eXtended arRAYs) that is designed to make working with multi-dimensional datasets a lot easier.** `xray` allows you to add dimension names and coordinate values to numpy ndarrays. You can then use those dimension names and coordinate values to perform operations over the array. For example, with `xray`, you can find the time mean of an array by doing something like `x.sum('time')` - rather than `x.sum(axis=0)`, if time was on the first dimension.


+ **Jake asked about how to set the x-y aspect ratio of a plot.** We talked about many ways of doing this. The easiest solution is probably to use the `axes` method `set_aspect`. An minimal working example is provided [here](plot-aspect-ratio).


+ **Earle talked about different ways of saving Python data to file.** Several options were mentioned; for e.g. (most) data can be saved as `.mat`, `netcdf` or `HDF` files. However, the standard way of saving Python objects to file is to use the [pickle](https://docs.python.org/2/library/pickle.html#data-stream-format) module. The syntax for saving objects using pickle is `pickle.dump(obj,file,protocol)`. You can find examples of how to use pickle [here](http://earlew.github.io/Reading-and-writing-data/index.html#Reading-and-saving-data-using-Pickle). By default, `pickle.dump(...)` tries to save data in a human-readable format. This is ok for small, simple objects but saving large n-dimensional arrays this way is very slow and results in files that take up a lot of disk space. The `protocol` parameter allows users to change this behaviour. Setting `protocol = pickle.HIGHEST_PROTOCOL` or `protocol = -1`, tells pickle to use the fastest, most memory efficient option available. By using the highest protocol, you can save files that take up as much space as a `netcdf` or `.mat` file containing the same data. 



+ **Earle briefly showed how to make a plot with broken axes**. An example is given [here](broken-axes).


+ **We had a pretty lengthy discussion about version control software** - git, in particular. JPaul brought up the [git rebase](http://git-scm.com/book/en/Git-Branching-Rebasing) command and showed how it can be useful when pushing changes to a group repository. We also tried to understand the difference between `git checkout` and `git reset`. Cim mentioned that [bitbucket](https://bitbucket.org/) is an alternative to github and offers free, online private repositories.


+ Jake says that PyHOG (PYthon Hour for Oceanographers and Geoscientists) sounds a lot better than GeoPUG (Geoscience Python User Group). So, PyHOG it is...
