#!/usr/bin/python3
from sys import argv, exit

len = len(argv)
if __name__ == "__main__":
    if len == 1:
        print("0 argument.")
        exit()

    elif len == 2:
        print("".join("{} argument:".format(len - 1)))
    else:
        print("".join("{} arguments:".format(len - 1)))

    for i in range(1, len):
        print(f"{i}: {argv[i]}")
