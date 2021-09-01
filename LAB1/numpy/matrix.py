import numpy as np

alist = [1, 2, 3, 4, 5]
narray = np.array([1, 2, 3, 4, 5])

npmatrix1 = np.array([narray, narray, narray])
npmatrix2 = np.array([alist, alist, alist])
npmatrix3 = np.array([narray, [1, 1, 1, 1], narray])
print(npmatrix1)
print(npmatrix2)
print(npmatrix3)

okmatrix = np.array([[1,2],[3,4]])
print(okmatrix)
print(okmatrix*2)

badmatrix = np.array([[1, 2], [3, 4], [5, 6, 7]]) # Define a matrix. Note the third row contains 3 elements
print(badmatrix) # Print the malformed matrix
print(badmatrix * 2) # It is supposed to scale the whole matrix