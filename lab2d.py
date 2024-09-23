#!/usr/bin/env python3

import sys

# Check the number of command line arguments
if len(sys.argv) < 3 or len(sys.argv) > 3:
    # Output the usage message if there are not exactly 2 arguments
    print("Usage: ./lab2d.py name age")
else:
    # Extract name and age from the arguments
    name = sys.argv[1]
    age = sys.argv[2]
    # Print the correct message
    print(f"Hi {name}, you are {age} years old.")
