# parent2
#    |
# parent1
#    |
# child


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(self.name)
        print(self.species)


class Dog(Animal):
    def __init__(self, name, species, breed):
        Animal.__init__(self, name, species)
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(self.breed)


class GermanShefered(Dog):
    def __init__(self, name, species, breed, color):
        Dog.__init__(self, name, species, breed)
        self.color = color

    def show(self):
        Dog.show(self)
        print(self.color)


o = GermanShefered("Tommy", "Dangerous", "German", "Black")
o.show()
print(GermanShefered.mro())
