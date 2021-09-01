import numpy as np



nparray2 = np.array([[1, 1], [2, 2], [3, 3]]) # Define a 3 x 2 matrix.
nparrayCentered = nparray2 - np.mean(nparray2, axis=0) # Remove the mean for each column
print('Original matrix')
print(nparray2)
print('Centered by columns matrix')
print(nparrayCentered)

print('New mean by column')
print(nparrayCentered.mean(axis=0))


nparray2 = np.array([[1, 3], [2, 4], [3, 5]]) # Define a 3 x 2 matrix.
nparrayCentered = nparray2.T - np.mean(nparray2, axis=1) # Remove the mean for each row
print("nparray:",nparrayCentered)
nparrayCentered = nparrayCentered.T # Transpose back the result
print('Original matrix')
print(nparray2)
print('Centered by columns matrix')
print(nparrayCentered)
print('New mean by rows')
print(nparrayCentered.mean(axis=1))