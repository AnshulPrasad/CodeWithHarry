# factorial(3) = 3*2*1


def factorial(n):
    if n == 1 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(int(input("Enter factorial number: "))))


# lis = [1,1]
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print([fibonacci(i) for i in range(1, 1 + int(input("Enter length of series: ")))])
