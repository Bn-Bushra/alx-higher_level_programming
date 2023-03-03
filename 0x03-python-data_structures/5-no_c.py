#!/usr/bin/python3
def no_c(my_string):
    if 'c' in my_string == True:
        newString = my_string.replace('c', '', my_string.index('c'))
        print()
        return newString
    # elif 'C' in my_string == True:
    #     newString = my_string.repalce('C', '', my_string.index('C'))
    #     print(newString)
    #     return newString
    # else:
    #     pass


# name = "Chicago"
# print('C' in name)
# # check for the letter c or C in the string
# # if 'c' in string or 'C' in string:
#     # check the index using
#     # if present remove
#         # string.index('c')
# # how 

# new = name.replace('C','',name.index('C'))

# print(new)

# # print(no_c("Best School"))