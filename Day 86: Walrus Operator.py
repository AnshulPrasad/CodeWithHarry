# assigns values to variables as part of a larger expression
a = True
print(a)
print(a := False)
print(a)

numbers = [1, 2, 3, 4, 5]
while n := len(numbers) > 0:
    print(numbers.pop())

foods = []
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)
