# banking application


def show_balance(balance):
    print(f"\nyour current balance is ${balance:.2f}")


def deposit(balance):
    amount = read_amount()
    balance += amount
    print(f"${amount:.2f} has been credited...")

    return balance


def withdraw(balance):
    amount = read_amount()
    if amount > balance:
        print("Insufficient account balance!")
    else:
        balance -= amount
        print(f"${amount:.2f} has been debited...")

    return balance


def quit_app():
    print("\nThank you for using our app....")
    return False


def read_amount():
    while True:
        amount = float(input("\nenter your amount: "))
        if amount <= 0:
            print("please enter a valid amount!")
        else:
            break

    return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n------ Banking App ------")
        print("1. show balance")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. quit")
        choice = int(input("your choice: "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance = deposit(balance)
            case 3:
                balance = withdraw(balance)
            case 4:
                is_running = quit_app()
            case _:
                print("invalid operation!")


if __name__ == "__main__":
    main()
