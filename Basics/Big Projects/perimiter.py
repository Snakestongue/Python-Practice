import math
def rect(length, width):
    return (length * 2) + (width * 2)
def tri(side1, side2, side3):
    return side1 + side2 +side3
def circle(radius):
    return (2 * math.pi * radius)
def square(side):
    return (4*side)
def para(length, width):
    return (length * 2) + (width * 2)
def trap(side1, side2, side3, side4):
    return(side1+side2+side3+side4)

inp = input("Which shape to calculate perimiter?").lower()
if inp =="rectangle":
    length = float(input("Length of side please: "))
    width = float(input("Width of side please: "))
    print(rect(length, width))
elif inp =="triangle":
    side1 = float(input("Length of side please: "))
    side2 = float(input("Length of side please: "))
    side3 = float(input("Length of side please: "))
    print(tri(side1, side2, side3))
elif inp =="circle":
    radius = float(input("Length of radius please: "))
    print(circle(radius))
elif inp =="square":
    side = float(input("Length of side please: "))
    print(square(side))
elif inp =="para":
    length = float(input("Length of side please: "))
    width = float(input("Width of side please: "))
    print(para(length, width))
elif inp =="trapizoid":
    side1 =float( input("Length of side please: "))
    side2 = float(input("Length of side please: "))
    side3 = float(input("Length of side please: "))
    side4 = float(input("Length of side please: "))
    print(trap(side1, side2, side3, side4))
else:
    print("invalid")

   