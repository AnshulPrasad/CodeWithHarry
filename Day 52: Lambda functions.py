# def double(x):
#     return x*2

double = lambda x: x * 2
print(double(3))

add = lambda *x: sum(x)
print(add(3, 5, 10))


def appl(fx, value):
    return 6 + fx(value)


print(appl(double, 11))  # pass function double as an argument
# function "lambda *x: sum(x)" has no name. It is called anonymous function
