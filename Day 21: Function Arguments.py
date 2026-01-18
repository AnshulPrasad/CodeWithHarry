def average(a, b=5):  # a is a required argument, b is a default argument
    print((a + b) / 2)


average(7, 11)
average(b=7, a=11)  # keyword arguments
average(7)
# average() # incorrect function call


def name(*name):  # arguments are accessed as a tuple
    print(type(name))
    print(name[0], name[1], name[2])


name("anshul", "prasad", "hello")


def name(**name):  # arguments are accessed as a dictionary
    print(type(name))
    print(name["f"], name["s"], name["arbitrary"])


name(f="anshul", s="prasad", arbitrary="hi")


def name(**name):  # by default function return None
    return f"{name['f']} {name['s']} {name['arbitrary']}"


a = name(f="anshul", s="prasad", arbitrary="batata")
print(a)
