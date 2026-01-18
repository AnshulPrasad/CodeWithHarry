# Just a convention not a hard rule offered by python

# Types of access specifier
# public access specifier -> all variables are access directly
# private access specifier -> use name mangling to access variables indirectly
# protected access specifier -> Just a convention and can be different from the one shown below


class Employee:
    def __init__(self):
        self.name = "Anshul"  # public
        self.__age = 22  # private


a = Employee()
print(a.name)
# print(a.__age) # cannot access directly
print(a._Employee__age)  # can be accessed indirectly using name mangling
print(a.__dir__())


class Student:
    def __init__(self):
        self.name = "Harry"

    def _funName(self):  # protected
        return "Anshul"


class Subject(Student):
    pass


obj1 = Student()
obj2 = Subject()

print(obj1.name)
print(obj1._funName())

print(obj2.name)
print(obj2._funName())

print(dir(obj1))
print(dir(obj2))
