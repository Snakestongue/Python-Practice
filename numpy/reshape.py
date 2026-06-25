import numpy as np
np.random.seed(10)
arrays = np.random.randint(1, 25, 24)
# print(arrays)
# print(arrays.reshape(2, -1))
# print(arrays.reshape(3, -1))
# print(arrays.reshape(6, -1))
# print(arrays.reshape(8, -1))
# print(arrays.reshape(12, -1))

print(arrays.reshape(4, -1))
g = arrays.reshape(4, 6)
print(g[3, 3])