import shutil
import os

shutil.copy("Exercise 9 - Shoutouts to Everyone.py", "fun.py")  # for files
shutil.copytree("/home/anshul/Documents/CodeWithHarry", "/home/anshul/Documents/folder")  # for folders
os.remove("/home/anshul/Documents/folder/fun.py")
shutil.move("fun.py", "/home/anshul/Documents/folder")
shutil.rmtree("/home/anshul/Documents/folder")
