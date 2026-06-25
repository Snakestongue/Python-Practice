import numpy as np
np.random.seed(10)
arrays = np.random.rand(5)
print(arrays[(arrays<.7) & (arrays>.2)]) #numpy uses &
new_array = np.random.rand(5) *.5 +.2 
print(new_array)
#starts 0-1, multiply by .5 so now 0 - 0.5 + .2 so .2-.7