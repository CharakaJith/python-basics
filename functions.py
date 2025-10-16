# function is a block of reusable code
# function can have none or many arguments
# return statement can be used to return a value at the end of the function and back to the caller
# def my_function(age):
#       return age + 10


def print_happy_birthday(name, age):
    print(f"Happy birthday to {name}!\nYou are {age}.....")


# call function one time
print_happy_birthday("John", 31)

# execute it more than once
for x in range(3):
    print_happy_birthday("Jane", 20 + x)


def display_invoice(user_name, amount, due_date):
    print(f"hello {user_name}!\nyour bill of ${amount:.2f} is due on {due_date}")


display_invoice("Bob", 42.50, "01/12/2025")
display_invoice("Joe", 100.95, "05/08/2025")


def add(num_1, num_2):
    return num_1 + num_2


def substract(num_1, num_2):
    return num_1 - num_2


x = add(10, 12)
y = add(0, -18)
z = substract(15, -3)

print(x)
print(y)
print(z)


def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    return f"{first_name} {last_name}"


full_name = create_name("john", "doe")
full_name_2 = create_name("patrick", "star")

print(f"your full name is: {full_name}")
print(f"your full name is: {full_name_2}")
