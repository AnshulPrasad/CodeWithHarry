# parent1           parent2
#     \              /
#       \           /
#           child1


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance


o = DancerEmployee("Anshul", "Kathak")
print(o.name)
print(o.dance)
o.show()  # Dancer's show function will be called
print(DancerEmployee.mro())  # method resolution order
