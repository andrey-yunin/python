
import os

#text = "Haaaaaaaa!\nThis is some text\nHave a good one\n"
text = "Have a nace day!\n"

try:
    #with open('C:\\Users\\пользователь\\Python\example\\test.txt','w') as file: # all text will be rewrite
    with open('C:\\Users\\пользователь\\Python\example\\test.txt','a') as file: # text will be add


        file.write(text)

        #print(file.read())
except FileNotFoundError:
    print("File is not exist")

try:
    with open('C:\\Users\\пользователь\\Python\example\\test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("File is not exist")

















































