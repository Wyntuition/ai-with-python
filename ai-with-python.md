# Python Machine Learning

From the book, [Artificial Intelligence with Python](https://www.safaribooksonline.com/library/view/artificial-intelligence-with/9781786464392/ch02s03.html)

python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install -U scikit-learn

## Concepts

- Building models, label data, make predictions
- automated reasoning, cognitive modeling, neural networks, genetic algorithms, expert databases, expert systems, knowledge representation, logic programming, and natural-language processing

### 1.

- Turing Test
- rational agents
- General Problem Solver (GPS)
- Different tyyes of models

### 2. Classification & regression using supervised learning

- Preprocessing data
- Label encoding
- Build a logistic regression classifier
- Naive Beyes classifier
- Confusion matrix
- Support Vector Machines. Build classifier based on that.
- Linear and polynomial regression
- Build a linear regressor for single variable and multivariable data
- Estimate housing prices using Support Vector Regressor
- 



## Getting Started using scikit-learn (has test datasets, etc)

from sklearn import datasets
house_prices = datasets.load_boston()
print(house_prices.data)
print(house_prices.target) // labels

// Image datasets
digits = datasets.load_digits()
print(digits.images[4]) // print 5th image


### LAB: Preprocessing data

Binarization
Mean removal
Scaling
Normalization

#### Binarization - converting numerical values into booleans




@mitultiwari

NOTES:

- pip not working - put in .profile: pip3='python3 -m pip'