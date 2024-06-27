# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# Eg.1] using '+' operator:

print(1 + 2) #3
print("Iron" + "Man") # IronMan
print([1,2,3] +[4,5,6]) #[1,2,3,4,5,6]

# everywhere the meaning of '+' operator is different, because of which the + operator is overloaded 

print("\n")
# Use of dunder functions: 
# Program to add complex numbers 

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"+ ",self.img,"i")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,3)   # Don't get confused, arguments stored in num1 are basically values of self.real and self.img .
num1.shownumber()

num2 = Complex(4,6)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()





