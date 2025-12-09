a = int(input("Enter your age: "))
print("Your age is", a)

# conditional operators
# >, <, >=, <=, ==, !=
print(a > 18)
print(a >= 18)
print(a < 18)
print(a <= 18)
print(a == 18)
print(a != 18)

# if else ladder
if a > 18:
    print("Your can drive")
elif a == 18:
    print("You can drive under guidance")
else:
    print("You cannot drive")

# nested if else statements
if a > 18:
    print("Your can drive")
else:
    if a == 18:
        print("You can drive under guidance")
    else:
        print("You cannot drive")
