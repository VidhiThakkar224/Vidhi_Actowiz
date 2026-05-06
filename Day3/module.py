# The os module in Python is a built-in library that lets your program interact with the operating system
# (like Windows, Linux, or macOS).
# The os module helps you work with files, folders, and system-related tasks such as creating directories,
# checking paths, or running system commands.
#
# Why we use os module
# It allows you to:
#
# Create, delete, and rename files/folders
# Navigate through directories
# Get information about the system
# Work with file paths

import os

# Create a new file
file = open("old.txt", "w")
file.close()

#rename file
os.rename("old.txt", "new.txt")

#remove file
os.remove("new.txt")

# get current working directory
print(os.getcwd())

#change directory
os.chdir("C:/Users")
print(os.getcwd())

#list file and folder
print(os.listdir())



