# keyword argument is an argument preceded by an identifier
# helps the readability and the order of arguments does not matter unline default arguments


def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title}. {first_name} {last_name}")


# correctly prints the output
hello("Hello", "Mr", "John", "Doe")

# order is not in order hence the output is not correct
hello("John", "Hello", "Doe", "Mr")

# used keywords, hence order does not matter
hello(first_name="John", greeting="Hello", last_name="Doe", title="Mr")

# end is a keyword argument for print()
for x in range(1, 11):
    print(x, end=" ")

print("")

# sep is another keyword argument
print("1", "2", "3", "4", "5", sep="-")
