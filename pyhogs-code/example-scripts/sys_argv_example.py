#!/usr/bin/env/python
from __future__ import print_function
import sys

# Get the total number of arguments
total = len(sys.argv) - 1 # Subtract 1 for the script name

# Print it
print("{:d} arguments passed to the script".format(total))
for i, a in enumerate(sys.argv):
    print("Argument #{:d}: {} ".format(i, a))