import random
number = random.randint(1,100)
inp = int(input("Guess the number: "))
while inp != number:
    if inp > number:
        print("Too high")
        inp = int(input("Guess the number: "))

    elif inp <number:
        print("Too low")
        inp = int(input("Guess the number: "))

print(f"Good job. The number was {number}")