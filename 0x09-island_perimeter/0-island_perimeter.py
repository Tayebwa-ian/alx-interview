#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Calculate paraneter of an Item
    Arg:
        grid: list of lists
    """
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for i, j in zip([0] + row, row + [0]):
            perimeter += int(i != j)
    return perimeter
