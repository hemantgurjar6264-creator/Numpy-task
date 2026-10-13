import numpy as np

arr = np.random.randint(1, 101, (5, 5))

arr.min()
arr.max()

normal = (arr - arr.min()) / (arr.max() - arr.min())

print(normal)

