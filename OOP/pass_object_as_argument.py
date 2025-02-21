# we can pass object as argument to a function much like what we have been doing 
# with variabls however the type of objects that we pass in may be limited
# based on the required attributes and methods thst given a cladss or object 
#might have!

class Car:
    color = None

class Motocicle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color 

car_1 = Car()
car_2 = Car()
car_3 = Car()

motocicle_1 = Motocicle()
change_color(motocicle_1, "black")


change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue") 

print(car_1.color)

print(car_2.color)
print(car_3.color)

print(motocicle_1.color)


