import random

# 0 means draw, 1 means user won, -1 means user lost
matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
choices = {"snake": 0, "water": 1, "gun": 2}
point_u, point_c = 0, 0

print("press quit to exit.")
while True:
    user = input("\nEnter your move: ")
    if user == "quit":
        break

    computer = random.choice(list(choices.keys()))
    print(f"computer move: {computer}")

    a = matrix[choices[computer]][choices[user]]

    if a == 1:
        point_u += 1
        print("You won")
    elif a == 0:
        print("Draw")
    else:
        point_c += 1
        print("You lost")


print(f"User's points: {point_u}")
print(f"Computer's points: {point_c}")
