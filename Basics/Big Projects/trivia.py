score = 0
inp = input("Which of the following colors are not warm? Red, Orange, Yellow or Green").lower()
if inp == "green":
    score+=1
inp = input("Which car is not Japanese? Toyota, Honda, Volkswagon or Mazda").lower()
if inp == "volkswagon":
    score+=1
inp = input("Which is not a real coding language? Python, Kotlin, Crepmen or CSS").lower()
if inp == "crepmen":
    score+=1
inp = input("Which company does not make TVs? Apple, Samsung, Insginia or LG").lower()
if inp == "apple":
    score+=1
inp = input("Which language is generally not spoken in India? Hindi, Punjabi, English, Spanish").lower()
if inp == "spanish":
    score+=1
print(f"Nice try. You got {score} points.")