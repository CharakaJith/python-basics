# concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 3.00,
    "lemonade": 4.25,
}

cart = []
total = 0

print("         MENU          ")
print("-----------------------")

print(f"{'item':10}{'price':10}")
for key, value in menu.items():
    print(f"{key:10}: $ {value:.2f}")

while True:
    food = input("\nselect an item or q to quit: ")
    if food.upper() == "Q":
        break
    elif menu.get(food) is None:
        print("please select a valid item!")
    else:
        cart.append(food)
        print("item added successfully!")

print("\nyour items: ", end=" ")
for food in cart:
    total += menu.get(food)
    print(f"{food}", end=", ")

print(f"\nyour total is: $ {total:.2f}")
