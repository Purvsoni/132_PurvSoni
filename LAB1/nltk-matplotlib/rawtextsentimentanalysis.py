import nltk
from nltk.corpus import twitter_samples
import re 
import string 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk.tokenize import TweetTokenizer


all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

tweet = all_positive_tweets[2277]
print(tweet)

# download the stopwords from NLTK
nltk.download('stopwords')

print('\033[92m' + tweet)
print('\033[94m')
# remove hyperlinks
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)
print(tweet2)


# tokenizing strings
print()
print('\033[92m' + tweet2)
print('\033[94m')
# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False)
# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet2)
print()
print('Tokenized string:')
print(tweet_tokens)