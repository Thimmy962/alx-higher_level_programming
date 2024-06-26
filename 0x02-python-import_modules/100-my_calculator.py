#!/usr/bin/python3
from calculator_1 import *
from sys import argv, exit


def main():
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in ['-', '+', '/', '*']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif op == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif op == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    main()
