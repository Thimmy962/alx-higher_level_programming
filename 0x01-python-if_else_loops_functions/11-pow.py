#!/usr/bin/python3
def pow(a, b):
    num = 1
    if b == 0:
        return 1
    while(b > 0):
        num = num * a
        b = b - 1
    
    return num
