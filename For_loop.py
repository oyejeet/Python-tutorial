# Eg.1] 
nums = [1,2,3,4,5]
for val in nums :
    print(val)

#Eg.2]
Fav_lang = ["Python God","C++","Java"]
for Lang in Fav_lang:
    print(Lang)

#Eg.3] In Tuples

num = (1,2,3,4,5)
for val in num:
    print(val)  

#Eg.4] In String

name = "Lovely Singh"
for char in name:
    print(char)

#For loop with else

# Eg.1]
name = "Lovely Singh"
for char in name:
    print(char)
else:
    print("is self obsessed")

#Note : This Else statement is always executed once the for loop ends, beacuse of which it cannot be executed in loops containing the break keyword in it.

# Eg.2]

name = "lovely Singh"
for char in name:
    if(char == "i"):
        break
    print(char)
else: #Here this else statement will not be printed because of the use of break. 
        print("YO")   
print("yo") #this will get printed since it is out of the loop and used without else.  
