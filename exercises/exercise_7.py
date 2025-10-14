# advanced calculator

num1 = float(input("input the first number: "))
num2 = float(input("input the second number: "))

opt = input("enter an operation (+ - * /): ")

if opt == "+":
    result = round(num1 + num2, 2)
elif opt == "-":
    result = round(num1 - num2, 2)
elif opt == "*":
    result = round(num1 * num2, 2)
elif opt == "/":
    result = round(num1 / num2, 2)
else:
    result = ""
    error = "please select a valid operation!"

if result != "":
    print(f"\n{num1} {opt} {num2} = {result}")    
else:
    print(f"\n{error}")
    
