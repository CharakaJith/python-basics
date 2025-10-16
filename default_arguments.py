# default argument sets a default value to a function parameter
# used when function call omits the said parameter when calling the function
# non default arguments must be before the default arguments


def net_price(list_price, discount=0.00, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


# function call without any extra parameters
ps5_price = net_price(500)

# functoin call with price and discount
ps4_price = net_price(400, 0.1)

# functoin call with price, discount and tax
ps3_price = net_price(400, 0.1, 0)

print(f"pst5 price: ${ps5_price:.2f}")
print(f"pst4 price: ${ps4_price:.2f}")
print(f"pst3 price: ${ps3_price:.2f}")
