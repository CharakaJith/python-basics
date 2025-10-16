# used to test if a value or variable is found in a sequence (string, list, tuple, set or dictionary)
# in     : return True if value is in a sequence, else False
# not in :return True if value is NOT in a sequence, else False

# string
word = "apple"

## check if char a is in the word
print(True if "a" in word else False)

## check if char a and t is NOT in the word
print(True if "a" not in word else False)
print(True if "t" in word else False)

while True:
    char = input("your character: ")
    if char.upper() not in word.upper():
        print("guess again!")
    else:
        print(f"guessed correctly! the word is {word}")
        break

## validate string
email = "john@gmail.com"

if "@" in email and "." in email:
    print("valid email!")
else:
    print("invalid email!")

# set
students = {"Jane", "John ", "Joe", "Bob"}

name = input("enter student name: ").capitalize()

if name in students:
    print(f"student {name} found!")
else:
    print(f"student {name} was not found!")

# dictionary
grades = {"Jane": "A", "John": "C", "Joe": "A+", "Bob": "D-"}

name = input("enter student name: ").capitalize()

if name in grades.keys():
    print(f"student {name} got: {grades[name]}")
else:
    print(f"student {name} was not found!")
