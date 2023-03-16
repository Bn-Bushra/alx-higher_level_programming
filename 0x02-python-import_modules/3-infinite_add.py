#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    loopLen = len(argv) - 1
    sum = 0
    for a in range(loopLen):
        arguments = int(argv[a + 1])
        sum += arguments
    print(sum)
