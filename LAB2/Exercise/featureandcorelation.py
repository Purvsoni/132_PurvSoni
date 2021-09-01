import numpy as np
import pandas as pd
import seaborn as sns

#loading the dataset
data = pd.read_csv('Exercise-CarData.csv')

#printing the some of the first rows in the dataset
data.head()

data = data.iloc[:,:-1]
data.head()
data.info()

corr = data.corr()
corr.head()

columns = np.full((corr.shape[0],), True, dtype=bool)
print(columns)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False
