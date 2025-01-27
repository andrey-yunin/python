# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments4

def add(num1, num2):
    sum = num1 + num2
    return sum

print (add(1, 2))


def add(*args):
    for i in args:
        print(i)  
    

(add("Andrey",49, "Yunin"))




































