costumes ={ 
    "vampire cape": 15.00,
    "witch hat": 8.50,
    "zombie mask": 12.75,
    "skeleton suit": 20.00,
    "ghost sheet" :5.25
} 
total = 0
while True:
    inp = input("Which costume you want. Type stop to stop: ").lower()
    if inp == "stop":
        print(f"Your total is {total}")
        break
    elif inp in costumes:
        pass
    else:
        print("Invalid try again")
