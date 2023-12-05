#!/usr/bin/python3
'''module: prime GAME
'''


def isWinner(x, nums):
    '''prime game implementation
    args
        x is the number of rounds and nums is an array of n
    Return:
        name of the player that won the most rounds,
        else return None
    '''
    mariaWins = 0
    benWins = 0
    for i in range(x):
        primes = find_prime(nums[i])
        if len(primes) % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1
    if mariaWins > mariaWins:
        return f'Maria'
    elif benWins > mariaWins:
        return f'Ben'
    return None


def find_prime(n):
    '''return prime number determined:
    '''
    primes = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primes.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primes
