# weight conversion program

weight = float(input("enter your weight: "))
unit = input("kilograms or pounds (k or l): ")

is_error = False
if unit.capitalize() == "K":
    new_weight = round(weight * 2.205, 2)
    new_unit = "lbs"
elif unit.capitalize() == "L":
    new_weight = round(weight / 2.205, 2)
    new_unit = "kg"
else:
    is_error = True
    print("invalid unit!")

if not is_error:
    print(
        f"\nyour weight {weight} {'kg' if unit.capitalize() == 'K' else 'lbs'} = {new_weight} {new_unit}"
    )
