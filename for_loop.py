# for loop executes a code block for a fixed number of times
# can be used to iterate over a range, string or sequence
# (start, end, step)

# basic for loop
for x in range(1, 10):
    print(x)

# count back word
for x in reversed(range(1, 11)):
    print(x)

# count with interval 3
for x in range(1, 20, 3):
    print(x)

# iterate over a string
credit_card = "1234-5678-9101-1121"

for x in credit_card:
    print(x)

# continue keyword used to skip over an iterate
for x in range(1, 20):
    if x == 13:
        continue
    else:
        print(x)

# break keyword used to break the loop
for x in range(1, 20):
    if x == 10:
        break
    else:
        print(x)
