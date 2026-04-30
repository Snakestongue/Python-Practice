initial = float(input("Enter your original balance: "))
uD = input("Has your investment been increasing(press I) or decreasing(press D): ").upper()
rate = float(input("Enter the rate your balance has been changing (as percent): "))
time = float(input("How many months have you had the investment: "))

if uD == "I":
    total = initial * (1+(rate*.01))**time
    print(round(total, 2))
elif uD == "D":
     total = initial * (1-(rate*.01))**time
     print(round(total, 2))
else:
     print("Invalid.")