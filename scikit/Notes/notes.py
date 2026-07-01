from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import pandas as pd
df = pd.read_csv("scikit/Notes/students.csv") #read

"""SCIKIT"""
X = df[[
    "Math",
    "Science",
    "English",
    "Attendance",
    "Study_Hours_Per_Week"
]] # this is the features a model looks at when determining a target

Y = df["average"] # the target

xTrain, xTemp, yTrain, yTemp = train_test_split(
    X, #features
    Y, #targets
    test_size=.3, #30% temporary, 70% training
    random_state=11 # like a seed in numpy
) 
xVal, xTest, yVal, yTest = train_test_split(
    xTemp, yTemp, test_size=.5, random_state=12
)
#splits into 15% validation, 15% testing --> validation for selecting best model with lowest MSE

#xtrain: Features (data) to learn
#yTrain: actual result based off features
# xTest: "Practice problems" the model has not seen
#yTest: The actual result

model = LinearRegression() #a model that has "no brain"
model.fit(xTrain, yTrain) #this is where the model actually learns the relationship between the features and target
predict = model.predict(xTest)# this is the test to see how accurate the model is


r = pd.DataFrame({
    "Actual": yTest,
    "Prediction": predict.round(2)
})
print(r)
print(mean_absolute_error(yTest, predict)) #off by about whatever this point value is (low better)
print(r2_score(yTest, predict))# percent variation it understands (0-1) (real answer, prediction) (high better)
print(mean_squared_error(yTest, predict)) # used for identifiying large mistakes
print(model.coef_) #prints the weighting
"""Vocab"""
#Target Leakage: When you ask the model to predict something but you gave everything
#Features: X, factors when determing a target
#Target: Y, trying to determine this
#permutation feature importance: Weighting of each feature and removing to see what happens
#Data leakage: When a model gets data it shouldn't (such as predicting final grade but it's already given)
#Preprocsessing: Turns raw data into data that a model can effectivly use 
    #StandardScaler --> turns data (ex comparing age and salary) into comparable values
