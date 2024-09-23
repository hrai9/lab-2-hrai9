#!/usr/bin/env python3

import sys

# Default countdown value
countdown_start = 3

# Check if an argument is provided
if len(sys.argv) == 2:
    try:
        countdown_start = int(sys.argv[1])  # Convert argument to integer
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)  # Exit with an error status if conversion fails

# Countdown using a while loop
n = countdown_start
while n > 0:
    print(n)
    n -= 1  # Decrement n by 1

print("blast off!")  # Print the final message
