import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def grades(score):
    if score >89:
        return "A"
    elif score>79:
        return "B"
    elif score>69:
        return "C"
    elif score>59:
        return "D"
    else:
        return "F"

def pf(score):
    if score>64:
        return "PASS"
    else:
        return "FAIL"
df = pd.read_csv("mpl/students.csv")
df = df.drop_duplicates(subset=["Name"])

subjects = ["Math", "Science", "English"]
df = df[(df[subjects]>0).all(axis=1) & (df[subjects]<101).all(axis=1)]

df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
df = df[(df["Attendance"]<101) & (df["Attendance"]>0)]
df.dropna(axis=0, subset=["Attendance"], inplace=True)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df = df[(df["age"]>13) & (df["age"]<19)]
df.dropna(axis=0, subset=["age"], inplace=True)

df["Student_ID"] = "SO" + (df.index+1).astype(str)

df["average"] = ((df["Math"] + df["English"] + df["Science"]) / 3).round(2)
df["letter_grade"] = df["average"].apply(grades)
df["pass_fail"] = df["average"].apply(pf)

df = df.sort_values(["average"], ascending=False)
# print(df.head(10))
# print(df.tail(10))
# print((df["Math"].mean()).round(2))
# print((df["Science"].mean()).round(2))
# print((df["English"].mean()).round(2))
# print(df["Attendance"].max())
# print(df["Attendance"].min())
# print(df["Study_Hours_Per_Week"].max())
# print((df.groupby("Gender")["average"].mean()).round(2))
# print((df["Class"]==9).sum())
# print((df["Class"]==10).sum())
# print((df["Class"]==11).sum())
# print((df["Class"]==12).sum())

print(np.mean(df["average"]))
print(np.median(df["average"]))
print(np.std(df["average"]))
print(np.var(df["average"]))
print(np.max(df["average"]))
print(np.percentile(df["average"], 25))
print(np.percentile(df["average"], 50))
print(np.percentile(df["average"], 75))
print(np.round(np.corrcoef(df["Attendance"], df["average"]), 2))
print(np.round(np.corrcoef(df["Study_Hours_Per_Week"], df["average"]), 2))

plt.scatter(df["Study_Hours_Per_Week"], df["average"])
# plt.plot(df["Attendance"], df["average"])
plt.show()