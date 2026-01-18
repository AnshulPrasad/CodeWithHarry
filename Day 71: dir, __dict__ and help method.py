x = [1, 2, 3]
print(
    dir(x)
)  # dir returns a list of all the attributes and methods available for an object
print(x.__add__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John", 30)
print(p.__dict__)  # returns a dictionary representation of an object's attributes

print(help(Person))  # get help docs for an object
