# program should not hault

a = input("Enter the number: ")

print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{a} X {i} = {int(a)*i}")
except IndexError:
    print("Index Error")
except ValueError:
    print("Value error")
except Exception as e:
    # print(e)
    print("Invalid input.")
