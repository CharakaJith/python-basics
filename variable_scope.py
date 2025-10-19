# variable scope means where a variable is visible and accessible
# scope resolution/order (LEGB) = Local -> Enclosed -> Global -> Built-in

# improt built in variable from another module
from math import pi

# global version outside of any function.
# can be used in any function iside the module
number = 100


def func_1():
    # variable a is local to func_1 only
    a = 10
    print(a)

    # print(b) # this would be an error since there is no variable b inside the func_1


def func_2():
    a = "hello"  # different variable a
    b = "world"  # variable b is local to func_w only
    print(f"{a} {b}")
    print(number)


def func_3():
    x = 10
    y = 20

    def func_4():
        x = 2
        print(x)  # takes the value of local variable x inside the func_4
        print(y)  # takes the value of the enclosed variable y from func_3
        print(number)  # takes the value of the global variable number from module

    func_4()
    print(x)
    print(y)
    print(pi)


func_1()
func_2()
func_3()
print(pi)
