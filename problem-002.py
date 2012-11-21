#!/usr/bin/env python

# summing the even-valued terms below 4000000 in the fibonacci sequence

def problem_2(n):
    """Sum the even-valued terms in the fibonacci sequence below n."""
    prev = 1
    curr = 1
    total = 0
    while curr < n:
        if curr%2 == 0:
            total += curr
        following = prev + curr
        prev = curr
        curr = following
    return total

print problem_2(4000000)
