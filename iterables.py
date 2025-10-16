# iterable an object or collectrion that can return one if its elemants at a time
# allows to be iterated over in a loop

# a list is an iterable
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, end=" ")
print()

for num in reversed(nums):
    print(num, end=" - ")
print()

# tuple is an iterable
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for num in numbers:
    print(num, end=" ")
print()

# sets are also iterable (sets cannot be revered)
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit, end=" ")
print()

# strings are iterable
name = "John Doe"

for char in name:
    print(char, end=" ")
print()

# dictionaries are iterable
capitals = {
    "Sri Lanka": "Kotte",
    "Japan": "Tokyo",
    "Chine": "Beijin",
    "Russia": "Moscow",
}

# this would only return the keys, not values
for capital in capitals:
    print(capital, end=" ")
print()

for key, value in capitals.items():
    print(f"capital of {key} is {value}")
