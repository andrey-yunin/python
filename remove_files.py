import os
import shutil

source = "C:\\Users\\пользователь\\Python\example\\test.txt"

try:
    os.remove(source)    

except FileNotFoundError:
    print("File is not found")

source_folder = "C:\\Users\\пользователь\\Python\example\\folder"

try:
    # os.remove(source_folder) # remove file
    # os.rmdir(source_folder) # remove empty folder
    shutil.rmtree(source_folder)  # remove not empty folder

except PermissionError:
    print("You don't have permission to remove folder")
except OSError:
    print("Folder is not empty")
else:
    print (source_folder + " was removed")





 









































