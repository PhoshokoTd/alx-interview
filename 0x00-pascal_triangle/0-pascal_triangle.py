#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the Pascal’s triangle of n number
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle_lst = [[1]]
    for i in range(1, n):
        prev_row = triangle_lst[-1]
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        triangle_lst.append(row)
    return triangle_lst
