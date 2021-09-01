import numpy as np

okmatrix = np.array([[1,2],[3,4]])
result = okmatrix*2 + 1
print(result)

# Add two sum compatible matrices
result1 = okmatrix + okmatrix
print(result1)
# Subtract two sum compatible matrices. This is called the difference vector
result2 = okmatrix - okmatrix
print(result2)

result = okmatrix * okmatrix # Multiply each element by itself
print(result)


matrix3x2 = np.array([[1, 2], [3, 4], [5, 6]]) # Define a 3x2 matrix
print('Original matrix 3 x 2')
print(matrix3x2)
print('Transposed matrix 2 x 3')    # Transpose of a matrix
print(matrix3x2.T)

nparray = np.array([[1, 2, 3, 4]]) # Define a 1 x 4 matrix. Note the 2 level of square brackets
print('Original array')
print(nparray)
print('Transposed array')
print(nparray.T)