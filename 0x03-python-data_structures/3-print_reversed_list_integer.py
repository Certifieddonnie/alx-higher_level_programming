#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    counter = -1
    for num in my_list:
        counter += 1
    while (counter >= 0):
        print("{:d}".format(my_list[counter]))
        counter = counter - 1
