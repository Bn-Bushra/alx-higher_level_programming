#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # print(row)
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "\n")
    # mat = len(matrix)
    # for i in range(mat):
    #     for j in range(mat):
    #         matrix[i][j] = "{}{}".format(i, j)
    #         # print(matrix[i][j])
    # for i in range(mat):
    #     for j in range(mat):
    #         print("{}".format(matrix[i][j]), end=" ")
    #     print()