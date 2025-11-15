#!/usr/bin/python3

def print_last_digit(number):
    """Print and return the last digit of a number."""
    last_digit = abs(number) % 10  # Get the absolute value and find the last digit
    print("{:d}".format(last_digit), end="")  # Print the last digit
    return last_digit