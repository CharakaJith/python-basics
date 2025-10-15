# basic shopping cart

item = input("item name: ")
price = float(input("unit price: "))
quantity = int(input("quantity: "))

total = price * quantity

print(f"\n{item} (${price}): x{quantity}")
print(f"your total is ${total}")
