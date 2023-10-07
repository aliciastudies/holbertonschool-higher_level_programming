#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for index in range(len(matrix[row])):
            if index != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][index]), end="")
        print("")
