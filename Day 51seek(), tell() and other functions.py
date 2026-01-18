with open("myfile.txt", "r") as f:
    print(type(f))

    f.seek(10)  # move 10 characters forward
    data = f.read(7)  # read 7 characters from current position
    print(data)
    print(f.tell())  # current position of pointer

with open("myfile2.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)  # reduce size of file to 5 characters

with open("myfile2.txt", "r") as f:
    print(f.read())
