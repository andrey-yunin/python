import os

source = "C:\\Users\\пользователь\\Python\example\\test.txt"
destination = "C:\\Users\\пользователь\\Python\example\\fold\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
      
except FileNotFoundError:
    print("File is not found")





 









































