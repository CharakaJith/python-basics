# indexing means accessing elements of a sequence using []
# [start : end : step]

credit_card = "1234-5678-9101-1121"

# print the character in position 3
print(credit_card[3])

# print character 0 to 6 digits
# print(credit_card[0:6])
print(credit_card[:6])

# print character 6 to 11
print(credit_card[6:11])

# print character 11 to end
print(credit_card[11:])

# print the last character
# in here string is counting from the end of the string to the start
print(credit_card[-1])

# print every 2nd character
print(credit_card[::2])

# get last 4 digits
last_digits = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")