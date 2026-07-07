def add(a: float, b: float, c:float, d:int)->float:
    return (round(a+b+c, d))

def sub(a:float, b:float, c:float, d:int)->float:
    return (round(a-b-c, d))

def multi(a:float, b:float, c:float, d:int)->float:
    return (round(a*b*c, d))

def div(a:float, b:float, c:float, d:int)->float:
    if b == 0 or c == 0:
        raise ValueError("Can't divide by 0!") #Raise, allows you to like change the exception!
    return round(a / b / c, d)

while True:
    try:
        x = float(input("Enter number 1: "))
        y = float(input("Enter number 2: "))
        z = float(input("Enter number 3: "))
    except ValueError:
        print("Not a number! ")
        continue
    try:
        r = int(input("Enter how many number to round to! "))
    except ValueError:
        print("Not a whole number! ")
        continue
    else:
        print(add(x, y, z, r))
        print(sub(x, y, z, r))
        print(multi(x, y, z, r))
        try:
            print(div(x, y, z, r))
        except ValueError as e:
            print(e)
        break

print("Thanks for using this!")