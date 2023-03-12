#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inn in range(len(matrix)):
        for out in range(len(matrix)):
            print("{} {} {}".format((inn,out), out, out, ))