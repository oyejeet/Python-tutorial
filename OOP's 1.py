# Eg.1]
class student:       # student is a class
    name = "Karan"
    
s1  = student()      # s1 & s2 are objects of class student
print(s1.name)       # name is a parameter of class with value "Karan"

s2 = student()
print(s2)

#Eg.2]

class car:
    colour = "Blue"
    brand = "Mercedes"

car1 = car()
print(car1.colour)
print(car1.brand) 

# by using __init__ function
# this is more accurate way of writing the code.
class Student():

    def __init__(self,fullname):  # self paramater is a reference to the current instance of the class, and is used to access variables that belongs to the class.

        self.name = fullname
        print("adding new student in Database..")


s1 = Student("karan")
print(s1.name)

s2 = Student("Arjun\n")
print(s2.name)

#Eg.4]

class Wishes:
    college_name1 = "IIT BOMBAY"
    college_name2 = "Parul University"
    def __init__(self, car, colour, apartment, crush,marks):
        # here self is reference for object,whereas self.name..etc are instance attributes which means they are different for different 
        self.car = car
        self.colour = colour
        self.apartment = apartment
        self.crush = crush
        self.marks = marks

        print(Wishes.college_name1) # This will be common for both conditions. 

        print("\nMy Dream Car is:", self.car)
        print("Colour of that Car will be:", self.colour)
        print("I wish I had a", self.apartment)
        print("My crush is:", self.crush)
        print("I wish i could score",self.marks,"\n")

# Creating a single instance with all required arguments
wishes1 = Wishes("Mercedes", "Black", "Villa", "Samay Raina",10)

wishes2 = Wishes("alto","grey","1RK on rent","kangana ranaut","Pass without KT's\n")

#Eg.5]
class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Hey student tell me your name and marks : ")

    def your_name(self):
        print("My name is :",self.name)
   
    def your_marks(self):
        print("My marks are : ",self.marks)
s1 = Student("Karan",97)
s1.welcome()  # This is the function call
s1.your_name()
s1.your_marks()
