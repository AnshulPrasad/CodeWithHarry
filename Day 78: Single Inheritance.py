# one class inherited from parent class


class Animal:
    def __init__(self):
        self.name = "Animal"

    def info(self):
        print(self.name)

    def make_sound(self):
        print("Hi")


class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def info(self):
        print(self.name)
        print(self.breed)

    def make_sound(self):
        print("Bark")
