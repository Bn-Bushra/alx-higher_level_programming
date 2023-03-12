#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
       if str[i] >= 'a' and str[i] <= 'z':
            print(chr(ord(str[i]) - 32), end="")
       elif str[:-1]:
            print(str[i], end="")
       else:
            print(str[i])
    print()
