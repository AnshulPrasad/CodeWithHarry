tup = 1
print(type(tup))

tup = (1,)
print(type(tup))

tup = (1, 5.0, "Anshul", True, None, complex(2, 3))
print(type(tup), tup)
# tup[0]=90 # tuples and strings are immutable

print(tup[0])
print(tup[-1])
print(len(tup))
print(tup[1:-1])
print(5.0 in tup)
