# a loop within a loop can be known as a nested loop
# outer loop:
#       inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")  # print x on same line with space between
    print()
