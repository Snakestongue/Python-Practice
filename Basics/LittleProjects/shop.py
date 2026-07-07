dict ={
    "chocolate":2.75,
    "candy":1.50,
    "candy corn": 1.00,
    "white chocolate":3.00
}
inp = input("Which item would you like to purhchase "+", ".join(dict.keys())+" ")
while inp!="stop":
    if (inp in dict):
        pass