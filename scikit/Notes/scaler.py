from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder, Normalizer, Binarizer,PolynomialFeatures, RobustScaler, QuantileTransformer, PowerTransformer
import pandas as pd

"""STANDARD"""
standData = pd.DataFrame({
    "ages": [10, 20, 30, 40, 50]
})
standardScale = StandardScaler()
print(standardScale.fit_transform(standData))
# creates standard deviations from the mean for comparsion with other data

"""MINMAX"""
minmaxData = [
    [10],
    [20],
    [30],
    [40]
]
minMaxScale = MinMaxScaler()
print(minMaxScale.fit_transform(minmaxData))
#creates and scales values from 0-1

"""Label Encoder"""
labelData = ["Red", "Green", "Blue", "Green"]
encoder = LabelEncoder()
print(encoder.fit_transform(labelData)) 
#scales alphabetically so blue is 0, green is 1, red is 2

"""One Hot"""
cities=[
    ["New York"],
    ["Boston"],
    ["Chicago"]
]
oneEncoder = OneHotEncoder(sparse_output=False)
print(oneEncoder.fit_transform(cities))
#does # of rows by  # of unique
# 1 is = to selected city, 0 is not

"""Normalization"""
normalData = [
    [4, 1],
    [2, 3],
    [5, 3]
]
normalizer = Normalizer()
print(normalizer.fit_transform(normalData))
#takes data and turns it into a decimal length for comparision

"""Binarization"""
binaryData = [
    [1],
    [2],
    [3]
]
binary = Binarizer(threshold=2)
print(binary.transform(binaryData))
#if above threshold, it's 1, if less then or equal to threshold it's 0

"""Polynomial Features"""
polyData = [
    [3], 
    [5], 
    [7]
]
poly = PolynomialFeatures(degree=2)
print(poly.fit_transform(polyData))
# Prints 1, x, x^degree leading up to the value 
#EX: If degree = 5, it's giving 1, x, x^2, x^3, x^4, x^5

"""Robust Scaler"""
robustData = [
    [1],
    [2],
    [3],
    [100]
]
scaler = RobustScaler()
print(scaler.fit_transform(robustData))
#uses median and IQR, less affected by outliers (value-median)/IQR
# positive above median, negative below median

"""Quantile"""
quantData = [
    [1],
    [2],
    [3],
    [100]
]
quant = QuantileTransformer(output_distribution="normal")
print(quant.fit_transform(quantData))
#does percentile (equally spaced) then inverse of normallcdf, reduces magnitude of outliers

""""Power Transformer"""
powerData = [
    [1],
    [2],
    [4],
    [8],
    [16]
]
power = PowerTransformer()
print(power.fit_transform(powerData))
#compressed via power (idk)