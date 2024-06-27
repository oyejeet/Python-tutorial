# Functions are the group of statements that perform specific tasks.

#Eg.1] Writing sum of two numbers:

# Function definition
def calc_sum(a,b): #a,b are parameters
    sum = a + b    # Some work
    print(sum)     # Will print that work
    return sum     # if you need to use the result of the function elsewhere in your code, returning it allows you to do that.

calc_sum(5,10)     # Function Call ;arguments
calc_sum(11,4.23)  # Function can be called several times.

# Funtions are used to reduce the redundancy of the code, i.e to reduce the repetitive and unnecessary lines in our code 


# avg of 3 numbers

def calc_avg(a,b,c):
    avg = (a + b + c)/3
    print(avg)
    return avg

calc_avg(1,2,3)
calc_avg(22,33,44)
  

# Default Parameters : Assining some vslue to the parameters and keeping the argument part empty

def calc_prd(a = 2 , b = 2):
    prd = a*b
    print(a * b)
    return a * b
calc_prd()  # it will print the prd of default values to the parameters
calc_prd(1,3) # here prd will be printed based on the value to the arguments.