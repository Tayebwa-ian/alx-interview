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
    grid_len = len(grid)
    cells = 0
    if grid_len > 101:
        return 0
    for i, list_el in enumerate(grid):
        inner_len = len(list_el)  # length of inner list
        if inner_len > 101 or inner_len == grid_len:
            return 0
        for j, el in enumerate(list_el):
            if (i == 0 or i == grid_len - 1) and el == 1:
                return 0
            elif (j == 0 or j == inner_len - 1) and el == 1:
                return 0
            if el == 1 and (grid[i][j + 1] == 1
                            and grid[i + 1][j] == 1):
                return 0
            if el == 1:
                cells += 1
    paramater = (cells * 2) + 2
    return paramater
