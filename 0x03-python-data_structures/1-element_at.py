#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif len(my_list) > 0:
        if idx > len(my_list):
            return None
        else:
            return my_list[idx]
