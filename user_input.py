# input() function will prompt the user to enter data
# enter/return key press accepts the data as a string

name = input("Enter your name: ")

print(f"\nWelcome, {name}")

ageStr = input("How old are you: ")
age = int(ageStr)

print(F"\n{'Too young to enter!' if age <= 18 else 'Please come in!'}")