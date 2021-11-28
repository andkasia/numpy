import numpy as np

liczby = list(map(int,input().split()))

n = liczby[0]*liczby[1]
array = np.arange(n)
matrix2D = array.reshape(liczby[0], liczby[1])

print(matrix2D)