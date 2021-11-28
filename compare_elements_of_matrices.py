import numpy as np

a = input().split()
matrix1 = (np.array(a, dtype=int))

b = input().split()
matrix2 = (np.array(b, dtype=int))

print(np.greater(matrix1, matrix2))
