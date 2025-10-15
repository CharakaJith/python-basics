# logical operators evaluate multiple conditions (and, or, not) 
# or: at least one condition must be true
# and: both conditions must be true
# not: invert the condition

temp = 30
is_raining = False
is_sunny = True

if temp > 35 or temp <= 0 or is_raining:
    message = "outdoor event is cancelled!"
else:
    message = "outdoor event is still scheduled!"

print(f"{message}")

if temp >= 28 and is_sunny:
    message = "it is hot and sunny outside!"
elif temp >= 28 and not is_sunny:
    message = "it is hot but not sunny outside!"
elif temp <= 0 and is_sunny:
    message = "it is cold but sunny outside!"
else:
    message = "it is cold and dark outside!"

print(f"\n{message}")
    


