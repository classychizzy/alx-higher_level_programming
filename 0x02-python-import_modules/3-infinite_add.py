#!/usr/bin/python3
if __name__ == "__main__":
    """function that prints the addition of command arguments"""
    import sys
    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
        print("{}".format(result))
