import numpy as np
import pandas as pd
import seaborn as sns

#loading the dataset
data = pd.read_csv('Data_for_Correlation.csv')

#printing the some of the first rows in the dataset
data.head()

data = data.iloc[:,:-1]
data.head()
data.info()

corr = data.corr()
corr.head()
sns.heatmap(corr)

columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False

selected_columns = data.columns[columns]
data = data[selected_columns]
print(data)

