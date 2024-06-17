#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set(set_1)
    for i in set_2:
        new_set.add(i)
    return new_set
