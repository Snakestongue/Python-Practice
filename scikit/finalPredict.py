import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("scikit/grades.csv")

X = df[[
    "Study_Hours",
    "Attendance",
    "HW",
    "Previous_Test"
]]
Y = df["Final_Test"]

xTrain, xTest, yTrain, yTest = train_test_split(
    X, Y,
    test_size=.2,
    random_state=11
)

model = LinearRegression()
model.fit(xTrain, yTrain)
predict = model.predict(xTest)

r = pd.DataFrame({
    "Actual": yTest,
    "Predict": predict.round(2)
})
print(r)
print(mean_absolute_error(yTest, predict))
print(r2_score(yTest, predict))
print(model.coef_) #prints the weighting