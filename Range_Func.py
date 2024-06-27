seq = range(5)
print(seq[0]) #To print the numbers of the range.
print(seq[1]) #To print the numbers of the range.
print(seq[2]) #To print the numbers of the range.
print(range(5)) #To print the range.

# second way is using loops:

seq = range(5) #this 5 is the stopping condition
for i in range(5): #here in place of for i in range(5): we can also write... for i in seq:
    print(i)  

seq = range(2,10)
for i in range(2,10):
    print(i) #here 2 is the starting condition and 10 is the stopping condition.

seq = range(2,10,3) #here 2 is the starting condition and 10 is the stopping condition and 3 is the step condition
for i in range(2,10,3):
    print(i)

# For printing odd numbers between 1 to 100

i = range(1,101,2)
for num in range(1,101,2):
    print(num)  


