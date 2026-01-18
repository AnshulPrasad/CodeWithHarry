for i in range(5):
    print(i)
    if i == 3:
        break
else:  # Executed only when loop ended successfuly
    print("Sorry no i")

# similar for while loop
j = 0
while j < 5:
    print(j)
    if j == 3:
        break
    j += 1
else:
    print("Sorry no i")
