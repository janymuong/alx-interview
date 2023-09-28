#!/usr/bin/python3
'''module - file for Pascal's triangle.
'''


def pascal_triangle(n):
    '''Pascal's triangle;
    returns a list of lists of ints representing the Pascal's triangle of n:
    Returns an empty list if n <= 0
    Aassumes `n` will be always an integer
    '''

    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        row = [1]
        if pascal_triangle:
            last_row = pascal_triangle[-1]
            row.extend([last_row[j] + last_row[j + 1]
                        for j in range(len(last_row) - 1)])
            row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
