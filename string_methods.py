name = input("your name: ")

# returns the length of the given string including spaces
print(len(name))

# returns the first position of given character in the string
# returns -1 if the character is not found
print(name.find("a"))

# returns the last position of given character in the string
# returns -1 if the character is not found
print(name.rfind("a"))

# captilaize the first character
print(name.capitalize())

# capitalize all characters
print(name.upper())

# simplaize all characters
print(name.lower())

# return a true if string only have numbers, else false
print(name.isdigit())

# return true if string only contains alphabatical characters, else false (space does not count)
print(name.isalpha())

# count how many characters are in a string
print(name.count("a"))

# replace any character with given character
print(name.replace("a", "e"))

print(help(str))
