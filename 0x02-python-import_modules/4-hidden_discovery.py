#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for l in dir(hidden_4):
        if l[:2] != "__":
            print("{:s}".format(l))
