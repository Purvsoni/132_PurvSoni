import matplotlib.pyplot as plt

# declaring a custom figure size 
fig = plt.figure(figsize=(5,5))

labels = 'ML-Lab1-Matplotlib', 'ML-Lab1-numpy', 'ML-Lab1-scipy'

sizepie = [50,30,20]

plt.pie(sizepie, labels=labels, autopct="%0.2f%%", shadow=False, startangle=0)

plt.axis('equal')

plt.show()

