import numpy as np

nparray1 = np.array([[1,2] , [3,4],[5,6]])

sum = np.sum(nparray1, axis=0)  #sum by the cols of npaaray
print("Sum by rows:",sum)

sum1 = np.sum(nparray1, axis=1) #sum by the rows of npaaray
print("Sum by Cols:",sum1)

# Mean of a matrix
nparray2 = np.array([[1, 2], [2, 3], [3, 4]]) # Define a 3 x 2 matrix. Chosen to be a matrix with 0 mean
mean = np.mean(nparray2) # Get the mean for the whole matrix
meanByCols = np.mean(nparray2, axis=0) # Get the mean for each column. Returns 2 elements
meanByRows = np.mean(nparray2, axis=1) # get the mean for each row. Returns 3 elements
print('Matrix mean: ')
print(mean)
print('Mean by columns: ')
print(meanByCols)
print('Mean by rows:')
print(meanByRows)


#norm of a given matrix
nparray1 = np.array([1, 2, 3, 4]) # Define an array
norm1 = np.linalg.norm(nparray1)
nparray2 = np.array([[1, 2], [3, 4]]) # Define a 2 x 2 matrix. Note the 2 level of square brackets
norm2 = np.linalg.norm(nparray2)
print(norm1)
print(norm2)


