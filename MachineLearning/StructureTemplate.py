#!/usr/bin/env python
# coding: utf-8

# # Decision Tree

# ### Import the data

# Learn how to predict the kind of music people like. 

# The goal of using a Decision Tree is to create a training model that can use to predict the class or value
# of the target variable by learning simple decision rules inferred from prior data(training data).

# use pandas to import data
import pandas as pd

try:
    data = pd.read_csv('music.csv')
except IOError as e:
    print(e)

# ### Clean the data

# No duplicates
data[data.duplicated()]

data.duplicated()

# Checks for null values

#data.isnull().any()
#data.isnull().values.sum() > 0
#data.isnull().sum() > 0
data.isnull().values.any()

# dropna drops missing values (think of na as "not available")
# axis=0 specifies rows that will be removed from the dataset
data = data.dropna(axis=0)

# ### Choose Prediction target and Features

# The columns that are inputted into our model (and later used to make predictions) are called "features." 
# In our case, those would be the columns used to determine the genre
# By convention, this data is called X.

# Features
features = ['age', 'gender']

X = data[features]
X.head()

# We'll use the dot notation to select the column we want to predict, which is called the prediction target. 
# By convention, the prediction target is called y.

# predicitons / answers
y = data.genre
y.head()

# ### Split the Data into Training / Test sets

# this class splits arrays or matrices into random train and test subsets.
from sklearn.model_selection import train_test_split

# test_size=0.2 allocates 20% of our data for testing
# train_test_split returns a tuple so we unpack it into 4 variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
y_test

# ### Define/Build/Specify a model

# sklearn is the package that comes with scikit learn library
# in this package we have a module called tree
# in this module we have a class called DecisionTreeClassifier
# this class implements the decision tree algorithm
from sklearn.tree import DecisionTreeClassifier

# Create a new instance of the DecisionTreeClassifier class
model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=1)

# ### Fit/Train the model

# fit() is for training a model. It produces metrics for the training set
# When training the model, pass only the training dataset
model.fit(X_train, y_train)


# ### Make predictions

# When making predictions, we pass the testing dataset
predictions = model.predict(X_test)
predictions

# Accuracy classification score.
# this function computes subset accuracy
# the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true.
from sklearn.metrics import accuracy_score

# y_test contains the expected values
# predicitons contains the actual values
# returns a prediction score between 0 - 1
score = accuracy_score(y_test, predictions)
score

# ### Evaluate and improve

# Evaluate() is for testing the trained model on the test set.

# Create Decision Tree classifer object
new_model = DecisionTreeClassifier(splitter='random')

# Fit/Train the Decision Tree Classifer
new_model = new_model.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = new_model.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", accuracy_score(y_test, y_pred))

# #### Visualising the tree

from sklearn import tree

tree.export_graphviz(model, 
                    out_file='music_recommend.dot',
                    feature_names=['age', 'gender'],
                    class_names=sorted(y.unique()),
                    label='all',
                    rounded=True,
                    filled=True)

