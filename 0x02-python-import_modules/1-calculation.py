#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    print("".join("{} + {} = {}".format(a, b, add(a, b))))
    print("".join("{} - {} = {}".format(a, b, sub(a, b))))
    print("".join("{} * {} = {}".format(a, b, mul(a, b))))
    print("".join("{} / {} = {}".format(a, b, div(a, b))))
