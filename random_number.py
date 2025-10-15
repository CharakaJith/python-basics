# random method has number of methods related to number related operations

import random

# generate whole random integer between and including 1 and 6
num = random.randint(1, 6)

# generate whole random integer between and including 1 and 20
num = random.randint(1, 20)

# generate a random decimal number between 0 and 1
num = random.random()

print(num)

# select a random option from a list/tuple
options = ("left", "right", "front", "back")
choice = random.choice(options)

print(choice)

# shuffle the sequence of a list
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
shuffled = random.shuffle(cards)

print(cards)
