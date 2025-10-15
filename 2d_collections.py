# 2d lists or list of lists is a list made out of list
# cart = [[], [], [], []]

# creating lists
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["carrots", "potatoes", "beets"]
meats = ["chicken", "beef", "pork", "turkey", "fish"]

# creating a 2d list
groceries = [fruits, vegetables, meats]

# printing 2d lists
print(groceries)

for item in groceries:
    print(item)

# print list inside the 2d list
print(groceries[1])

# print list item inside the 2d list
print(groceries[2][3])
