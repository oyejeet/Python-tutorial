info = {
    "key" : "value",
    "name" : "GOD Indrajeet",
    "hobbies" : "Sketching"+ "& " + "Playing Chess",
    "age" : 19,
    "is adult" : True,
    "Languages" : ["C","C++","Python","Java"],           #list
    "favmovies" : ("Arijit Singh","Sonu Nigam","KK"),    #Tuple
    12.99 : 94.4,                                        #keys can be float or integers as well
    12 : 96.8,
}
print(info["name"])
print(info["hobbies"])
print(info["key"])
print(type(info))
info["name"] = "Oyeejeet"                               #to change the value of name
info["surname"] = "Singh"                               #this way we added one more key to our dictionary
print(info)


# we can also add tuple and lists inside our dictionary
# mostly strings are made our key in dictionaries, tuple and lists are not much used in dictionaries