# In Python array is not a built-in data structure and therefore need to imported
# Array is a module which is a collection of elements of similar data types ,i.e collection of homemgenous elements.

# Syntax to get array imported : 


from array import *           # This statement means from array import everything.
# M1
a1 = array('i',[23,56,11])    # Here 'i' is the type code which means signed integer
print(type(a1))
print(a1) 

# # M2
# for x in a1:
#     print(x)
    
# # M3
# for i in range(len(a1)):
#     print(a1[i])

# M4
# i = 0
# while(i<len(a1)):
#     print(a1[i])
#     i += 1

# Functions in array :

a1.append(20)           # Will add the element 20 next to the last index inside the array a1.
print(a1)               

print(a1.count(23))     # Will count the no. of occurence of 23 in the array a1.

print(a1.index(11))     # Will print the index at which the element '11' resides in array a1.

print(a1.pop())         # Will remove the element at the last index by first returning it back to the user.
print(a1)

print(a1.pop(0))        # Will remove the element at zeroth index by first returning it back to the user.

a1.append(56)
print(a1)

a1.remove(56)           # Will remove the element 56 from its first occurence.
print(a1)