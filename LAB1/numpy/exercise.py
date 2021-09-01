import numpy as np

# 1) Create Two numpy array of size 3 X 2 and 2 X 3
# 2) Randomly Initalize that array
array3x2 = np.array([[1,2] , [4,5] , [6,7]])
array2x3 = np.array([[1,2,3,] , [4,5,6]])

#3) Perform matrix multiplication
mul = np.matmul(array3x2,array2x3)
print('Matrix Multiplication',mul)


# 4) Perform elementwise matrix multiplication
elementwisemul1 = np.array(array3x2 * array3x2)  
print(elementwisemul1)
elementwisemul2 = np.array(array2x3 * array2x3)  
print(elementwisemul2)

# 5) Find mean of first matrix
mean1 = np.mean(array2x3)
print("Mean of matrix array3x2:",mean1)

