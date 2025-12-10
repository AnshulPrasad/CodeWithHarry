s = {1, 2.0, True, "Anshul", complex(5, 6)}
print(s)  # unordered values
# print(s[2]) # sets don't support indexing

s1 = {}
print(type(s1))

s2 = set()
print(type(s2))

for i in s:
    print(i)
