#Add
def add(x,y):
    return (x+y)
#Subtract
def subtract(x,y):
    return (x-y)              #on master branch
#Multiply
def multiply(x,y):
    return x*y               #on Bug456 branch
#Divide
def divide(x,y):
    if y==0:                  #on Bug789 branch
        return DIVIDE_BY_ZERO_ERROR
    else:
        return x/y
