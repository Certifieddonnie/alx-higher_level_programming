#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    counter = 0
    for num in my_list:
        if counter == idx:
            break
        counter += 1
    return num
