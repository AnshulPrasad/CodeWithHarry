import time


def usingWhile():
    i = 0
    while i < 50000:
        i += 1
        print(i)


def usingFor():
    for i in range(50000):
        print(i)


init = time.time()
usingFor()
for_time = time.time() - init

init = time.time()
usingWhile()
while_time = time.time() - init

print(f"while_time: {while_time}s")
print(f"for_time: {for_time}s")

print(4)
time.sleep(3)
print("This is printed after 3 seconds")

print(time.localtime())
print(time.strftime("%Y-%m-%d hello %H:%M:%S"))
