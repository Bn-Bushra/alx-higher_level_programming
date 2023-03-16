#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    anotherList = []
    for i in my_list:
        if i % 2 == 0:
            anotherList.append(True)
        else:
            anotherList.append(False)
    return anotherList
