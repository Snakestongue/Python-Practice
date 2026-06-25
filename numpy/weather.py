import numpy as np
np.random.seed(10)
weather = np.random.randint(50, 101, 7)
print(np.max(weather))
print(np.min(weather))
mean = np.round(np.mean(weather), 2)
print(mean)
print(weather[weather > mean])
print(np.round((weather-32) / (9/5), 2))