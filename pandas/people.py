import pandas as pd
df = pd.read_csv("pandas/people.csv")
df["department"] = df["department"].str.lower() # makes depatments all lowercase

df["age"] = pd.to_numeric(df["age"], errors="coerce") #.to_numeric converts values into numbers, errors="coerce" means errors = Nan instead of breaking
df =df[df["age"]>=0] # keeps all above 0
df.dropna(axis=0, subset=["age"], inplace=True) 
# dropna removes rows with Nan
# subset selects the column, axis=0 selects rows (1 is columns)

df.dropna(axis=0, subset=["department"], inplace=True)# same as above
df = df[df["email"].str.endswith(".com")] # keeps only if the email ends with .com

df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce") #.to_datetime converts values into YYYY-MM-DD
df.dropna(axis=0, subset=["join_date"], inplace=True) # same as above

df = df.drop_duplicates(subset=["name"]) # deletes duplicate names
df = df[df["salary"]<300000] # keeps all salaries under 300,000
df["id"] = range(1, len(df)+1) # makes id's from 1 to length of csv + 1

print(df)