students = []
with open("text.csv") as file:
    for x in file:
        name, house = x.rstrip().split(",")
        student = {
            "name": name, 
            "house": house
        }
        students.append(student)

for student in (students):
    print(f"{student['name']} is in {student['house']}")