import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Network\housing.csv')

X= dataset.iloc[:,[0,1,2,3,4,5,6,7,9]].values

y = dataset.iloc[:,8].values

pd.plotting.scatter_matrix(dataset)

plt.scatter(dataset['total_bedrooms'],dataset['households'])
dataset.isnull().sum()

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values = 'NaN', 
              strategy='median')
X[:,[4]] = imp.fit_transform(X[:,[4]])

from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()
X[:,8] = lab.fit_transform(X[:,8])

from sklearn.preprocessing import OneHotEncoder
one = OneHotEncoder(categorical_features = [8])
X = one.fit_transform(X)
X=X.toarray()

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

lin_reg.score(X,y)