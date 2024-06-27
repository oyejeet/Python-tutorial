# Abstraction : Hidding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def car_started(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.car_started()

# Encapsulation : Wrapping data and functions into a single unit(object).
#This is what we have done so far

