#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    This function recursively calculates the factorial of a non-negative integer.
    The factorial of n (denoted as n!) is the product of all positive integers
    less than or equal to n.

    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number.

    Raises:
    RecursionError: If the input is too large, causing excessive recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)