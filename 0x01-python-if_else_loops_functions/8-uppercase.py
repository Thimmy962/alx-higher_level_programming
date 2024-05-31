#!/usr/bin/python3
def uppercase(str):
    print("".join("{}".format(chr(ord(i) - 32) if 'a' <= i <= 'z' else i) for i in str))


