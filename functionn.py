a=2
b=4
c=sum((a,b))
#print(c)

def func1(a,b):
    print("hello g\n",a+b)
func1(2,5)

def func2(a,b):
    """this gives the average"""
    average=(a+b)/2
    #print(average)
    #return(average)
    #this will return none if we will not use return statement
    return(average)
avg=func2(2,5)
print(avg)
#this is called docstring:
print(func2.__doc__)