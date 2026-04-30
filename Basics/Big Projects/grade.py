fName = []
lName = []
grades = []

def run(fN, lN, grade):
    fName.append(fN)
    lName.append(lN)
    grades.append(grade)
    return fN + " " + lN + " has a " + grade

while True:
    fN = input("Enter first name: ")
    lN = input("Enter last name: ")
    grade = input("Enter current grade student has: ") 
    run(fN, lN, grade)  
    conti = input("Would you like to stop inputting students (Y for stop, N for continue, P for print all students): ").upper()
    if conti == "Y":
        break
    elif conti == "P":
        for i in range(len(fName)):
            print(fName[i] + " " + lName[i] + " has a " + grades[i])
    else:
        continue