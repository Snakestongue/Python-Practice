import pandas as pd
df = pd.read_csv("pandas/employee.csv")
df["salary"].mean()
df.groupby("city")["salary"].mean().idxmax()
df.sort_values(["salary"], ascending=False).head()
df.isnull().sum()
df["takeHome"] = df["salary"] - (df["salary"] *.09)