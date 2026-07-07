import random
x = random.randint(1, 100)
tries = 0
inp = int(input("Guess the number 1-100: "))
while (inp != x):
    tries+=1
    print("Too high") if inp>x else print("Too low")
    inp = int(input("Guess the number 1-100: "))

print("You got it in", (tries+1), "tries. The number was", x)