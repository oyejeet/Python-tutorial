list = [2,1,3]
list.append(4) #to add one more element to our list
print(list)
#alaways keep the syntax this way

list.sort() #sorts in ascending order
print(list)

list.sort(reverse = True) #sorts in descending order
print(list)

list.reverse #to reverse the list
print(list)

list.insert(1,5) #to insert any element by giving its index no.
print(list)

list.remove(4) #to remove the first occurence of the element entered
print(list)

list.pop(3) #to remove the element at that index
print(list)


#note: all the value gets updated and passes to the next operation, like when we performed the append operation at very first then the list variable gets updated and further updates and operations will be done in this new list
#in short (new list = list)
