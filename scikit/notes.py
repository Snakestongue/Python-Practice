from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import pandas as pd

"""CLEANING - FROM PROJECT"""
df = pd.read_csv("mpl/students.csv") #read
df = df.drop_duplicates(subset=["Name"]) #delete duplicate name

subjects = ["Math", "Science", "English"] #array of subjects
df = df[(df[subjects]>0).all(axis=1) & (df[subjects]<101).all(axis=1)] # filter so grades between 0-100, boolean series

df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce") 
df = df[(df["Attendance"]<101) & (df["Attendance"]>0)]
df.dropna(axis=0, subset=["Attendance"], inplace=True)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df = df[(df["age"]>13) & (df["age"]<19)]
df.dropna(axis=0, subset=["age"], inplace=True)

df["Student_ID"] = "SO" + (df.index+1).astype(str)

df["average"] = ((df["Math"] + df["English"] + df["Science"]) / 3).round(2)
df = df.sort_values(["average"], ascending=False)


"""SCIKIT"""
X = df[[
    "Math",
    "Science",
    "English",
    "Attendance",
    "Study_Hours_Per_Week"
]] # this is the features a model looks at when determining a target

Y = df["average"] # the target

xTrain, xTest, yTrain, yTest = train_test_split(
    X, #features
    Y, #targets
    test_size=.2, #20% testing, 80% training
    random_state=11 # like a seed in numpy
)
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

"""Vocab"""
#Target Leakage: When you ask the model to predict something but you gave everything
#Features: X, factors when determing a target
#Target: Y, trying to determine this
#permutation feature importance: Weighting of each feature and removing to see what happens