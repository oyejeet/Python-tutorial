tup = (65,77,82,41,77,77,82)
print(tup)

print(type(tup)) #to print class

print(tup[0]) #indexing

print(tup[0 : 3]) #slicing 65,77,82

print(tup.index(82))  #to find the index of the element at first occurence

print(tup.count(77)) #to count the no. of times the element got repeated inside the tuple

#syntax of tupple when there is only one element inside it
tup1 = (1,)
tup2 = ("hello",)

print(tup1)
print(type(tup1))

print(tup2)
print(type(tup2))