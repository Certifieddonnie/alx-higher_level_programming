#!/usr/bin/python3

# function that prints the last digit of a number.
# Returns the last digit.

def print_last_digit(number):
    if number < 0:
        number = number * (-1)
    num = number % 10
    print("{}".format(num), end='')
    return (num)
