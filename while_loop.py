# while loop executes a code block while some condition is true

# do something while condition is true, else exit
name = input("your name: ")

while len(name) == 0:
    print("please enter your name!")
    name = input("\nyour name: ")
    
age = int(input("\nenter your age: "))

while age < 0:
    print("age cannot be less than 0!")
    age = int(input("\nenter your age: "))
    
print(f"\nwelcome, {name}! you are {'an adult!' if age >= 18 else 'a child!'}")

# do something while the condition is not true, exits once the condition is true
food = input("\nenter a food you like (q to quit): ")

while not food.capitalize() == "Q":
    print(f"you like {food}")
    food = input("\nenter a food you like (q to quit): ")
    
print("\nbye.....")

# use conditional statements for the loop conditions
num = int(input("\nenter a number between 1 - 10: "))

while num < 1 or num > 10:
    print("please enter a valid number!")
    num = int(input("\n enter a number between 1 - 10: "))
    
print(f"\nyour number is {num}")