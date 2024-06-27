#grade of students based on marks

marks = int(input("Enter Marks:"))
if(marks >= 90):
    print("grade = 'A'")
elif(marks >= 80 and marks < 90):
    print("grade = 'B'")
elif(marks >= 70 and marks < 80):
    print("grade = 'C'")
elif(marks < 70):
    print("grade = 'D'")
else:
    print("Invalid Marks")
#in place of print if and elif statements we can also write that without using the print statement
