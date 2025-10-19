# basic slot machine

import random, time


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🏆", "⚡"]
    results = [random.choice(symbols) for _ in range(3)]

    return results


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 8
        elif row[0] == "🏆":
            return bet * 10
        elif row[0] == "⚡":
            return bet * 25

    return 0


def main():
    balance = 100

    print("\n------ Slot Machine ------")
    print("symbols: (🍒 🍉 🍋 🏆 ⚡)")
    print("--------------------------")

    while balance > 0:
        print(f"current balance: ${balance:.2f}")

        bet = input("\nplace your bet: ")
        if not bet.isdigit():
            print("please enter a valid amount!")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient balance!")
            continue

        if bet < 0:
            print("please enter a valid amount!")
            continue

        balance -= bet

        row = spin_row()
        print("spining", end="")
        for x in range(6):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("")

        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"\ncongratulations! you won ${payout:.2f}")
        else:
            print(f"\nplease try again!")

        balance += payout

        play_again = input("\nplay again y/n: ").upper()
        if play_again == "N":
            break

    print("\n------------------------------------")
    print(f"game over! current balance: ${balance:.2f}")
    print("------------------------------------")


if __name__ == "__main__":
    main()
