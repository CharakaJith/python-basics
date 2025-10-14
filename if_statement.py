# used to execute code only if a certain condition is True, else run a different code
# follows standard logical evaluation (can combine with and, or, not)

# with numberic values
age = int(input("enter your age: "))

if age >= 18 and age < 100:
    message = "you are signed up!"
elif age < 0:
    message = "you haven't been born yet!"
elif age >=100:
    message = "you should be dead by now!"
else:
    message = "you must be at least 18 years old!"
    
print(f"\n{message}")

# with string values
response = input("would you like some food? (y/n): ")

if response.capitalize() == "Y":
    message = "have some food!"
else:
    message = "no food for you!"
    
print(f"\n{message}")

# validate name
name = input("your name: ")

if name == "":
    message = "please enter a valid name!"
else:
    message = f"welcome, {name}"
   
print(f"\n{message}") 

# with boolean values
is_online = True

if is_online:
    status = "online"
else:
    status = "offline"
    
print(f"\nthe user is {status}.....")
