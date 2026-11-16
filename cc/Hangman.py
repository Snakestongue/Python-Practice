import random
lists = ["program", "java", "python", "coding", "computer"]
word = random.choice(lists)
guessed_letters = set() 
"""
A set is a type of dataset unique to python. It allows no duplicates & is unordered (can't use indexing)!
"""
lives = 5
while lives > 0:
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ") #Instead of ending on a newline, just end on a space!
        else:
            print("_", end=" ")
    won = True
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break
    if won:
        print("You win! The word was:", word)
        break
    inp = input("Enter a letter: ").lower().strip()
    if len(inp) != 1 or not inp.isalpha():
        print("Please enter a single valid letter (a-z).")
        continue
    if inp in guessed_letters:
        print(f"You already guessed '{inp}'! Try a different letter.")
        continue
    guessed_letters.add(inp)
    if inp in word:
        print(f"Correct! The letter {inp} is in the word!"+ " You have",lives,"lives left")
    else:
        lives -= 1
        print(f"Incorrect! You have {lives} lives left.")
if lives == 0:
    print("Game over! The word was:", word)