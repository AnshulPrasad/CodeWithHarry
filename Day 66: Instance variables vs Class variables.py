# instance variable is alloted seperately to each and every object
# class variable
class Employee:
    company_name = "Apple"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
        self.raise_amount = 0.02  # instance variable

    def show_details(self):
        print(f"The name of {self.company_name} employee is {self.name}")


emp1 = Employee("Anshul")
emp1.show_details()


emp1.company_name = (
    "Google"  # class variable becomes instance variable of instance emp1
)
emp1.show_details()
# Employee.show_details(emp1)

Employee.company_name = "Microsoft"
print(Employee.company_name)


emp2 = Employee("Prasad")
emp2.show_details()
