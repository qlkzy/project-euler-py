#!/usr/bin/env python

# find the largest prime factor of 600851475143

def problem_3(x):
    """Find the largest prime factor of x."""
    factor = 2
    while x > 1:
        if x%factor == 0:
            x /= factor
        else:
            factor += 1
    return factor

print problem_3(600851475143)
