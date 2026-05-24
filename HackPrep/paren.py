#Python - Parthenon - In Python, create a game where the player is an ancient builder that helped to build the Parthenon.
# The game must end when the Parthenon is completely built. Best gameplay experience wins!


import random
import time

sand = 0
marble = 0
gold = 0
life = 3
moves = 0
progress = 0
print("Welcome to Parthenon. Your goal is to get 10 pieces of sand, marble and gold without losing all of your lives in the shortest amount of moves possible!")
while True:
    if life == 0:
        print("You died! Try again next time!")
        break
    inpA = input(f"Sand: {sand} \nMarble: {marble} \nGold: {gold} \nLife: {life} \nMoves: {moves} \nProgress: {progress}% \nWould you like to search for items(s), build(b), fight(f): ").lower()
    if inpA == "s":
        for i in range(random.randint(3, 6)):
            print("Searching for materials" +"." * (i+1))
            time.sleep(random.randint(1, 3))
        
        select = random.choice(["sand", "marble", "gold"]) #the material, choice selects variable value NOT string
        totalSelect = random.randint(1, 3) #the amount
        if select == "sand":
            sand+=totalSelect
        elif select == "gold":
            gold+=totalSelect
        elif select == "marble":
            marble+=totalSelect
        print(f"You found {totalSelect} of {select}")
        moves+=1
    elif inpA == "b":
        if (gold>=2 and marble>=2 and sand>=2 and progress==80):
            print("You completely built the Parthenon! Congrats you won!")
            progress = 100
            break
        elif (gold>=2 and marble>=2 and sand>=2):
            progress += random.randint(10, 30)
            print(f"You built {progress}% of the Parthenon!")
            sand-=2
            gold-=2
            marble-=2
        else:
            print("Need a minimum of 2 gold, marble & sand to start building!")
    elif inpA == "f":
        #temp = True
        em = random.choice(["dL", "dR", "aL", "aR"])
        choice = random.choice(["sand", "marble", "gold"])
        amount = random.randint(3, 5)
        inpF = ""
        while True:
            inpF = str(input("You have selected to fight. \nYour goal is to fight the monster for materials. \nWould you like to attack left(al), attack right(ar), defend right(dr) or defend left(dl): ")).lower()
            #AL
            if inpF == "al":
                if em == "aL":
                    print(f"Both attacked at the same time. You lost a life but got {amount} pieces of {choice}")
                    life-=1
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                elif em =="aR":
                    print("He attacked right. You did not gain any materials or lose a life.")
                elif em =="dL":
                    print("He defended your attack. You lose a life.")
                    life-=1
                elif em == "dR":
                    print(f"You attacked him successfully! You got {amount} pieces of {choice}")
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                break
            #AR
            elif inpF == "ar":
                if em == "aL":
                    print("He attacked left. You did not gain any materials or lose a life.")
                elif em =="aR":
                    print(f"Both attacked at the same time and place. You lost a life but got {amount} pieces of {choice}")
                    life-=1
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                elif em =="dR":
                    print("He defended your attack. You lose a life.")
                    life-=1
                elif em == "dL":
                    print(f"You attacked him successfully! You got {amount} pieces of {choice}")
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                break
            #DR
            elif inpF == "dr":
                if em == "aL":
                    print("He attacked left. You did not gain any materials or lose a life.")
                elif em =="aR":
                    print(f"You defended his attack! You got {amount} pieces of {choice}")
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                elif em =="dR" or em=="dL":
                    print("He defended as well. You did not gain any materials or lose a life.")
                break

            elif inpF == "dl":
                if em == "aR":
                    print("He attacked right. You did not gain any materials or lose a life.")
                elif em =="aL":
                    print(f"You defended his attack! You got {amount} pieces of {choice}")
                    if choice == "sand":
                        sand+=amount
                    elif choice =="gold":
                        gold+=amount
                    else:
                        marble+= amount
                elif em =="dR" or em=="dL":
                    print("He defended as well. You did not gain any materials or lose a life.")
                break
            else:
                print("Invalid choice. Try again")
        moves+=1
    else:
        print("Please pick a valid action!")
