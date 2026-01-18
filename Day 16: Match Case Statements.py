x = int(input("Enter the value of x: "))

match x:  # x is  a variable which is matched with pattern
    case 0:  # 0 is a pattern
        print("x is zero")
    case 4:  # 4 is a pattern
        print("x is 4")
    case _ if x != 90:
        print("x is not 90")
    case _:  # default case
        print(x)
