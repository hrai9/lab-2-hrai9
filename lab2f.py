#!/usr/bin/env python3

import sys

# Check if an argument is provided
if len(sys.argv) != 2:
    print("Usage: ./lab2f.py <number>")
    sys.exit(1)

# Try converting the argument to an integer

# try - might raise an exception. Here, it tries to convert string argument to int
# except ValueError - if conversion fails (eg, user gives abc and not an integer) python raises 
# (continued) ValueError. This block catches error and execute code
try:
    n = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Countdown
for i in range(n, 0, -1):
    print(i)

print("blast off!")
