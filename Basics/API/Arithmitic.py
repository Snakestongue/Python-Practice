#friends * or / or + or - or ** or % add =1
# ** = exponent to power of 2
# % remainder
# Math = round(x), abx(x), pow(x, y), max/min(x,y,z)
# pow: 4*4*4(exponent)
 
# Following are import math
# math.sqrt, math.pi, math.ceil, math.floor
# Ceil: Round up no matter number (9.1 -> 10).
# Floor: Round down no matter number (9.9 >9)

import math
x = float(input("What is the length of a "))
y = float(input("What is the length of b "))
super =  math.sqrt(pow(x,2) + pow(y,2))
print(f"The area is {super}")