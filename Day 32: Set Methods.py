s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1 | s2)  # .union()
print(s1 & s2)  # s1.intersection(s2) s1.intersection_update(s2)
print(s1 ^ s2)  # s1.symmetric_difference(s2) s1.symmetric_difference_update(s2)
print(s1 - s2)  # s1.difference(s2) s1.difference_update(s2)
print(s2 - s1)  # s2.difference(s1) s2.difference_update(s1)

s1.update(s2)
print(s1, s2)


cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities1.isdisjoint(cities2))  # nothing in common then True
print(cities1.issuperset(cities2))
print(cities1.issubset(cities2))

cities1.add("Mandsaur")
print(cities1)

cities1.update(cities2)  # used usual when we need to add more than one elements as sets
print(cities1, cities2)

# cities1.remove("Indore") # throw an error if value not found
cities1.discard("Indore")
print(cities1)

item = cities1.pop()
print(item, cities1)

del cities2
# print(cities2) # now set cities2 don't exist

cities1.clear()
print(cities1)

print("Delhi" in cities1)
