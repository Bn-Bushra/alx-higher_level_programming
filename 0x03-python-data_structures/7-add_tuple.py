#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if tuples contain less than two value, replace it with zero?
    t1 = tuple_a + (0, 0)
    t2 = tuple_b + (0, 0)
    i = t1[0] + t2[0]
    j = t1[1] + t2[1]
    return i, j
