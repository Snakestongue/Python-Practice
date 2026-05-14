with open("example.txt", "a") as file:
    file.write("\n hi")

with open("example.txt", "r") as file:
    #file.write("hi")
    for x in file:
        print(x.strip())