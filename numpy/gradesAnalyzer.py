import numpy as np
np.random.seed(10)
arrays = np.random.randint(70, 101, 10) #end excluded
print(arrays)
print(np.mean(arrays))
print(np.sum(arrays))
print(np.max(arrays))
print(np.min(arrays))
print(arrays[0])
print(arrays[-1])
print(arrays[::2])
print(arrays+5)
print(arrays[arrays>80])

