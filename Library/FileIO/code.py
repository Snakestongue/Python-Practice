name = str(input("What's your name?"))

#file, 
# "w"--> Rewrite entire file
# "a" --> Append to file
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

#Shortcut for above
name = []
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
with open("names.txt", "r") as file:
    for x in file:
        name.append(x.rstrip())
for x in sorted(name):
    print(f"{x}")
        


