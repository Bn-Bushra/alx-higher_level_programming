#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'c' or i == 'C':
            pass
        else:
            print(i, end='  ')
    return ""
