import math
inp = input("Enter your shape: ").lower()

def triangle():
    inputTriangleHeight = float(input("Enter height: "))
    inputTriangleBase = float(input("Enter base length: "))
    print(.5 * inputTriangleBase * inputTriangleHeight)
def circle():
    inputcircleRadius = float(input("Enter radius: "))
    print(math.pi * (inputcircleRadius**2)) 
def Square():
    inputSquare = float(input("Enter length: "))
    print(inputSquare**2)
def Rectangle():
    inputRectLength = float(input("Enter length: "))
    inputRectHeight = float(input("Enter width: "))
    print(inputRectLength * inputRectHeight)
def Para():
    inputParaLength = float(input("Enter length: "))
    inputParaHeight = float(input("Enter width: "))
    print(inputParaLength * inputParaHeight)
def Trapi():
    trapTop = float(input("Enter Top base: "))
    trapBottom = float(input("Enter Bottom base: "))
    trapHeight = float(input("Enter height: "))
    print(((trapBottom+trapTop)/2)*trapHeight)


if inp =="triangle":
    triangle()
elif inp =="square":
    Square()
elif inp =="rectangle":
    Rectangle()
elif inp =="trapezoid":
    Trapi()
elif inp =="parallelogram":
    Para()
elif inp =="circle":
    circle()
else:
    print("Try again")





