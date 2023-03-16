#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1
    if arg == 1:
        print("{} argument:".format(arg))
        print("{}: {}".format(arg, argv[arg]))
    else:
        if arg != 0:
            print("{} arguments:".format(arg))
            for a in range(0, arg):
                print("{}: {}".format(a + 1, argv[a + 1]))
        else:
            print("{} arguments.".format(arg))
