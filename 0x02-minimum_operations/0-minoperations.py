#!/usr/bin/python3
'''Minimum Operations - Data Structures;
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
    Copy All and Paste.
    Given a number n, this method calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''minOperations(args)
    calculates the fewest number of operations
    needed to achieve `n` `H` characters in a text file.

    args:
    n: the desired number of H characters in the text file.

    returns:
        an integer, the fewest number of operations
        needed to achieve n H characters in the text file,
        or 0 if n is impossible to achieve.
    '''
    if n <= 0:
        return 0

    # initialize array to store minimum operations for each position
    min_op = [float('inf')] * (n + 1)

    min_op[1] = 0

    # get minimum operations for each position from 2 to n
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                min_op[i] = min(min_op[i], min_op[j] + i // j)

    return min_op[n] if min_op[n] != float('inf') else 0
