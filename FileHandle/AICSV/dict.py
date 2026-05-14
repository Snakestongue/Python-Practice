import csv



with open("dictAddy.csv", "a") as file:
    names = ["name", "age", "address"]
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    writer.writerow({
        "name": "bob",
        "age": 30,
        "address": "123 ABC Rd"
    })
with open("dictAddy.csv", "r") as file:
    reader = csv.DictReader(file)
    for x in reader:
        print(x["name"], x["age"])