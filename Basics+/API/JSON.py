import json
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
city = str(input("Enter your city: "))
data = {
    "name": name,
    "age":age,
    "city":city
}

x = json.dumps(data)
#json.loads(data) is JSON to python
print(x)