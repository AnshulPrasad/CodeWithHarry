class Person:
    name = "Anshul"
    occupation = "AI engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.info()

b = Person()
b.name = "Mohan"
b.occupation = "Singer"
b.info()
