# modes: read(r), write(w), append(a), readbinary(rb), text(t), binary(b)
f = open("myfile.txt", "r")
print(f)

text = f.read()
print(text)
f.close()

# if an non-existing file opened in write mode, then it will be created
# f=open('myfile.text','x') give error if file already exist and make file if not.
f = open("myfile2.txt", "w")
f.write("Hello")
f.close()

f = open("myfile2.txt", "a")
f.write("\nHi")
f.close()

with open("myfile.txt", "w") as f:
    f.write("Hello, I am inside with")
