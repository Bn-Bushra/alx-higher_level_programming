#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if tuples contain less than two value, use 1 for the missing one solve?
    a, b = tuple_a + (0)
    c, d = tuple_b, (0)
    i = a + c
    t = b + d
    return i, t