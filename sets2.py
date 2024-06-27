# two important set methods are   1]set union.
#2]set intersection.

set1 = {1,2,3}
set2 = {2,3,4,5}
set3 = {1,2,3,5,7,9}

print(set1.union(set2)) #will give combined value {1,2,3,4,5}

print(set2.union(set1)) #both are one and the same

print(set1.intersection(set2).intersection(set3)) #will take intersection of all the three sets
