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
print(arrays[1::2]) #start:end:step

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

