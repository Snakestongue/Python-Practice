import math
inp = input("Enter your shape: ").lower()

def triangle(inputTriangleHeight, inputTriangleBase):
    return (.5 * inputTriangleBase * inputTriangleHeight)
def circle(inputcircleRadius):
    return(math.pi * (inputcircleRadius**2)) 
def Square(inputSquare):
    return(inputSquare**2)
def Rectangle(inputParaLength, inputParaHeight):
    return(inputParaLength * inputParaHeight)
def Para(inputParaLength, inputParaHeight):
    return(inputParaLength * inputParaHeight)
def Trapi(trapTop, trapBottom, trapHeight):
   return ((trapBottom+trapTop)/2)*trapHeight


if inp =="triangle":
    inputTriangleHeight = float(input("Enter height: "))
    inputTriangleBase = float(input("Enter base length: "))
    print(triangle(inputTriangleHeight, inputTriangleBase))
elif inp =="square":
    inputSquare = float(input("Enter length: "))
    print(Square(inputSquare))
elif inp =="rectangle":
    inputParaLength = float(input("Enter length: "))
    inputParaHeight = float(input("Enter width: "))
    print(Rectangle(inputParaLength, inputParaHeight))
elif inp =="trapezoid":
    trapTop = float(input("Enter Top base: "))
    trapBottom = float(input("Enter Bottom base: "))
    trapHeight = float(input("Enter height: "))
    print(Trapi(trapTop, trapBottom, trapHeight))
elif inp =="parallelogram":
    inputParaLength = float(input("Enter length: "))
    inputParaHeight = float(input("Enter width: "))
    print(Para(inputParaLength, inputParaHeight))
elif inp =="circle":
    inputcircleRadius = float(input("Enter radius: "))
    print(circle(inputcircleRadius))
else:
    print("Try again")





