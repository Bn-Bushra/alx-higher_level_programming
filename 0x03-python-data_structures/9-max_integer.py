#!/usr/bin/python3
def max_integer(my_list=[]):
    highest = 0
    for i in my_list:
        if i > highest:
            temp = i
            i = highest
            highest = temp
    return highest


