weight = float(input("Enter your weight: "))
unit = input("KG or LB: ")
if unit == "KG":
    weight = weight *2.205
    unit = "LBS"
    print(f"Your weight is {round(weight, 3)} {unit}")
elif unit =="LB":
    weight = weight /2.205
    unit = "KG"
    print(f"Your weight is {round(weight, 3)} {unit}")
else:
    print(f"{weight} was not valid")
    
