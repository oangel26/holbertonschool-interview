#!/usr/bin/python
"""
Module that prints pascal triagle
"""

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


def pascal_triangle(n):
    """
    Method which returns a list of list of integers representing
    the Pascal's triangle of n:
    """
    triangle = []
    for row in range(1, n + 1):
        lista = []
        for column in range(1, row + 1):
            if row == 1 or row == 2:
                # First and second row
                lista.append(1)
            elif column > 1 and column < row:
                # Third row and up
                number = (triangle[row - 2][column - 2] +
                          triangle[row - 2][column - 1])
                lista.append(number)
            else:
                # first and last columns of lista
                lista.append(1)
        triangle.append(lista)
    return triangle


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
