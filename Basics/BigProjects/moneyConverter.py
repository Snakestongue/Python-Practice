currency={
    "USD": 1,
    "EUR": 1.1,
    "JPY": .0067,
    "GBP": 1.25,
    "CAD": .75
}
while True:
    curCur = input("Enter your current currency: ").upper()
    if curCur in currency:
        break
    else:
        print("Invalid")
while True:
    targCur = input("Enter your target currency: ").upper()
    if targCur in currency:
        break
    else:
        print("Invalid")
total = int(input(f"How much in {curCur} do you want to switch to {targCur}?"))
switch = total * currency[curCur]
new = switch /currency[targCur]
rounder = round(new, 3)
print (f"The amount is {rounder}")