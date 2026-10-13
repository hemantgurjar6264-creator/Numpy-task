import numpy as np

arr = np.array([10, 50, 30, 80, 20])

largest = arr.max()

arr[arr<largest]

second_largest = arr[arr < largest].max()

print(second_largest)