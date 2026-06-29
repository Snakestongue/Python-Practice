import pandas as pd

def grade(score):
    if score >89:
        return "A"
    elif score >79:
        return "B"
    elif score>69:
        return "C"
    elif score >59:
        return "D"
    else:
        return "F"
    
df = pd.read_csv("pandas/students.csv")
df["average"] = (df["math"] + df["science"] + df["english"]) / 3
df.sort_values("average", ascending=False).head(1)
df["total"] = df["math"] +df["science"] + df["english"]
df["letter_grade"] = df["average"].apply(grade)
