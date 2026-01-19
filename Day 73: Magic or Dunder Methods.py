from emp import Employee

e = Employee("Anshul")
print(e)  # run __str__() by default else __repr__()
print(str(e))  # run __str__()
print(repr(e))  # run __repr__()
e()  # run __call__()
