import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

"""Create a CSV"""
n=350
data={
    "ID": [i for i in range(1, n+1)], # generates ID 1-350
    "Study_hours": [random.randint(1, 16) for i in range(n)], # generates random study hours from 1-16
    "Att": [random.randint(75, 100) for i in range(n)],# generates random attendance from 75-100%
    "HW": [random.randint(65, 100) for i in range(n)],# generates random HW grade from 65-100
    "Previous_test": [random.randint(65, 100) for i in range(n)],# generates random previous test scores from 65-100
    "Sleep": [random.randint(4, 12) for i in range(n)],# generates random sleep from 4-12 hrs
    "Stress": [random.randint(1, 10) for i in range(n)],# generates random strss level from 1-10
    "Participate": [random.randint(1, 10) for i in range(n)]# generates random participate level from 1-10
}
df = pd.DataFrame(data)

df["Final"]=40+( #does all these features (weighted) + 40 + random (-5,5) to get a final scores
    df["Study_hours"] * .25+
    df["Att"] * .1+
    df["HW"] * .2+
    df["Previous_test"] *.25+
    df["Sleep"] * .05+
    df["Stress"] *-.1+
    df["Participate"] *.1+
    [random.uniform(-5, 5) for i in range(n)] #generateas a random decimal number from -5 --> 5
)
df["Final"] = df["Final"].clip(0, 105).round(2) # round to 2, stops at 105
df.to_csv("students.csv", index=False) # makes the csv

"""Filtering Practice (not needed since CSV generated should not have these issues)"""
df = df[(df["Stress"]>0)& (df["Stress"]<11)]
df = df[df["Final"]<106]
df = df[df["Sleep"]>0]
df = df[df["Att"]<101]

"""NUMPY"""
print("The mean of the dataset is: ", np.mean(df["Final"]))
print("The median of the dataset is: ",np.median(df["Final"]))
print("The variance of the dataset is: ",np.var(df["Final"]))
print("The Standard Deviation of the dataset is: ",np.std(df["Final"]))
print("The 25 Percentile of the dataset is: ",np.percentile(df["Final"], 25))
print("The 50 Percentile of the dataset is: ",np.percentile(df["Final"], 50))
print("The 75 Percentile of the dataset is: ",np.percentile(df["Final"], 75))
print(np.round(np.corrcoef(df["Att"], df["Final"]), 2)) # Correlation
print(np.round(np.corrcoef(df["Study_hours"], df["Final"]),2))

"""PANDAS"""
df = df.sort_values("Final", ascending=False)
print(df.head(10))
print(df.tail(5))
print(df["Stress"].mean())
print(df.groupby("Stress")["Final"].mean())
print(df.groupby("Att")["Final"].mean())

"""Matplotlab"""
plt.figure()
plt.hist(df["Final"]) #histogram
plt.xlabel("Final Scores")
plt.ylabel("Amount")
plt.title("Final Score Distribution")

plt.figure()
plt.scatter(df["Study_hours"], df["Final"]) #scatterplot
plt.xlabel("Hours Studies")
plt.ylabel("Final Score")
plt.title("Study Hours affecting Final Scores")

stressBar = df.groupby("Stress")["Final"].mean()
plt.figure()
plt.bar(stressBar.index, stressBar.values) #bargraph
plt.xlabel("Stress Level")
plt.ylabel("Final Score")
plt.title("Stress affecting Final Scores")

plt.show()

"""SCIKIT"""
X = df[[
    "Study_hours",
    "Att",
    "HW",
    "Previous_test",
    "Sleep",
    "Participate",
    "Stress"
]]
Y = df["Final"]

xTrain, xTest, yTrain, yTest = train_test_split(
    X, Y,
    random_state=11,
    test_size=.2
)
model = LinearRegression()
model.fit(xTrain, yTrain)
predict = model.predict(xTest)

r = pd.DataFrame({
    "Actual": yTest,
    "Prediction": predict.round(2)
})

print(r)
print(mean_absolute_error(yTest, predict))
print(mean_squared_error(yTest, predict))
print(r2_score(yTest, predict))
print(model.coef_)