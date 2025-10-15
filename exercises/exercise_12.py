# compound interest calculator

import math

principle = 0
time = 0
rate = 0

while True:
    principle = float(input("\nenter principle amount: "))
    if principle < 0:
        print("principle cannot be less than 0!")
    else:
        break
        
while True:
    rate = float(input("\nenter rate amount: "))
    if rate < 0:
        print("rate cannot be less than 0!")
    else:
        break
        
while True:
    time = float(input("\nenter number of years: "))
    if time < 0:
        print("number of years cannot be less than 1!")
    else:
        break
        
amount = principle * math.pow((1 + (rate / 100)), time)

print(f"your total amount will be ${amount:.2f}")
    