# Inheritance : When one class(child/derived) derives the properties & methods of another class(parent/base).

#Eg1] Single Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): #Inheritance: ToyotaCar inherits from Car, so it gains access to all the methods defined in Car.

    def __init__(self , name): #Constructor (__init__ method): This method initializes an instance of ToyotaCar with a name attribute.

        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("pirus")

car1.start()
car2.stop()


#Eg.2] Multilevel inheritance

class Car():
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel") 
car1.start()



#Eg.3] Multiple Inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


