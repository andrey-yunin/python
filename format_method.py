# str.format() = optional method that gives users
#                more control when displaying output

number = 1000
print(type(number))

animal = "cow"
item = "moon"

#print ("the " + animal + " jumped over the " + item)
print("the {} jump over the {}".format("cow", "moon"))
print("the {} jump over the {}".format(animal, item))
print("the {1} jump over the {0}".format(animal, item)) # positional argument
#print("the {animal} jump over the {item}".format(animal = "cow", item = moon)) # keyword argument

text = "The {} jump over {}"

print(text.format(animal, item))

name = "Andrey"
print("My mame is {}".format(name))

print("My mame is {:10}.Nice to meet you".format(name))
print("My mame is {:<10}.Nice to meet you".format(name))
print("My mame is {:>10}.Nice to meet you".format(name))
print("My mame is {:^10}.Nice to meet you".format(name))

number = 3.14159
print("pi is {:.2f}".format(number))
number = 1000
print("number is {:b}".format(number))
print("number is {:o}".format(number))
print("number is {:X}".format(number))
print("number is {:E}".format(number))

































