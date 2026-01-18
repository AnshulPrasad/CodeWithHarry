import os


def rename(folder_path, format):
    count = 1
    for i in os.listdir(folder_path):
        file_extension = i.split(".")[-1]
        if file_extension == format:
            file_path = os.path.join(folder_path, i)
            os.rename(file_path, f"{folder_path}/{count}.{file_extension}")
            count+=1


rename("/home/anshul/Documents/CodeWithHarry/temp", "txt")
