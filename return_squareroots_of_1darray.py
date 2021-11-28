import numpy as np

a = input().split()
table1D = (np.array(a, dtype=float))

result = np.sqrt(table1D)
print(*result)