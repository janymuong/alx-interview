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

    for _ in range(x):
        mariaTurn = True
        n = len(nums)

        while n > 0:
            if mariaTurn:
                prime = findPrime(nums)
                removeMultiples(nums, prime)
                n -= 1
                mariaTurn = False
            else:
                prime = findPrime(nums)
                removeMultiples(nums, prime)
                n -= 1
                mariaTurn = True

        if mariaTurn:
            benWins += 1
        else:
            mariaWins += 1

    if mariaWins > benWins:
        return f'Maria'
    elif benWins > mariaWins:
        return f'Ben'
    else:
        return None


def findPrime(nums):
    '''return prime number determined:
    '''
    for num in nums:
        if isPrime(num):
            return num
    return -1


def removeMultiples(nums, prime):
    '''rid multiples/ duplicates
    '''
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] % prime == 0:
            del nums[i]


def isPrime(n):
    '''get prime numbers
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
