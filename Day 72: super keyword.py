class ParentClass:
    def parent_method(self):
        print("This is the parent method.")


class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")

    def parent_method(self):
        print("Anshul")
        super().parent_method()


child_object = ChildClass()
child_object.parent_method()
