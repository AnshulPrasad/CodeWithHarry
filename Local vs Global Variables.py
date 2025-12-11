x = 10


def hello():
    x = 5
    print(f"Local x: {x}")


print(f"Global x: {x}")
hello()
print(f"Global x: {x}")


x = 10


def hello():
    global x
    x = 5
    print(f"Local x: {x}")


print(f"Global x: {x}")
hello()
print(f"Global x: {x}")


# prefer not to change global variables from within a fucntion because it will become difficult debug the code later.
