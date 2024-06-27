# Break: Terminates the loop when encountered
#Eg.1]
i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

#Eg.2]
nums = (1,4,9,16,25,36,49,64,81,100)
idx = 0
x = 36
while idx < len(nums):
    if(nums[idx] == x):
        print("Finded the number at index",idx)
        break
    else:
        print("Finding")
        idx += 1

#Continue: It is a keyword that terminates the current execution and continues execution of the loop with next iteration

#Eg.1]

i = 1
while i<=5:
    if(i==3):
        i += 1
        continue # This acted as skip and 3 was skipped.
    print(i)
    i += 1

#Eg.3] Print Just Odd Numbers and skip the even numbers from 1 to 10

i = 1
while(i<=10):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1




