import numpy as np

alist = [1, 2, 3, 4, 5]
narray = np.array([1, 2, 3, 4, 5])

print(alist)
print(narray)
print(type(alist))
print(type(narray))


#algebraic operations on pyyhon list vs numpy array
print(alist + alist)
print(narray + narray)

print(narray*3)
print(alist*3)