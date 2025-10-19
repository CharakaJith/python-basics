# if __name__ == __main__ : this means this script can be imported or run stand alone
# functions and classes in this mmodule can be reused without the main block of code executing


# define before the import to avoid circular import issue
def fav_food(food):
    print(f"your favourtie food: {food}")


from script_1 import *


def main():
    print("main is called...")
    fav_food("pizza")
    print("good bye!")


if __name__ == "__main__":
    main()
