
import os

path = "C:\\Users\\пользователь\\Python\\example\\fold"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("location is a file")
    elif os.path.isdir:
        print("location is a folder")
else:
    print("That location doesn't exist!")












































