import random


inp = input("Would you like to roll(say yes):  ").lower()
while inp == "yes":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        total = dice1+dice2
        print(f"You rolled a {dice1} and a {dice2} for a total of {total}")
        inp = input("Would you like to roll(say yes)").lower()
