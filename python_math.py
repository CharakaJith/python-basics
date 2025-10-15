# math library provides a wide range of mathematical functions and constants
# useful for more advanced calculations beyond basic arithmetic
# have to import the library in order to use

import math

x = 3.14
y = 4
z = 5

# built in math related functions
## round a given number
result = round(x)

## find the absolute value of a number
result = abs(y)

## find power
result = pow(y, z)

## find maximum number
result = max(x, y, z)

## find minimum number
result = min(x, y, z)

print(result)

# python math library
## find the square root of a number
new_result = math.sqrt(y)

# round a float to upper limit
new_result = math.ceil(x)

# round a float to lower limit
a = 9.9
new_result = math.floor(a)

print(f"\nvalue of pi: {math.pi}")
print(f"value of e: {math.e}")

print(new_result)
