# format specifiers {value:flags}

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")#prints price 1 with 2 decimals (.2) and f is float
print(f"Price 2 is ${price2:10}")# the :10 creates 10 spaces between $ and price2
print(f"Price 3 is ${price3:<10}")#<10: left justified, >10 right justified