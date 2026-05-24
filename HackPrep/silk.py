# Python – Silk Road Tycoon – In Python, create a strategy/trading game where the player leads a caravan across Asia on the Silk Road. 
# Manage supplies, negotiate with cities, survive bandits and weather, and become the richest merchant before winter arrives. 
# The game ends when the caravan successfully returns home or collapses.

import random
import time
progress = 0
supp = 0
cash = 100
neg = 0
bandit = 0
life = 5
storm = False
sand = False
flood = False
weather = "Clear"
print("Welcome to the Silk Road Trade Game. Your goal is to get home! You will face bandits, bad weather and many other surprises on the way!")
print("Welcome. You are now leaving the city of Venice! Your goal is to get to Samarkand. Let's start!")

while True:
    inp = input(f"Progress: {progress} \nSupplies: {supp} \nCash: {cash} \nWeather: {weather} \nLife: {life} \nWould you like to talk to a traveler (t), find supplies (s), fight bandits (f) or travel along the road (r): ").lower()
    if inp == "t":
        x = random.choices(["good", "bad"])
        if x == "good":
            y = supp + random.randint(4, 7)
            print(f"The traveler gave your {y} supplies")
            supp+=y
        else:
            if supp <= 6:
                print("The traveler hit you. You lost a life...")
            else:
                z = random.randint(3, 6)
                print(f"The traveler looted you and took {z} supplies")
                supp-=z
    elif inp == "s":
        for i in range(random.randint(2, 4)):
            print("Searching for materials", "." * (i+1))
            time.sleep(1)
        a = random.randint(1, 3)
        print(f"You found {a} supplies")
        supp+=a
    elif inp =="f":
        amt = random.randint(3, 5)
        side = random.choices(["right", "left"])
        inpFight = input("Select your weapon: \nSword (s) \nBat (b) \nNunchucks (n) \n").lower()
        if inpFight == "s":
            sInpD = input("Attack left (l) or right (r)?").lower()
            if sInpD == "l":
                if side == "right":
                    print(f"Direct contact. You got {amt} supplies")
                    supp+=1
                else:
                    print(f"Miss. You lost 1 life")
                    life-=1

