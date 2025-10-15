# validate user inputs (username)
# 1. no more than 12 characters
# 2. must not contain space
# 3. must not contain digits

user_name = input("select a username: ")

if len(user_name) > 12:
    message = "user name must not have more than 12 characters!"
elif user_name.find(" ") != -1:
    message = "user name cannot contain any space!"
elif not user_name.isalpha():
    message = "user name cannot have any numbers!"
else:
    message = f"your username: {user_name}"

print(f"\n{message}")
