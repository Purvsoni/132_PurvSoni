import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10,10))

labels = 'Positive','Negative'

size = [50, 50]

plt.pie(size, labels=labels, autopct="%0.2f%%", shadow= True, startangle=0)

plt.show()