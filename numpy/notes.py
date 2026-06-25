import numpy as np

"""1D"""
arrays = np.array([10, 20, 30, 40, 50])

print(arrays.shape) #shape, 5,
print (arrays.ndim) #dimension, 1
print (arrays.size) #size, 5

"""2D"""
multi_array = np.array([
    [1,2,3],
    [4, 5, 6]
])
print (multi_array.shape)
print (multi_array.ndim)

"""Quicky"""
print(np.zeros((2, 3))) #could be np.ones

"""Range/Space"""
print(np.arange(0, 10, 2)) #start(include), stop(exclude), step
print(np.linspace(0, 1, 5)) #start, stop, number of numbers (0, .25, .5, .75, 1)


"""Indexing"""
print(arrays[-1])
print(multi_array[0, 2])

"""1D Slicing"""
print(arrays[1::2]) #start:end(exclude):step

"""2D Slicing"""
print(multi_array[:, 0]) #rows, columns
# The colon(:) selects all
#1D slicing can be used inside too

"""Operation """
a = np.array([1, 2, 3])
b = np.array([4, 6, 8])
print(a+b) #adds up each column so 5, 8, 11, same thing with -, *, /
print(a+20) #adds each item in the array +20, same thing with -, *, /

"""Functions"""
c = np.array([1, 2, 3, 4, 5, 6])
print(np.sum(c)) #also have mean, median, max, min

"""2D Functions"""
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(np.sum(d)) #sum of all elements
print(np.sum(d, axis = 1)) #0 = sum by columns, 1 sum by rows


"""Reshape"""
e = np.array([1, 2, 3, 4, 5, 6])
print(e) 
f = e.reshape(2, 3) 
#-1, is like auto like CSS(10% 10% auto), except using -1 instead of auto
#x.reshape(rows, columns)
print(f)

"""Random"""

random0 = np.random.rand() # random 0-1 decimal,
random1= np.random.rand(5) #the 5 generates 5 random numbers
random2 = np.random.rand(5, 3) #generates a 5 by 3 (15) random numbers 0-1
random3 = np.random.randint(1, 10, 5) #low, high(exclude), size --> could print smth like 3, 7, 9, 1, 4
random4 = np.random.randint(1, 10, (2, 3)) # same thing by 2D so 2 by 3 box with 6 random ints from 1-9

np.random.choice(e, 3) #selects random choice from array, or 3
np.random.choice(e, 3, replace=False) #choices cannot be repeated b/c replace =False
np.random.shuffle(e) #randomizes e and modifies the orginaol array
np.random.randn(5) #generates numbers around 0, 5 times

np.random.seed(5) #starting point, if you decide seed (any number) it will always geenrate the same random number
print(np.random.rand(3)) # review

dataset = np.random.rand(100, 3) #creates random dataset with 100 rows, 3 columns 


"""Types"""
print(e.dtype)
g = np.array([1, 3, 5], dtype=float) #dtype is just the type
print(g)

"""Filtering (if statements basically)"""

h = np.array([1, 2, 3, 4, 5, 6])
print(h>3) #prints true/false, if you add h[h>3], it will print the actual values

"""Combine"""
i = np.array([
    [1, 2, 3],
    [7, 8, 9]
])
j = np.array([
    [4, 5, 6],
    [10, 11, 12]
])
# print(np.concatenate([i, j])) # 1d combine

print(np.vstack([i, j]))  #2d combine vertical
print(np.hstack([i, j])) # 2d combine, horizontal