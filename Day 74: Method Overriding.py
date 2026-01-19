class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(Shape):
    def __init__(self, r):
        super().__init__(r, r)
        self.r = r

    def area(self):
        return 3.14 * super().area()


s = Shape(3, 5)
print(s.area())

c = circle(3)
print(c.area())
