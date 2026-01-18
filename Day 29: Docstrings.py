# docstring can be used in function, method, class or module


def func1():
    """This function print Hello world"""

    print("Hello world")


func1()
print(func1.__doc__)


def func2():
    a = 5
    """This function print Hello world"""

    print("Hello world")


func2()
print(func2.__doc__)

print(sum.__doc__)
