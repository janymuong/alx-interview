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

    # initialize lsit to store minimum operations for each position
    min_op = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                min_op.append(i)
    return sum(min_op)
