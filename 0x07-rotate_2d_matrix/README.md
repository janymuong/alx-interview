# Rotate 2D Matrix

> This implements a Python function to rotate a 2D matrix ***90 degrees clockwise***. The rotation is done in-place.  
> **Prompt**:  
>> Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.  

>> Prototype: `def rotate_2d_matrix(matrix):`  
>> Do not return anything. The matrix must be edited in-place.  
>> You can assume the matrix will have 2 dimensions and will not be empty.  


## Environment

```python
- Python version: 3.8.10
- Operating System: Ubuntu 20.04 LTS
- Code style: pycodestyle (version 2.8.0)
```

## Usage

To use the matrix rotation function, import the `rotate_2d_matrix` function from `0-rotate_2d_matrix.py` and provide a 2D matrix as an argument. The matrix will be rotated in place.

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

```bash
./main_0.py
```


## Implementation Details

The rotation is achieved in two steps:
1. Transpose the matrix (swap rows with columns).
2. Reverse each row of the transposed matrix.


## Files

- `0-rotate_2d_matrix.py`: implementation of the matrix rotation function.
- `main_0.py`: script to demo.

