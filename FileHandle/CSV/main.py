import csv
students = []
with open("text.csv") as file:
    reader = csv.DictReader(file)
    for x in reader:
        students.append({"name": x[0], "home": x[1]})



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")