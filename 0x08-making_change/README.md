# Coin Change Algorithm

> **Note**  
> Python, Algorithm  
>> This Python project implements an algorithm to determine the fewest number of coins needed to meet a given total amount using a dynamic programming approach. The goal is to find the optimal combination of coins from a given set to achieve the desired total.

### Sepcs:
Given a pile of `coins` of different values, determine the fewest number of coins needed to meet a given amount `total`.

Prototype: `def makeChange(coins, total):`  
`Return`: fewest number of coins needed to meet `total`  
If `total` is 0 or less, `return 0`  
If `total` cannot be met by any number of coins you have, `return -1`  
`coins` is a list of the values of the coins in your possession  
The value of a `coin` will always be an *integer greater than 0*  
You can assume you have an infinite number of each denomination of coin in the list  
Your solution’s runtime will be evaluated in this task  


## Function Signature

```python
def makeChange(coins, total):
    '''
    Returns the fewest number of coins needed to meet the given total amount.

    Args:
    - coins: A list of coin values in your possession.
    - total: The total amount to be achieved.

    Returns:
    - The fewest number of coins needed to meet the total. If the total is 0 or less, return 0.
      If the total cannot be met by any combination of coins, return -1.
    '''
    # function implementation ...
```

## Usage

```python
from 0-making_change import makeChange

# example 1
result1 = makeChange([1, 2, 25], 37)
print(result1)  # output: 7

# example 2
result2 = makeChange([1256, 54, 48, 16, 102], 1453)
print(result2)  # output: -1
```

## How to Run:

To test the algorithm, run the provided main file:

```bash
./0-main.py
```

## Notes

- The solution uses a dynamic programming approach for efficiency.
- If the total is 0 or less, the function returns `0`.
- If the total cannot be achieved by any combination of available coins, the function returns `-1`.
