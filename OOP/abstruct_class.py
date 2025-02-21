# Prevents a user from creating an object of this class 
# + compels a user to override abstract methods in a child class 

# Abstact class = a class witch contains one or more abstact methods.
# Abstract method that has a declatation but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motocycle") 

    def stop(self):
        pass


#vehicle = Vehicle()
car = Car()
motocycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motocycle.go()






