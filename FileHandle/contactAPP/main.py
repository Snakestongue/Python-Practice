import csv
import os
fileExisit = os.path.exists("file.csv")


def addRow(name, age, city):
    with open ("file.csv", "a", newline="") as file:
        names = ["name", "age", "city"]
        w = csv.DictWriter(file, fieldnames=names)
        if not fileExisit:
            w.writeheader()
        w.writerow({
            "name": name,
            "age": age,
            "city":city
        })
def viewRow():
    pass

def deleteRow():
    pass

def main():
    pass