a = int(input("Enter any value between 1 and 9: "))

if a < 1 or a > 9:
    raise ValueError("Value should be between 1 and 9.")


a = input("Enter input: ")

if a != "quit":
    raise ValueError("input is not 'quit'")
