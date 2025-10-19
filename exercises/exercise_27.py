# substitution encryption program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# encryption
plain_text = input("enter a message to input: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"\noriginal message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# decrypt
encrypted_text = input("\nenter a message to decrypt: ")
text = ""

for letter in encrypted_text:
    index = keys.index(letter)
    text += chars[index]

print(f"\nencrypted message: {encrypted_text}")
print(f"noriginal message: {text}")
