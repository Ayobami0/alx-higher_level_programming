#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for n in range(len(ele)):
            print("{:d}".format(ele[n]), end="" if n == len(ele) - 1 else " ")
        print("")
# print_matrix_integer([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
