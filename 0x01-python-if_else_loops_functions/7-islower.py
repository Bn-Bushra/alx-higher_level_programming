#!/usr/bin/python3
def islower(c):
    for z in (range(97, 122)):
        if c is chr(z):
            return True
        else:
            return False
for i in range(97, 123):
    print(islower(chr(i)))
