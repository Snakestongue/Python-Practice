
while True:
    try:
        x = int(input("Enter a number! "))
    except ValueError:
        print("Not a number!")
    else:
        print(f"Your number was {x}")
        break