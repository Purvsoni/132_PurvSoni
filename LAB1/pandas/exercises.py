import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('Data_for_Transformation.csv')
#print(data)

# Exercise: 1) Draw Scatter Plot between age and salary for "Data_for_Transformation.csv" file
plt.scatter(data['Age'],data['Salary'])
#plt.show()

#2) Draw Histogram of Salary
plt.hist(data['Country'],bins=3)
#plt.show()

#3) Plot bar chart of Country
plt.bar(data['Country'],height=11)
plt.show()