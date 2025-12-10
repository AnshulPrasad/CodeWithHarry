tup = (1, 2, 3, 4, 5)

temp = list(tup)  # typecasting
temp.append(6)  # add
temp[3] = 3  # change
temp.pop(1)  # remove
temp = temp + [999, -134]  # concatenate
tup = tuple(temp)  # typecasting
print(tup)

print(tup.count(3))  # count(element)
print(
    tup.index(3, 1, 5)
)  # first occurence. index(element,start,end). raise error if element not found
print(len(tup))
