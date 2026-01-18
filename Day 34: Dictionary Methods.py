ep1 = {101: 45, 102: 89, 103: 69, 104: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)

# ep1.clear()
# print(ep1)

empt = {}
print(empt)

ep1.pop(101)
print(ep1)

ep1.popitem()
print(ep1)

# del ep2
# print(ep2)

del ep2[222]
print(ep2)
