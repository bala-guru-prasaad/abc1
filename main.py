"""A small library of utility functions."""

import math

def is_prime(num):
    """
    Checks if a number is a prime number.

    This implementation is optimized by checking for divisors only up to the
    square root of the number.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using an iterative approach.
    """
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
    """
    Reads the content of a file and returns it as a string.

    Handles FileNotFoundError gracefully by returning an error message.
    """
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