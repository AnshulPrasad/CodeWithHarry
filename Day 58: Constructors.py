class Person:
    def __init__(
        self, name, occ
    ):  # Constructor. Always return None. Parameterized constructor take some arguments. Default constructor only take self as an argument.
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Anshul", "AI engineer")
# print(a.name,a.occ)
# a.info()

# a.name = "Prasad"
# a.occ = "Runner"
# print(a.name,a.occ)
# a.info()

b = Person("Harry", "Developer")

a.info()
b.info()

# c = Person(1,2,3) # 4 arguamets are passed: self,1,2,3
