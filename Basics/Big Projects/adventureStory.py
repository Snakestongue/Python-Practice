num1 = input("You go trick or treating. There's a scary house? Do you knock or run").lower()
while True:
    if num1 == "knock":
        num1_2 = input("You knock. The door opens but no one is inside. Do you go inside or run(say inside or run)").lower()
        if num1_2 == "inside":
            num1_2_1 = input("You walk through the house and see something in the backyard and in the garage? Where do you go").lower()
            if num1_2_1 == "garage":
                print("Inside the garage there's a rat and nothing else. You leave the house cause it was a false alarm.")
            else:
                print("In the backyard there was a man in all black. He punches you and runs away. You sustain heavy life-long injuries")
        else:
            num1_2_2 = input("You try to run but you trip and fall. Than a male in all black walks up. Do you run or listen to him").lower()
            if num1_2_2 == "listen":
                print("He says get up, and you do but than punches you and gives you life-long injuries")
            else:
                print("you run away and get home safetly. He doesn't follow you")
    else:
        num12 = input("You run but some random kid pushed you accidently. You fall down and then some kids start laughing at you. Do you stay down or get up?").lower()
        if num12 == "get up":
            print("You get up and you take the kids candies")
        else:
            print("The kids leave you alone since they think you're injured.")