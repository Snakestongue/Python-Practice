sum = 0
done = False
while done == False:
    inp = input(str("What would you like? cake, brownie, sandwich, wrap, cookie:  ")).lower()
    if inp == "cake":
        sum += 4
        print("You ordered a cake")
    elif inp == "cookie":
        sum += 3
        print("You ordered a cookie")
    elif inp == "sandwich":
        sum += 7
        print("You ordered a sandwich")

    elif inp == "wrap":
       sum += 6
       print("You ordered a wrap")

    elif inp == "brownie":
        print("You ordered brownies")
        sum += 3
    elif inp == "done":
        print(f"${sum}")
        done=True
    else:
        print("Invalid")
        done=False

