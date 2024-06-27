collection = {1,2,3,4}

print(collection)
print(type(collection))

set1 = {88,9.4,"41","Honey",88,"yo","yo"} #after seeing the output it can be said that sets ar unordered and secondly it ignores the duplicate values.
print(set1)
print(len(set1)) #even length function ignores duplicate values.

#empty set looks like:
items = set()

items.add(1) #to add elements to any set.

items.add("Pata nhi")

items.add(1)

items.add("kuch bhi karlo")

items.add((1,2,3)) #tuples can be added but lists and dictionaries cannot be.

print(items) # here also duplicate values are not added
 
items.remove("kuch bhi karlo") #to remove some particular item.
print(items)

items.clear() #makes the set a null set.
print(items)
