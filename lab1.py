import matplotlib.pyplot as plt
import nltk
from nltk.corpus import twitter_samples
from nltk.corpus.reader import ipipan
import random

nltk.download('twitter_samples')

all_positive_tweets=twitter_samples.strings('positive_tweets.json')
all_negative_tweets=twitter_samples.strings('negative_tweets.json')

print(len(all_negative_tweets),type(all_positive_tweets))
print(len(all_negative_tweets),type(all_negative_tweets))

fig=plt.figure(figsize=(5,5))

labels='ML-BSB-LEC','ML-HAP-LEC','ML-HAP-LAB'
sizes=[40,35,25]
plt.pie(sizes,labels=labels,autopct='%.2f%%',shadow=True,startangle=90)

plt.axis('equal')
plt.show()