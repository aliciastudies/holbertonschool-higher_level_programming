#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("{0} arguments.".format(0))
    elif length == 2:
        print("{0} argument:".format(1))
        print("{0}: {1}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, length):
            print("{0}: {1}".format(i, sys.argv[i]))
