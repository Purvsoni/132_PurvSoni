import numpy as np

vector1 = np.array([0, 1, 2, 3])
vector2 = np.array([1,2,3,4])

dotprod = np.dot(vector1,vector2)  #Way-1
print(dotprod)


dotprod =  np.sum(vector1*vector2)  #Way-2
print(dotprod)

flavor3 = vector1 @ vector2 # Way-3
print(flavor3)

# As you never should do: #Way-4
flavor4 = 0
for a, b in zip(vector1, vector2):
    flavor4 += a * b
print(flavor4)

