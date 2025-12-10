list1 = [1, 2.0, "Anshul", True, None, complex(9, 10)]

print(list1[4]) # positive index
print(list1[-1]) # negative index == list1[len(list1)-1]
print(len(list1))

print(None in list1) # find element in list1

print("sh" in list1[2]) # search in string element of list1

print(list1[:])
print(list1[1:-1])
print(list1[::2])

# list comprehension
lst = [i*i for i in range(10) if i%2==0]
print(lst)