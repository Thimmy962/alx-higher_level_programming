#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dic in sorted(a_dictionary):
        print(f"{dic}: {a_dictionary[dic]}")
