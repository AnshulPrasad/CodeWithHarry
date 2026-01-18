# is = compare exact locations
# == = compare values

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)

a = 3 # both a and b are pointing to the same memory location
b = 3

print(a is b)
print(a == b)

a = (1, 2, 3)
b = (1, 2, 3)

print(a is b)
print(a == b)


a = None
b = None

print(a is b)
print(a == b)
