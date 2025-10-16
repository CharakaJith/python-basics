# list comparision a concise way to create lists in python
# compact and easier to read than traditional lopps
# [expression for value in iterable if condition]

doubls = []

# traditional way of populating the list
for x in range(1, 11):
    doubls.append(x * 2)

print(doubls)

# create list with list comparision
singles = [x * 1 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]


print(singles)
print(triples)
print(squares)

# lists with list comparision
fruits = ["apple", "orange", "banana", "grapes"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruits)
print(fruit_chars)

# list comparision with conditions
numbers = [1, -2, 3, -4, 5, -6, 7, -8]
positives = [num for num in numbers if num >= 0]
negatives = [num for num in numbers if num < 0]

print(positives)
print(negatives)

evens = [triple for triple in triples if triple % 2 == 0]
odds = [triple for triple in triples if triple % 2 == 1]

print(evens)
print(odds)
