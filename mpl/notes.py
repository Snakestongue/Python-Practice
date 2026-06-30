import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

"""Line Plot"""
# plt.plot(x, y, #line connecting the points
#          color="blue", # color
#          linestyle="--", #style
#          linewidth = 3, #width
#          marker="*" #actual points where x, y intersect
#          ) # plots x,y  (xaxis, yaxis)

"""Scatter plot"""
plt.scatter(x, y, #dots where x, y, intersect
            color="red", #color
            s=100, # size of dot
            marker="s"
            )
"""Labels"""
plt.xlabel("Days") # x axis name
plt.ylabel("Temp") # yaxis name
plt.title("Temp each day") #title of graph
plt.show()