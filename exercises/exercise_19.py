# random number guessing game

import time, random

while True:
    lower = int(input("enter the lower limit: "))
    if lower <= 0:
        print("lower limit cannot be less than 0!")
    else:
        break

while True:
    upper = int(input("\nenter the upper limit: "))
    if upper <= 0:
        print("upper limit cannot be less than 0!")
    elif upper <= lower:
        print("upper limit has to be greater than the lower limit!")
    else:
        break

random_num = random.randint(lower, upper)

time.sleep(2)
print(f"random number has been generated...")

tries = 0
while True:
    num = int(input("\nyour guess: "))
    if num <= 0:
        print("your guess cannot be less than 0!")
    else:
        tries += 1

        if num == random_num:
            print(f"\ncorrect! you guessed the number in {tries} tries")
            break
        elif num < random_num:
            print("incorrect! the number is higher than your guess!")
        elif num > random_num:
            print("incorrect! the number is lower than your guess!")
