#This folder is just what AI has taught me for CSV
import csv



with open ("addy.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["hi", 30, "abc Plain Rd"])

with open("addy.csv", "r", newline="") as file:
    read = csv.reader(file)
    for x in file:
        print (x.rstrip())