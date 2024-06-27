#WAP to find the greatest of 3 numbers entered by the user

a = int(input("Enter first no. "))
b = int(input("Enter Second no. "))
c = int(input("Enter Third no. "))
if(a > b and a > c):
    print(str(a) , " is the greatest")
elif(b > a and b > c):
    print(str(b) + " is the greatest")
else:
    print(str(c) + " is the greatest")

#str(a), str(b), str(c) are used to get that actual value of a, b , c in our outputs
    