from if_name_equals_main import *


def fav_drink(drink):
    print(f"your favourtie drink: {drink}")


def main():
    print("this is script 1...")
    fav_food("pasta")
    fav_drink("ice milo")
    print("goodbye!")


if __name__ == "__main__":
    main()
