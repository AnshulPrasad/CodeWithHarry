import os


def rename(folder_path, extension):
    i = 1
    for file in os.listdir(folder_path):
        if file.endswith(extension):
            file_path = os.path.join(folder_path, file)
            os.rename(file_path, f"{folder_path}/{i}{extension}")
            i += 1


rename("/home/anshul/Documents/CodeWithHarry/txt", ".txt")
