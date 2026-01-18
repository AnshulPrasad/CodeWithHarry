class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod # this will make cls to take class and change the class variable bellow
    def changeCompany(cls, newCompany):  # cls takes object as argument by default.
        cls.company = newCompany


e1 = Employee()
e1.name = "Anshul"
e1.show()

e1.changeCompany("Tesla") # class variable company will be changed and not instance method
e1.show()

print(Employee.company)
