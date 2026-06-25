#each column, diff product
import numpy as np
np.random.seed(10)
arrays = np.random.randint(5, 11, (5, 3))
print(arrays)
print("Product A total: ", np.sum(arrays[:, 0]))
print("Product B total: ", np.sum(arrays[:, 1]))
print("Product C total: ", np.sum(arrays[:, 2]))
# max_array = np.array([np.sum(arrays[:, 0]), np.sum(arrays[:, 1]), np.sum(arrays[:, 2])])
# print("Best selling product: ", np.max(max_array))

print("Day 1 total: ", np.sum(arrays[0, :]))
print("Day 2 total: ", np.sum(arrays[1, :]))
print("Day 3 total: ", np.sum(arrays[2, :]))
print("Day 4 total: ", np.sum(arrays[3, :]))
print("Day 5 total: ", np.sum(arrays[4, :]))