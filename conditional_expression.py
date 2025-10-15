# is a one-line shortcut for the if ele statement (also known as the ternary operator)
# used to print or assign one or two values based on a condition
# X if condition else Y

num = 5
age = 31
user_role = "admin"

# assigning value
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

status = "adult" if age >= 18 else "child"
print(status)

# print value with nested ternary
print("positive" if num > 0 else ("zero" if num == 0 else "negative"))

print(
    "full access"
    if user_role == "admin"
    else ("limited access" if user_role == "user" else "invalid role")
)
