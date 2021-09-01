import nltk
from nltk.corpus import twitter_samples
import re 
import string 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk.tokenize import TweetTokenizer

tweet = "Incredible: 4 million iPhone 4Ss in 3 days. 135% better than the iPhone 4 http://t.co/1FMJxTMM @apple iphone4s"

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

