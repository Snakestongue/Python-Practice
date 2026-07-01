import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

np.random.seed(11)

X = np.sort(np.random.rand(200, 1) * 10, axis=0) #AI Data
Y = np.sin(X).ravel() + np.random.normal(0, 0.3, X.shape[0]) #AI Data

"""WEIGHT BASED"""
"""Linear/Polynomial"""
pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=5)),
    ("linear", LinearRegression())
])

xTrain, xTest, yTrain, yTest = train_test_split(
    X, Y, 
    test_size=0.2,
    random_state=11
)
pipeline.fit(xTrain, yTrain)
predict = pipeline.predict(xTest)
#become perfect instantly

"""Ridge"""
ridge =  Ridge(alpha=1.0)
ridge.fit(xTrain, yTrain)
ridge.predict(xTest)
#fit data wel but massive weights are NO GOOD
#uses squares of data
#can make weights close but not exactly 0

"""Lassso"""
lasso = Lasso(alpha=.1)
lasso.fit(xTrain, yTrain)
lasso.predict(xTest)
#fits data well but trys not to use massive weights, like ridge
# uses abs of data not squares
#can make weights exactly 0

#Main Difference: Lasso can say a feature is not helping at all and make it 0, Ridge can't do that


"""TREE BASED"""
"""Forest"""
rfr = RandomForestRegressor(
    n_estimators=100, # how many tree there are, different view different rules of data
    max_depth=5, # only 5 "if statements"
    random_state=11 # seed
)
rfr.fit(xTrain, yTrain)
rfr.predict(xTest)
#a bunch of random trees use "if statements" to decide a prediction and rfr returns the average
#different trees = different results cause A) Usage of different rows B) Different feature usage
#trees do NOT communicate w. each other. They are independant and an average is found

"""Gradient Booster"""
gbr = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=.1, # only trust the previous tree 10% to get the correct answer eventually & slowly
    max_depth=3,
    random_state=11
)
gbr.fit(xTrain, yTrain)
gbr.predict(xTest)
# Trees communocate with each other by basing their predictions off the previous tree

"""VOCAB"""
#Bias: Errors from the model being too simple (straight line on a wiggly)
#Variance: Errors from the model being too complex (wiggles too much)
#Overfitting: Knows the training data (memorized) but can't do the same patteren with test data (too much noise)
#Regularization: A way to prevent overfitting and make a model think simpler - a penalty for being too complex
    #L2 (reduce) -Ridge and L1 (cut) - Lasso do these