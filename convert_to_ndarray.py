import numpy as np

def convert_to_ndarray():
    a = input().split()
    print(np.array(a, dtype=int))

convert_to_ndarray()