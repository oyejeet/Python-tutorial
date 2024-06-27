def show(n):
    if(n == 0): # this is a base case, which is like a stoping condition
        return #simply stops the recursion when n is 0. It doesn't need to return any value because we only want to end the recursion.
    print(n)
    show(n -1) 
    
show(5)

# If we wrote print(n) above the return statement then then we will get 0 in our output as well

def show(n):
    if(n == 0):
        print(n)
        return
    show(n-1)
show(5)

# WAP using recursion to get factorial of a number n:

def fact(n):
    if(n == 0):
        return 1
    return fact(n -1) * n
print(fact(5))
