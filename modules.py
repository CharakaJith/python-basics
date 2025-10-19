# module is a python (.py) file containing a code
# have to use import <module> to use it in another file
# used to break up large programs to reusable separate files

# import math module
# import math

# use alias
import math as m

# import a variable or function from the module
# try to avoid this when possible
from math import e


# access module variables
print(m.pi)

print(e)

# user defined module
import modules_example as exmp

result = exmp.pi
result = exmp.area_circle(7)
result = exmp.circumference(5)
result = exmp.cube(3)

print(result)
