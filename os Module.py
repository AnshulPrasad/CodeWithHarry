import os

# os.mkdir("data") # raise error if directory already exist

if not os.path.exists("data"):
    os.mkdir("data")

# for i in range(100):
#     # os.mkdir(f"data/Day{i+1}")
#     os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")

folders = os.listdir("data")
# print("\n".join(folders))

for folder in folders:
    print(folder, end=": ")
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())  # current working directory
os.chdir("/")
print(os.getcwd())  # current working directory

# below code give error because the directory has been changed to /
# for folder in folders:
#     print(folder, end=": ")
#     print(os.listdir(f"data/{folder}"))
