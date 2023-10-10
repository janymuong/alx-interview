# Minimum Operations

> To Achieve `'H'` Characters;  
>> Provides a function to calculate the fewest number of operations needed to achieve a specified number of `'H'` characters in a text file. The operations allowed are `Copy All `and `Paste`.

## Usage

```bash
$ ./0-main.py
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
$
```

## Function
```python
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
    ...
```

## Test Case:

For example, if `n = 12`, the minimum number of operations required is 7. The function efficiently computes this value using dynamic programming.
