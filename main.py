"""A small library of utility functions."""

import math

def is_prime(num):
   
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def get_file_content(filename):
   
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."

def sum_of_many_numbers(*args):
    """
    Calculates the sum of a variable number of numerical arguments.

    This function is written to adhere to PEP 8 style guidelines.
    """
    return sum(args)
