#here we will create a null dictionary
#null dictionary are mostly used while writing code because we can add the keys later on while writing our program

null_dict = {} #this is a null dict
null_dict["name"] = "Oyeejeet"
null_dict["age"] = 19
print(null_dict)

# nested dictionaries

student = {
    "name" : "Indrajeet",
    "marks" : {
        "phy" : 95,
        "chem" : 97,
        "maths" : 92
    }
}

print(student["marks"])
student["marks"]["phy"] = 90 #marks of physics will get changed
student["marks"]["english"] = 98 #added one more value in our nested dictionary
print(student)
print(student.keys()) #to return keys of outer layer not the nested one

print(list(student.keys())) 
print(tuple(student.keys())) #to type cast the dictionary into a list or tuple

print(len(student)) #to get no. of elements in the dictionary

print(student.values()) #return only the values not the keys

print(student.items()) #returns all key value pairs as tuples
