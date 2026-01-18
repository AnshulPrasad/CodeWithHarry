dic = {"name": "anshul", "age": 22, "language": "english"}

print(dic["name"])
print(dic.get("name"))

# print(dic['name2']) # throw error if key not found
print(dic.get("name2"))

print(dic.keys())
print(dic.values())
print(dic.items())
