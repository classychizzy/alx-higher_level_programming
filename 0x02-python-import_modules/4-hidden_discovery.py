#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for name in range(0, len(arr)):
        if arr[name][0:2] != "__":
            print("{}".format(arr[name]))
