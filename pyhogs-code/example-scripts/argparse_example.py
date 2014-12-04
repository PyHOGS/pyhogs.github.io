#!/usr/bin/python
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

# We're done with the specification and parsing. In a real script you could define the parser in a function to seperate it from the main code.

# Determine the statistics
m = mean(args.scores)
s = std(args.scores)

if args.verbose:
    print('The mean is: {:f}'.format(m))
    print('The standard deviation is: {:f}'.format(s))
else:
    print('{:f} {:f}'.format(m, s))
