# type casting is the process of converting data type from one to another
# int -> float, int -> string, bool -> string etc

name = "John Doe"
age = 31
gpa = 3.2
is_student = True

# find the data type of a variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print(f"\ntype casting in progress.....\n")

# cast: float -> int
new_gpa = int(gpa)

# cast: int -> float
new_age = float(age)

# cast: bool -> string
new_is_student = str(is_student)

# cast: string -> bool
new_name = bool(name) # this would always be true as long as the variable 'name' has a value

print(f"age: {age} ({type(age)}) -> age: {new_age} ({type(new_age)})")
print(f"gpa: {gpa} ({type(gpa)}) -> gpa: {new_gpa} ({type(new_gpa)})")
print(f"is_student: {is_student} ({type(is_student)}) -> is_student: {new_is_student} ({type(new_is_student)})")
print(f"name: {name} ({type(name)}) -> name: {new_name} ({type(new_name)})")
