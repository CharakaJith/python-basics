# grades check

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
failing_grade = [grade for grade in grades if grade < 60]

print(f"passing grades: {passing_grades}")
print(f"failing grades: {failing_grade}")
