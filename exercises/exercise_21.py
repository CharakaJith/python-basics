# dice rolling game

import random

dice_faces = {
    1: ["╔═════╗", "║     ║", "║  ●  ║", "║     ║", "╚═════╝"],
    2: ["╔═════╗", "║ ●   ║", "║     ║", "║   ● ║", "╚═════╝"],
    3: ["╔═════╗", "║ ●   ║", "║  ●  ║", "║   ● ║", "╚═════╝"],
    4: ["╔═════╗", "║ ● ● ║", "║     ║", "║ ● ● ║", "╚═════╝"],
    5: ["╔═════╗", "║ ● ● ║", "║  ●  ║", "║ ● ● ║", "╚═════╝"],
    6: ["╔═════╗", "║ ● ● ║", "║ ● ● ║", "║ ● ● ║", "╚═════╝"],
}

dice = []
total = 0

# take user input
while True:
    num_of_dice = int(input("how many dices: "))
    if num_of_dice <= 0:
        print("please select a valid number of dices!")
    else:
        break

# random dice face for each dice
for x in range(num_of_dice):
    random_num = random.randint(1, 6)
    dice.append(random_num)

# calculate total
for die in dice:
    total += die

# print dice face
# for die in range(num_of_dice):
#     for line in dice_faces.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_faces.get(die)[line], end="\t")
    print("")

print(f"total: {total}")
