# calculate hypotenuse of a triangle

import math

a = float(input("enter side a: "))
b = float(input("enter side b: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"\na: {a} and b: {b} then c: {round(c, 2)}")