#!/usr/bin/python3
def new_in_list(my_list=[], idx=int, element=int):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        del new_list[idx]
        new_list.insert(idx, element)
        return new_list
