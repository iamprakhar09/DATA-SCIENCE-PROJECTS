import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('stopwords')

dataset = pd.read_csv('Network/train.csv')

dataset['tweet'][31961]

clean_tweets = []

for i in range(31962):
    tweet = re.sub('@[\w]*',' ',dataset['tweet'][i])
    tweet = re.sub('[^a-zA-Z#]',' ', tweet )
    tweet = tweet.lower()
    tweet = tweet.split()
    #temp =  [token for token in tweet if not token in stopwords.words('english')]
    tweet = [ps.stem(token) for token in tweet if not token in stopwords.words('english')]
    tweet = ' '.join(tweet)
    clean_tweets.append(tweet)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 3000)
X = cv.fit_transform(clean_tweets)
X = X.toarray()
y = dataset['label'].values

print(cv.get_feature_names())

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X,y)
gnb.predict(X)
gnb.score(X,y)