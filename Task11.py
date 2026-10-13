import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

l = arr.reshape((5,5))

print(l)

g = l.sum(axis = 1)
print(g)


