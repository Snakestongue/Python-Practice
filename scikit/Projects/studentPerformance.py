from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, QuantileTransformer, PowerTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
df = pd.read_csv("scikit/studentPerformance.csv")
X = df[[
    "Math",
    "Science",
    "English",
    "Attendance",
    "Study_Hours_Per_Week",
    "Sleep_Hours"
]]
Y = df["average"]

xTrain, xTemp, yTrain, yTemp = train_test_split(
    X, Y, random_state=11, test_size=.3
)
xTest, xModel, yTest, yModel = train_test_split(
    xTemp, yTemp, random_state=12, test_size=.5
)

models = {
    "Linear": LinearRegression(),
    "Ridge": Ridge(alpha=1),
    "Lasso": Lasso(alpha=.2),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=4,
        random_state=11 
    ),
    "Gradient": GradientBoostingRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=.1,
        random_state=11
    )
}
scalers = {
    "Standard": StandardScaler(),
    "MinMax": MinMaxScaler(),
    "Robust": RobustScaler(),
    "Quantile": QuantileTransformer(),
    "Power": PowerTransformer()
}
r2scores = []
for name, mod in models.items():
    for scale_name, scaler in scalers.items():

        pipeline = Pipeline([
            ("scale", scaler),
            ("model", mod)
        ])
        pipeline.fit(xTrain, yTrain)
        predict = pipeline.predict(xModel)
        r2scores.append((name, scale_name, r2_score(yModel, predict)))
        #print(name, scale_name, r2_score(yModel, predict))
        #print(mod.coef_ or mod.feature_importances)
        
        

best = max(r2scores, key=lambda x: x[2])
print(best)

"""NOTES"""
#use transform (not fit_transform) for test data
#don't need fit_transform since it's automatic in pipeline :)
