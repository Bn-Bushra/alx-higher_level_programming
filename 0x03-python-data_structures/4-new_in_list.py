#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        newList = my_list.copy()
        newList.remove(my_list[idx])
        newList.insert(idx, element)
        return newList

# # testing
# cube = [1, 3, 5, 9, 11, 13]
# # newCube = cube.copy()
# # newCube.remove(cube[1])
# # newCube.insert(1,8)
# # print(newCube)
# # print(cube)
# print(new_in_list(cube,1,9))
# print(cube)
