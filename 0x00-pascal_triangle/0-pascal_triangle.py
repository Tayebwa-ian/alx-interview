#!/usr/bin/python3
"""
Pascal's Triangle Module file
"""


def pascal_triangle(n) -> list:
    """ Return a list of values representing a pascal's triangle
    Arg:
        n: size of a triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        while(n > 0):
            temp = [1]
            if len(triangle) == 0:
                triangle.append(temp)
            else:
                for i in range(len(triangle[-1])):
                    if i == (len(triangle[-1]) - 1):
                        temp.append(1)
                    else:
                        j = i + 1
                        m = triangle[-1][i] + triangle[-1][j]
                        temp.append(m)
                triangle.append(temp)
            n -= 1
        return triangle
