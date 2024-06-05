#!/usr/bin/python3
def remove_char_at(str, n):
    str_1 = ""
    for (index, char) in enumerate(str):
        if index == n:
            continue
        else:
            str_1 += char
    return str_1
    