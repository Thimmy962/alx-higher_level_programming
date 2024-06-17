#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for dic in a_dictionary:
        new_dict[dic] = a_dictionary[dic] * 2
    return new_dict
