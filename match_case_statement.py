# match case statement is also known as the switch
# altrenative to using many elif statements
# executes a code block if  a value matches a 'case'


def day_of_week(date):
    day = ""
    match (date):
        case 1:
            day = "Monday"
        case 2:
            day = "Tuesday"
        case 3:
            day = "Wednesday"
        case 4:
            day = "Thursday"
        case 5:
            day = "Friday"
        case 6:
            day = "Saturday"
        case 7:
            day = "Sunday"
        case _:
            return "Not a valid date!"

    return f"it's a {day}"


print(day_of_week(2))
print(day_of_week(5))
print(day_of_week(12))


def is_weekend(day):
    is_weekend = False
    match (day):
        case "Saturday" | "Sunday":
            is_weekend = True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            is_weekend = False
        case _:
            return "Not a valid date!"

    return f"{day} is {'a weekend!' if is_weekend else 'not a weekend!'}"


print(is_weekend("Saturday"))
print(is_weekend("Wednesday"))
