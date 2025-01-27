# index operator [] = gives access toa sequence's elements (str, list, tuples....)

name = "andrey Yunin!"

if name[0].islower():
    name = name.capitalize()
    print(name)

#first_name = name[0:6]
first_name = name[:6]
last_name = name[7: -1]
last_character = name[-1]

print(first_name.upper())
print(last_name.lower())
print(last_character)




























