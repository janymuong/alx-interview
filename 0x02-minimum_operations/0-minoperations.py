#!/usr/bin/python3
'''Minimum Operations - Data Structures;
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
    Copy All and Paste.
    Given a number n, this method calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
'''


def minOperations(n, memo={}):
    '''minOperations(args)
    calculates the fewest number of operations
    needed to achieve `n` `H` characters in a text file.

    args:
    n: the desired number of H characters in the text file.
    memo: dictionary to store already computed results,
        which significantly reduces the number of recursive calls

    returns:
        an integer, the fewest number of operations
        needed to achieve n H characters in the text file,
        or 0 if n is impossible to achieve.
    '''
    if n == 1:
        return 1
    elif n < 1:
        return 0

    if n in memo:
        return memo[n]

    half = n // 2
    if n % 2 == 0:
        memo[n] = min(minOperations(half) + 1, minOperations(n - half) + 1)
    else:
        memo[n] = min(minOperations(half) + 2, minOperations(n - half) + 2)

    return memo[n]
