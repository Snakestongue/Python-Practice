from statistics import mean
from statistics import median
import statistics
ourList = [19, 28, 37, 46, 55, 66, 77, 88, 99, 101, 19]
print(round(mean(ourList), 2))
print((median(ourList)))
print(statistics.median_high(ourList))
print(statistics.median_low(ourList))
print(statistics.mode(ourList))