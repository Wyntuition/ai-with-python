### Logistic Regression
# - Go to method for binary classification problems (problems with 2 class values)
# - Based on the logistic function, or the sigmoid function, originally developed to describe properties of population growth, so is an S-shaped curve that maps any real number into a value between 0 and 1 exclusive: 1 / (1 + e^value) (i.e. bianry problem: male or female. Closer to 1, more likely male.)
# - Done using sklearn's LogisticRregression classiciation algorithm

import numpy as np 
from sklearn import linear_model  
import matplotlib.pyplot as plt 
from utilities import visualize_classifier 


# Define sample input data with two-dimensional vectors and corresponding labels:
X = np.array([[3.1, 7.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5], [5.6, 5], [3.3, 0.4], [3.9, 0.9], [2.8, 1], [0.5, 3.4], [1, 4], [0.6, 4.9]]) 
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]) 

# We will train the classifier using this labeled data. Now create the logistic regression classifier object:
# Create the logistic regression classifier 
classifier = linear_model.LogisticRegression(solver='liblinear', C=1) 

# Train the classifier using the data that we defined earlier:
classifier.fit(X, y) 

#Visualize the performance of the classifier by looking at the boundaries of the classes:
visualize_classifier(classifier, X, y) 