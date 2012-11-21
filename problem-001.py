#!/usr/bin/env python

# sum natural numbers below one thousand that are multiples of 3 or 5

def problem_1(n):
    """Sum natural numbers below n that are multiples of 3 or 5."""
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print problem_1(1000)
