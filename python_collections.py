# collections are a single variable used to store multiple values
# List  = [] = ordered and changeable, duplicates are OK
# Set   = {} = unordered and immutable, can be added and removed, NO duplicates
# Tuple = () = ordered and unchangable, duplicated are OK, and faster

# List
fruits = ["apple", "banana", "orange", "coconut"]

## print the full lits
print(fruits)

## print reverse
print(fruits[::-1])

## print a value at a given position
print(fruits[2])

## print every second value
print(fruits[::2])

## use for loop to iterate collection values
for fruit in fruits:
    print(fruit, end=" ")

## see list methods. this will show the methods that can be accessed by the list
print(dir(fruits))

## check if value is in list
print("apple" in fruits)
print("pineapple" in fruits)

## change value by index
fruits[0] = "pineapple"
fruits[1] = "kiwi"

## add a new value to the end list
fruits.append("apple")

## add a new value to the given position. the existing values will be shift to right
fruits.insert(2, "grapes")

## remove by value
fruits.remove("kiwi")

## sort a list by alphabetical order
fruits.sort()

## reverse the order by placed position
fruits.reverse()

## remove all the elemants of the list
# fruits.clear()

## return the index of a value
print(fruits.index("grapes"))

## count how many items are in the list
print(fruits.count("apple"))
print(fruits.count("kiwi"))

print("\n\n")

# Sets
cities = {"colombo", "kandy", "mathara", "kottawa"}

## print a set (the values are changed on each iteration, not on the order its defined)
print(cities)

## remove by element
cities.remove("kandy")

## remove the first element (going to random)
cities.pop()

## add existing value
cities.add("colombo")

print(cities)

print("\n\n")

# Tuples
colors = ("red", "green", "blue", "black", "white", "black")

## find length of a tuple
print(len(colors))

## print a tuple
print(colors)

## find index of a value
print(colors.index("blue"))

## find how many elements in the tuple by value
print(colors.count("black"))
