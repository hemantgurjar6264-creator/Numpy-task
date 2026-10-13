import numpy as np
arr = np.arange(1,100)
l = arr[arr % 2 == 0]
print(l)