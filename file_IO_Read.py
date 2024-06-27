f = open("/Users/indrajeetsinghbava/CODE /demoo.txt","r") #here we used a file saved in some other folder and copied its path and pasted that here.

Data = f.read() #will read the text in the file demoo.txt
print(Data) #will print the text in the file demo.txt

f.close()


f = open("/Users/indrajeetsinghbava/CODE /Python/file.txt","r") #here we used a file saved in same folder and copied its path and pasted that here.

Data = f.read(10) #will read the text in the file "file.txt" upto first 10 values including spaces and change of lines.
print(Data) # will print that first 10 characters.

f.close()

#Use of readline()
f = open("/Users/indrajeetsinghbava/CODE /demoo.txt","r") 

line1 = f.readline() #To read the first line
print(line1)         #To print that first line

line2 = f.readline() #To read the second line
print(line2)         #To print the second line
f.close()


#Important note: If once we read a particular part of the file or the complete file then we can't read that line again even if we pass some other argument

#Eg]

f = open("/Users/indrajeetsinghbava/CODE /demoo.txt","r") 

data = f.read()
print(data)
#Here the variable "data" read the complete text file and printed it so when we passed other arguments like "line1" & "line2" we will get blank spaces in place of them.
line1 = f.readline() 
print(line1)         

line2 = f.readline() 
print(line2)        
f.close()

# use of (with) syntax:

with open("/Users/indrajeetsinghbava/CODE /demoo.txt","r") as f:
    data = f.read()
    print(data)

with open("/Users/indrajeetsinghbava/CODE /demoo.txt","w") as f:
    data = f.write("new data")
    
