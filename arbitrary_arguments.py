# arbitrary arguments means the number of arguments being passed to the function when invoking is unknown
# args: allws to pass multiple non-keyword argumnts
# kwrgs: allows to pass multiple keywords argumnts


# args
## accepts a tuple
def add(*nums):
    total = 0
    for num in nums:
        total += num

    return total


print(add(5, 5))
print(add(5, 5, 12, 19, 1, 0, -2))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()


display_name("John", "Doe")
display_name("Patrick", "The", "Star")
display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


# kwrgs
## accepts a dictionary
def print_address(**kwrgs):
    for key, value in kwrgs.items():
        print(f"{key}: {value}")


print_address(
    line_one="10/2E, Newport Street",
    line_two="",
    province="Western",
    city="Colombo",
    postal_code="10220",
    country="Sri Lanka",
)


def shipping_label(*args, **kwrgs):
    print("------- SHIPPING LABEL -------")
    for arg in args:
        print(arg, end=" ")
    print("")

    print(f"{kwrgs.get('apt_no')}-{kwrgs.get('street')}")
    print(f"{kwrgs.get('city')}, {kwrgs.get('state')}, ({kwrgs.get('zip')})")
    print("------------------------------")


shipping_label(
    "Dr.",
    "Spongebob",
    "Squarepants",
    "III",
    street="123 Fake St.",
    apt_no="120/1E",
    city="Detroit",
    state="MI",
    zip="543-21",
)
