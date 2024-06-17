#!/usr/bin/python3
def best_score(a_dictionary):
    highest = None
    point = 0
    if a_dictionary is None:
        return highest
    for dic in a_dictionary:
        if a_dictionary[dic] > point:
            point = a_dictionary[dic]
            highest = dic
    return highest
