unit = input("Is the temperature in C/F ")
temp = float(input("What is the temp "))
if unit == "C":
    a = round((temp * 9/5) +32,1)
    print(f"The temp in F is {a}")
elif unit == "F":
    a = round((temp -32) * 5/9,1)
    print(f"The tempeature in C is {a}")
else:
    print(f"{unit} is invalid unit.")