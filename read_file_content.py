
import os

try:
    with open('C:\\Users\\пользователь\\Python\example\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File is not exist")















































