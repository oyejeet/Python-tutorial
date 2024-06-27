# The write method expects a string argument.

# 1]use of "w" mode
f =  open("/Users/indrajeetsinghbava/CODE /Python/file.txt" , "w")  # w is used to overwrite

f.write("Is it worth it to learn python?") #by this our entire text in file.txt gets overwrite by this new text "Is it worth it to learn python?"


f.close()

# 2]use of "a" mode
f =  open("/Users/indrajeetsinghbava/CODE /Python/file.txt" , "a")  # a is used to append the text 

f.write("\n Is it worth it to learn python?") #by this a new text "Is it worth it to learn python?" gets added at the end of the whole text in file.txt

f.close()

# 3]To create a file that  doesn't exist  

f = open("sample.txt","a") # and now we can perform operations like read and write inside it.
f.close

# 4] use of r+
#note r+ have no truncate
f = open("/Users/indrajeetsinghbava/CODE /r+_w+_a+_example.txt","r+")

f.write("abc") # so it just overwrites the first 3 char that were "abc" and then replaced it with "Thi" in the main text.

print(f.read()) # here the pointer is now at "s ..." and reads from there because we passed "abc" over here.

f.close()

# 5] use of w+ and also f.seek(0)

f = open("/Users/indrajeetsinghbava/CODE /r+_w+_a+_example.txt","w+")

f.write("abc") # w+ truncates the file i.e removes entire existing text from the linked text file.
 
f.seek(0) # The seek(0) method moves the file pointer to the beginning of the file, allowing subsequent read operations to start from the beginning.

print(f.read()) # now if f.seek(0) wasn't passed then nothing would have been printed on the terminal, since the main text file was truncated and eventhough we passed the print(f.read()) command after overwritng "abc" in the text file,but since the pointer is now passed the third place because of "abc" and since the main file was truncated there would have been empty space in the terminal for this print statement.


f.close()

# 6] use of a+

f = open("/Users/indrajeetsinghbava/CODE /r+_w+_a+_example.txt", "a+") #a+ will not truncate the main file.

f.write("\n123")
f.seek(0) # could'nt be print without seek(0) since the pointer is at the end
print(f.read())
f.close()