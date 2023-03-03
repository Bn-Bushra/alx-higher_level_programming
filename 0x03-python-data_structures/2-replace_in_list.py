#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list.remove(my_list[idx])
        my_list.insert(idx, element)
        return my_list[idx]
    
# cube = [1, 3, 5, 9, 11, 13]
# cube.remove(cube[1])
# cube.insert(1,8)
# print(cube)
