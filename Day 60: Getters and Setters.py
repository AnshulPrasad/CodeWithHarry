class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property  # Decorator getter is used to get value by print(obj.value).
    # It is shown as if 'value' is a property but in reality it is a method.
    # It is a way to encapsulate properties.
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter  # setter is used to set value 27 by using obj.value = 27
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
obj.show()

obj.ten_value = 27
obj.show()

print(obj.ten_value)
obj.show()
