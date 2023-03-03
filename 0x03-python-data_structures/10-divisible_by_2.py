list = [0, 1, 2, 3, 4, 5, 6]


def divisible_by_2(my_list=[]):
    anotherList = []
    for i in my_list:
        if i/2 == 0:
            anotherList.append(True)
        else:
            anotherList.append(False)
        print(anotherList)
        print(my_list)
    return anotherList
