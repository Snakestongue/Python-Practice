from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("scale", StandardScaler()), #(name, object) --> can use any name
    ("model", LinearRegression())
])
#Assembly line --> Raw Data -> Pipeline --> Scale --> Model --> Output
#when you do .fit() it automatically uses pipeline
#.fit()
    #Step 1: Values are scaled
    #Step 2: Model uses the scaled values and gets trained
#.predict()
    #do pipeline.predict(data) since it uses the pipeline now
