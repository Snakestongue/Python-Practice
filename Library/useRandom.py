from random import choice
from random import randint
from random import shuffle
ourList = ["red", "green", "blue"]
shuffleCards = shuffle(ourList)
for x in ourList:
    print(x)

print(choice(["hi", "bye"]))
print(randint(1, 20))