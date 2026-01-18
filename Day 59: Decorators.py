def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function.")

    return mfx


@greet  # decorator is a function that takes another function as an argument and returns a new fuction that modifies the behaviour of the original function.
def hello():
    print("Hello World!")


hello()  # decorated function

# (or)
# greet(hello)()


def add(a, b):
    return a + b


greet(add)(1, 2)
