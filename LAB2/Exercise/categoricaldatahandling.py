# Step 1: Import Libraries

import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

# Step 2: Load Data
        
datasets = pd.read_csv('Exercise-CarData.csv') 
#print("\nData :\n",datasets)
#print("\nData statistics\n",datasets.describe())

# Step 3: Seprate Input and Output attributes

# All rows, all columns except last 
X = datasets.iloc[:, :-1].values 
  
# Only last column  
Y = datasets.iloc[:, -1].values 

#print("\n\nInput : \n", X) 
#print("\n\nOutput: \n", Y) 

# Step 4a: Apply LabelEncoder on the data 
#          to convert FuelType names into numeric values

le = LabelEncoder()
X[ : ,0] = le.fit_transform(X[ : ,0])
#print("\n\nInput : \n", X) 


# Step 4b: Use dummy variables from pandas library
#          to create one column for each Fuel type

dummy = pd.get_dummies(datasets['FuelType'])
print("\n\nDummy :\n",dummy)
datasets = datasets.drop(['FuelType','Weight'],axis=1)
datasets = pd.concat([dummy,datasets],axis=1)
print("\n\nFinal Data :\n",datasets)