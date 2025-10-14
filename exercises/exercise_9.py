# temperature conversion program

unit = input("current unit (C, F or K): ")
temp = float(input("enter your temperature: "))
to_unit = input("unit to convert to (C, F or K): ")

is_error = False
# validate current unit
if unit.capitalize() == to_unit.capitalize():
    is_error = True
    print("\ninvalid operation!")

# validate source unit
elif unit.capitalize() not in ["C", "F", "K"]:
    is_error = True
    print("\ninvalid unit!")

# validate target unit
elif to_unit.capitalize() not in ["C", "F", "K"]:
    is_error = True
    print("\ninvalid conversion unit!")

# conversion logic
else:
    unit = unit.capitalize()
    to_unit = to_unit.capitalize()
    
    if unit == "C":
        if to_unit == "F":
            new_temp = (temp * 9/5) + 32
        elif to_unit == "K":
            new_temp = temp + 273.15
    elif unit == "F":
        if to_unit == "C":
            new_temp = (temp - 32) * 5/9
        elif to_unit == "K":
            new_temp = (temp - 32) * 5/9 + 273.15
    elif unit == "K":
        if to_unit == "C":
            new_temp = temp - 273.15
        elif to_unit == "F":
            new_temp = (temp - 273.15) * 9/5 + 32

    print(f"\n{temp}°{unit} = {round(new_temp, 2)}°{to_unit}")
