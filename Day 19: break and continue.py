for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    if i == 5:
        continue
    print(i)

# do while loop implementation
i = 0
while True:
    print(i)
    i += 1
    if i % 20 == 0:
        break
