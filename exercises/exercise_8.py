# weight conversion program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (k or l): ")

is_error = False

if unit.capitalize() == "K":
    new_weight = round(weight * 2.205, 2)
    new_unit = "lbs"
elif unit.capitalize() == "L":
    new_weight = round(weight / 2.205, 2)
    new_unit = "kg"
else: 
    is_error = True
    print("Invalid unit!")

if not is_error:
    print(f"\nYour weight {weight} {'kg' if unit.capitalize() == 'K' else 'lbs'} = {new_weight} {new_unit}")
