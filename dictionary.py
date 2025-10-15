# dictionary is a collection of key value pairs (like JSON)
# {key : value}
# ordered and changable, no duplicates

capitals = {
    "USA": "Washington DC",
    "Sri Lanka": "Jayawardenapura Kotte",
    "China": "Beijing",
    "India": "New Delhi",
    "Russia": "Moscow",
}

# print availables methods
print(dir(capitals))

# print captials
print(capitals)

# get value by key
print(capitals["USA"])
print(capitals.get("China"))

# if key is not found in the dictionary (returns None)
print(capitals.get("Japan"))

# insert a new key:value pair to the dictionary
capitals.update({"Japan": "Tokyo"})

# update value by key
capitals.update({"USA": "Alabama"})

# remove key:value pair by key
capitals.pop("Sri Lanka")

# remove the pair at the end
capitals.popitem()

# remove all the key:value pairs
# capitals.clear()

# get all keys in the dictionary
keys = capitals.keys()
print(keys)

# get all values in the dictionary
values = capitals.values()
print(values)

# get a tubple with key value pairs as the tuple values
items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")


print(capitals)
