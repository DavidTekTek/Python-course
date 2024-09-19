# function to find cube
def cube(num):
    return num*num*num

# define a function that execute the function cube if user enter number divisible by 3
def by_three(num):
    if num %3 == 0:
        return cube(num)
    else:
        return False
    
    # display result
    print(by_three(9))
    print(by_three(5))