# print a rectangle

cols = int(input("number of columns: "))
rows = int(input("number of rows: "))
symbol = input("your symbol: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()