Title: Python Hour - 1 December 2014
Slug: python-hour-2014-12-01
Date: 2014-12-01 12:00 UTC-07:00
Tags: 2-D interpolation, command line
Summary: Bilinear interpolation and parsing command-line arguments
Author: JP Rinehimer

## Bilinear interpolation
Parker showed his results of bilinear interpolation to interpolate data from
one plaid grid to another. Here's the resulting code:

*(from the comments to [last weeks meeting](python-hour-2014-11-24)):*

    :::python
        # add velocity vectors
        # get velocity
        u = ds.variables['u'][0, -1, :, :].squeeze()
        v = ds.variables['v'][0, -1, :, :].squeeze()
        # set masked values to 0
        ud = u.data; ud[G['mask_u']==False] = 0
        vd = v.data; vd[G['mask_v']==False] = 0
        # create interpolant
        import scipy.interpolate as intp
        ui = intp.interp2d(G['lon_u'][0, :], G['lat_u'][:, 0], ud)
        vi = intp.interp2d(G['lon_v'][0, :], G['lat_v'][:, 0], vd)
        # create regular grid
        import numpy as np
        aa = ax.axis()
        daax = aa[1] - aa[0]
        daay = aa[3] - aa[2]
        axrat = np.cos(np.deg2rad(aa[2])) * daax / daay
        nngrid = 80
        x = np.linspace(aa[0], aa[1], round(nngrid * axrat))
        y = np.linspace(aa[2], aa[3], nngrid)
        xx, yy = np.meshgrid(x, y)
        # interpolate to regular grid
        uu = ui(x, y)
        vv = vi(x, y)
        mask = uu != 0
        # plot velocity vectors
        xt, yt = zfun.labxy(ax, 'lr')
        scl = 3
        ax.quiver(xx[mask], yy[mask], uu[mask], vv[mask], units='y', scale=scl, scale_units='y', color='k')

## Running Python scripts from the command line

Parker described a workflow from a daily fore/now-casting model run. A series
of cron-jobs collects data from various sources, processes the data via legacy
Matlab scripts, runs the model, and uses Python to create some visualizations.
This lead to a discussion of running Python (and Matlab) from the command line.

To run a Python script from the command line:

    $python myscript.py  # Runs file named myscript.py

You can also make the script itself executable so that you don't need to
directly invoke the `python` executable. To do so, the very first line of the
file needs to be a "she-bang (`#!`) line":

    :::python
    #!/usr/bin/env python  # Python 2
    OR:
    #!/usr/bin/env python3  # Python 3

If this line starts your script, the shell knows to execute it through python.
You also have to make the file *executable* using `chmod`:

    chmod +x myscript.py

You can then run it like any other program just by typing it's name:

    ./myscript.py

The `./` is needed if the script is not in a directory of your `$PATH`
environment variable. If you move or copy your script to a location in your
`$PATH` you can run it from anywhere on your system just by typing the file
name.

## Command line arguments in Python

In the workflow described above, the scripts are written in 3 different
languages (shell, Matlab, and Python) and need a way to talk to each other.
While Matlab scripts can be run from the command line, they cannot take command
line arguments (although there are [ways around this using the `/r`
flag](http://www.mathworks.com/matlabcentral/answers/97204-how-can-i-pass-input-
parameters-when-running-matlab-in-batch-mode-in-windows)). Because of this,
Parker was sharing parameters, such as the date to start the model, between the
various scripts using temporary text files.

While workable, this method is awkward and mostly unnecessary in Python because
Python can accept command-line arguments, like most executables in Linux-based
systems. While terminology varies, arguments can be split into two broad
categories (which loosely correspond to Python's positional and keyword
function arguments):

* **positional arguments** where the argument order determines its function.
  Common examples include filenames in commands like `cp src dest` where the
  first argument is the file to copy and the second is its destination.

* **flags** which are specified following a single or double dash and can
  generally be in any order. Flags come in two varieties: *stand-alone*, which
  do not require any additional arguments, and flags which must be followed by
  one (or more) arguments. Flags often have both short and long forms which are
  equivalent. The short form is usually specified by a single dash `-` and a
  letter and the long form has two dashes `--` and a word. Many programs allow
  short form flags to be strung together like `ls -lat` which is equivalent to
  `ls -l -a -t`. While their use depends on the program, common flags include
  things like `-v` or `--verbose` for more information from programs, `-h` or
  `--help` for help, `-a` or `--all` for listing all occurrences, and `-r` or
  `--recursive` for recursive functionality.

Depending on your needs, you can include command-line arguments in your scripts
through either [`sys.argv`](https://docs.python.org/2/library/sys.html) or
[`argparse`](https://docs.python.org/3/library/argparse.html). Other modules
include
[`optparse`](https://docs.python.org/3.1/library/optparse.html?highlight=optpars
e#module-optparse) and
[`getopt'](https://docs.python.org/3.1/library/getopt.html) although these have
for the most part been superseded by the `argparse` module. All are available
in the Python Standard library.

### sys.argv
The `sys` module provides simple, string-based argument parsing through the
`argv` parameter. Command line arguments are passed to the function as
space-separated strings and are accessible through the list `sys.argv`. The
first element in this list is always the script name. No parsing or type
conversion is performed. This method should be used for simple scripts where
interpretation of the arguments is straightforward.

The example below is also in [our repository](https://github.com/PyHOGS/pyhogs.github.io/blob/pelican-source/pyhogs-code/example-scripts/sys_argv_example.py).

    #!/usr/bin/env/python
    from __future__ import print_function
    import sys
    
    # Get the total number of arguments
    total = len(sys.argv) - 1 # Subtract 1 for the script name
    
    # Print it
    print("{:d} arguments passed to the script".format(total))
    for i, a in enumerate(sys.argv):
        print("Argument #{:d}: {} ".format(i, a))

For example, this returns:

    $python sys_argv_example.py hello my name is foo bar
    7 arguments passed to the script
    Argument #0: sys_argv_example.py
    Argument #1: hello
    Argument #2: my
    Argument #3: name
    Argument #4: is
    Argument #5: foo
    Argument #6: bar
    

### argparse

[`argparse`](https://docs.python.org/3/library/argparse.html) is a fully
featured module for command-line argument parsing. It can interpret both
positional arguments and flags, understand long- and short-form flags,
automatically generate help text, do type conversion, set default values, and
understand subcommands commonly used in programs like `git` and `svn`.

Using `argparse` is more complicated that `sys.argv`, but it allows you to
incorporate full-featured argument parsing seen in most Linux programs using a
very minimal amount of code. Follow these steps to use the module:

1. Create a parser object from the [`argparse.ArgumentParser`](https://docs.python.org/2.7/library/argparse.html#argparse.ArgumentParser) class.
2. Add various arguments using the `ArgumentParser.add_argument` method. 
3. Run the `ArgumentParser.parse_args()` method to store the parsed arguments in a `argparse.Namespace` object.
4. Access the arguments from the `Namespace` object using the dot(`.`)-notation.

An example program is below (and [in our repository](https://github.com/PyHOGS/pyhogs.github.io/blob/pelican-source/pyhogs-code/example-scripts/argparse_example.py)), but check out the
[documentation](https://docs.python.org/2.7/library/argparse.html) for all of
its features and more examples.

    :::python
    '''
    This example script prints the mean and standard deviation 
    of a list of scores to demonstrate some of the features of argparse.
    
    This should all be wrapped in a main function, but I just wanted to 
    keep things simple.
    '''
    
    from __future__ import print_function, division
    import argparse
    
    # Define mean and standard deviation functions. We could use numpy,
    # but I only want to use Python 2 standard libraries...
    def mean(x):
        '''Return mean of list'''
        return sum(x) / len(x)
        
    def std(x):
        '''Return (unbiased) standard deviation of list'''
        m = sum(x) / len(x)
        xp2 = [(xi - m)**2. for xi in x]
        return (sum(xp2) / (len(x) - 1))**(1./2)
        
    # Create the parser
    parser = argparse.ArgumentParser('Determine mean and standard deviation of a list.')
    
    # Add the arguments. Notice that by specifying the argument without or with
    # dashes determines whether it's positional or not. Positional arguments
    # are added in the order they should be specified.
    
    # Positional argument with a list, by default it stores the result
    # to args.scorces, but you can specifiy the location 
    # using the `dest` keyword
    default_scores = [4., 9., 8., 3.]
    parser.add_argument('scores',
                        type=float,   # Store as floats 
                        nargs='*', # Gets all following arguments and stores as list
                        default=default_scores, # Set default scores
                        help='Scores to compute statistics for'  # Help text
                        )
                        
    # Add a stand-alone, boolean argument, off-by-default
    parser.add_argument("--verbose", # Long form,
                        "-v", # Short form
                        help="Print more stuff",
                        action="store_true") 
                        
    # Parse the arguments
    args = parser.parse_args()
    
    # We're done with the specification and parsing. In a real script you could
    # define the parser in a function to seperate it from the main code.
    
    # Determine the statistics
    m = mean(args.scores)
    s = std(args.scores)
    
    if args.verbose:
        print('The mean is: {:f}'.format(m))
        print('The standard deviation is: {:f}'.format(s))
    else:
        print('{:f} {:f}'.format(m, s))

This script returns:

    $ python argparse_example.py -h
    usage: Determine mean and standard deviation of a list. [-h] [--verbose]
                                                            [scores [scores ...]]
                                                            
    positional arguments:
      scores         Scores to compute statistics for
      
    optional arguments:
      -h, --help     show this help message and exit
      --verbose, -v  Print more stuff
      
    $ python argparse_example.py
    6.000000 2.943920
    
    $ python argparse_example.py -v
    The mean is: 6.000000
    The standard deviation is: 2.943920
    
    $ python argparse_example.py 1 1 1 1 1
    1.000000 0.000000
    
    $python argparse_example.py -2 -1 0 1 2 -v
    The mean is: 0.000000
    The standard deviation is: 1.581139
