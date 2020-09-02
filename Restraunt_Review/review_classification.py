import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk

dataset=pd.read_csv('Network/Restaurant_Reviews.tsv',delimiter = '\t')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('stopwords')

dataset['Review'][0]
clean_review = []

for i in range(1000):
    Review = dataset['Review'][i]
    Review = re.sub('[^a-zA-Z#]',' ',Review)
    Review = Review.lower()       
    Review = Review.split()
    Review = [ps.stem(token) for token in Review if not token in stopwords.words('english')]
    Review = ' '.join(Review)
    clean_review.append(Review)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 3000)
X = cv.fit_transform(clean_review)
X = X.toarray()

y = dataset['Liked'].values

print(cv.get_feature_names())

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X,y)
gnb.predict(X)
gnb.score(X,y)