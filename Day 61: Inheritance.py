class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"The employee name is {self.name} and id is {self.id}")


class Programmer(Employee):
    def show_language(self):
        print("Python")


# e1 = Employee("Anshul",1)
# e1.show_details()

# e1.show_language() # error

e2 = Programmer("Anshul", 2)  # inheritance
e2.show_details()
e2.show_language()

# Types of inheritance
# single inheritance
# multiple inheritance
# multilevel inheritance
# hierarchical inheritance
# hybrid inheritance
