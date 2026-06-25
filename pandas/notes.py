import pandas as pd
df = pd.read_csv("pandas/employee.csv")
print(df.head()) # prints first 5 rows
print(df.tail()) # prints last 5 rows

print(df.describe())#states like mean & count and other stats stuff
print(df.dtypes) # states data types for columns
print(df.shape) #prints rows, columns
print(df.columns) #prints the column titiles along with the datatype
print(df.info()) #summary + nice format of your csv

x = df[["city", "age"]] #selects columns
y = df["salary"]

z = df.iloc[0:5] # selects rows by position (0-5)

"""Rename"""
df.rename(
    columns={
        "age": "Age" # old-->new
    },
    inplace=True #--> used to change df (not the csv), most don't use it, usually just save it to new variable.
)
#print(df)

"""Replace"""
df.columns = df.columns.str.replace(" ", "_") # replaces spaces with _
print(df.columns)

"""Missing Values"""
df.isnull().sum() # shows total missing values
df.dropna(inplace=True) #Removes missing rows
df["age"] = df["age"].fillna(df["age"].mean())#Fills missing values with the avergae

"""Filter"""
df[(df["salary"]>50000) & (df["city"]=="Portland")] # self explanatory

"""Sorting"""
df.sort_values("salary", ascending=False) # this is descending, remove ascending for normal ascending

"""Columns"""
df["tax"] = df["salary"] * .09 #adds a column, tax, and it's equal to salary x 9%
df.drop("tax", axis=1) # removes tax column

"""Grouping"""
df.groupby("city")["salary"].mean() #groups city/salary together and finds the mean of salary in each city

"""Stats"""
df["salary"].mean() # finds the mean, max, min, sum can also be used
