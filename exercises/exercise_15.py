# advanced shopping cart

cart = []

while True:
    print(
        "\n1. add to cart"
        "\n2. remove from cart"
        "\n3. see all items"
        "\n4. clear cart"
        "\n5. checkout"
        "\n6. quit"
    )
    operation = int(input("select your operation: "))

    if operation == 1:
        while True:
            item = input("\nenter your item: ")
            if not item.isalpha():
                print("\nplease enter a valid item name!")
            else:
                break

        while True:
            price = float(input("enter the price: "))
            if price <= 0:
                print("\nplease enter a valid price!")
            else:
                break

        while True:
            qty = int(input("enter number of units: "))
            if qty <= 0:
                print("\nplease enter a valid quantity!")
            else:
                break

        cart.append({"item": item, "price": price, "qty": qty})

    elif operation == 2:
        if len(cart) != 0:
            print(f"\n{'No.':<5}{'Item':^15}{'Price':^15}{'Quantity':^15}")
            for i, item in enumerate(cart, start=1):
                print(f"{i:<5}{item['item']:^15}{item['price']:^15}{item['qty']:^15}")

            while True:
                index = int(input("\nItem number to remove: "))

                if index <= 0 or index > len(cart):
                    print("\nPlease enter a valid item number!")
                else:
                    cart.pop(index - 1)
                    break
        else:
            print("\nyour cart is empty!")
    elif operation == 3:
        if len(cart) != 0:
            print(f"\n{'No.':<5}{'Item':^15}{'Price':^15}{'Quantity':^15}")
            for i, item in enumerate(cart, start=1):
                print(f"{i:<5}{item['item']:^15}{item['price']:^15}{item['qty']:^15}")
        else:
            print("\nyour cart is empty!")
    elif operation == 4:
        cart.clear()

        print("\nyour cart has been cleared!")
    elif operation == 5:
        if len(cart) != 0:
            total = 0
            for item in cart:
                total += item["price"] * item["qty"]

            print(f"\nyour total is ${total:.2f}")
            print("thank you for shopping with us!")

            cart.clear()
        else:
            print("\nyour cart is empty!")

    elif operation == 6:
        if len(cart) == 0:
            print("\nthank you for shopping with us!")
            break
        else:
            print("\nplease checkout first!")
    else:
        print("\nplease select a valid operation!")
