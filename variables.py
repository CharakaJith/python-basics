# variable is a container for values (string, integer, float, boolean)
# a variable behaved as it was the value it contains

# data type: strings
first_name = "John"
last_name = "Doe"
email = "john@gmail.com"

# data type: integer
age = 31
mobile = 701234326

# data type: float
salary = 10.99
gpa = 3.2

# data type: boolean
# is_student = False
is_student = True

# print using formatted string literals
print(f"{first_name} {last_name} : {age}")
print(f"gpa: {gpa}")
print(f"email: {email}")
print(f"mobile: +94 {mobile}")
print(f"salary: ${salary} per hour")
print(f"currently {'a student' if is_student else 'not a student'}")
