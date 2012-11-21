#!/usr/bin/env python

# find the largest palindromic number that is the product of two
# 3-digit numbers

def palindromic(x):
    """Return True if x is palindromic."""
    digits = []
    while x > 0:
        digits.append(x % 10)
        x /= 10
    return digits == digits[::-1]

def problem_4(n):
    """Return the largest palindrome made from the product of two
    integers less than n."""
    best_so_far = 0
    for x in range(0, n):
        for y in range(0, n):
            if palindromic(x*y):
                best_so_far = max(best_so_far, x*y)
    return best_so_far

print problem_4(1000)

