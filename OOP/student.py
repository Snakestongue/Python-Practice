# name = input("Enter a name: ")
# house = input("Enter your house: ")
# print(f"{name} lives at {house}")

def main():
    student = getItems()
    print(f"{student['name']} lives at {student['house']}")

def getItems():
    student ={}
    student["name"] = input("Enter name: ")
    student["house"] = input("Enter house: ")
    return student
if __name__ == "__main__":
    main()

# Tuples - Immutable
# Lists - Mutable
