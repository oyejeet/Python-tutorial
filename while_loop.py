count = 1
while count <= 5:
    print("hello")
    count = count +1
print(count) #to know what is the final value of count
print("\n") 

#If we wrote count just aligning it below count = count+1 then that print(count) statement will be counted as part of loop, and will give the output accordingly.

#Print numbers from 1 to 100
num = 1
while num<=100:
    print(num)
    num = num+1

#Print numbers from 100 to 1

num = 100
while num<=1:
    print(num)
    num = num-1

#Print the multiplication table of a number n

n = int(input("Enter the number:"))
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i=i+1

#Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

n=1
while n<=10:
    print(n*n)
    n=n+1

#this was method 1
#method 2 is:

nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0 #while initializing the variable for the index always give it starting value of 0 , because the index always starts from zero.
while idx < len(nums):
    print(nums[idx])
    idx += 1 
  
#Search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)  

nums = (1,4,9,16,25,36,49,64,81,100) 
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index",i) 
    else:
        print("Finding")
    i += 1
# Important Note: This process of searching is called as linear search.