#!/usr/bin/python3
if __name__ == "__main__":
    """function that prints the addition of command arguments"""
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
        print("{}".format(result))
