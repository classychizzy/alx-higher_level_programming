#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        else:
            i = chr(ord(i))
        print("{:s}".format(i), end="")
    print(" ")
