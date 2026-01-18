class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num += n

    @staticmethod
    def add(
        a, b
    ):  # we can write it outside the class, but we want to ship it with the class.
        return a + b


a = Math(10)
print(a.num)

a.addtonum(2)
print(a.num)

print(a.add(6, 5))
