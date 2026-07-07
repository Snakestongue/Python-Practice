conversion = {
    "meter":1,
    "foot":3.28,
    "centimeter":100,
    "kilometer":.001,
    "inch": 39.37
}

while True:
    curConv = str(input("Which measurment do you currently have?")).lower()
    if curConv in conversion:
        break
    else:
        print("invalid")


while True:
    targConv = str(input("Which measurment do you want to switch to?")).lower()
    if targConv in conversion:
        break
    else:
        print("invalid")

number = float(input(f"How many {curConv} do you currently have"))
tempnew = (number / conversion[curConv])
new = (tempnew * conversion[targConv])
rounder = round(new, 3)
print(f"You now have {rounder}")
