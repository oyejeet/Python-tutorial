# WAF to print the length of a list

names = ["Ramu","Shamu","Mammu"]
nums = [1,2,3,4,5]
def len_list(list):
    print(len(list))
    return len(list)
len_list(names)
len_list(nums)
  
# WAF to print elements of a list in a single line.(list the parameter)

names = ["Ramu","Shamu","Mammu"] 
Marks = [94,98,69]
def print_list(list):
    for items in list:
        print(items, end= " ")

print_list(names)
print("\n")
print_list(Marks)


    
