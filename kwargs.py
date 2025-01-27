# **kwargs = parameter that will pack all arguments into dictionarity 
#            usefull so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("hello ", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ") 

hello(title = "Mr", first = "Andrey", last = "Yunin")




































