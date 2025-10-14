# calculate the area of a circle

import math

r = float(input("enter the radius of a circle: "))
area = round(math.pi * math.pow(r, 2), 2) # round to 2 decimal places

print(f"\narea of circle (r = {r}): {area} cm")