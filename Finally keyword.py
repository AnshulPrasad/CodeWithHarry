# try:
#     l = [1,2,3,4,5]
#     i = int(input("Enter the number: "))
#     print(l[i])
# except:
#     print("Some error occured.")
# finally:
#     print("I am always executed")
# print("I am always executed") # We can use it to get the same functionality. but not inside a function.


def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter the number: "))
        print(l[i])
        return 0
    except:
        print("Some error occured.")
        return 1
    finally:
        print(
            "I am always executed"
        )  # always executed no matter function is returned or not inside try or except block
    print("I am always executed")  # will never be executed


x = func1()
print(x)
