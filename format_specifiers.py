# allows to format a value on inserted flags
# {value:flag}

price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34
price_4 = 365000.00
price_5 = 1234500.99

# show only 2 decimal places
print(f"price 1: ${price_1:.2f}")

# add 1- spaces before the string
print(f"price 2: ${price_2:10}")

# add a padding with a character
print(f"price 3: ${price_3:010}")

# justify to left with 10 spaces
print(f"price 1: ${price_1:<10}")
print(f"price 2: ${price_2:<10}")

# justify to right with 20 spaces
print(f"price 1: ${price_1:>20}")
print(f"price 2: ${price_2:>20}")

# center align
print(f"price 1: ${price_1:^10}")
print(f"price 2: ${price_2:^10}")
print(f"price 3: ${price_3:^10}")

# display + sign for positive numbers
print(f"price 1: ${price_1:+}")
print(f"price 2: ${price_2:+}")
print(f"price 3: ${price_3:+}")

# add a space for padding
print(f"price 1: ${price_1: }")
print(f"price 2: ${price_2: }")
print(f"price 3: ${price_3: }")

# separte with a , for thousand 
print(f"price 4: ${price_4: ,.2f}")
print(f"price 5: ${price_5: ,.2f}")
