f = open("myfile.txt", "r")

i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    print(f"marks of student {i} in physics: {line.split(',')[0]}")
    print(f"marks of student {i} in chemistry: {line.split(',')[1]}")
    print(f"marks of student {i} in mathematics: {line.split(',')[2]}")
    print(line)

f = open("myfile2.txt", "w")
lines = ["line1\n", "line2\n", "line3\n"]
f.writelines(lines)
f.close()
