"""def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac = fac *(i+1)
    return fac
number=int(input("enter the number"))
print(factorial_iterative(number))

#recursive method
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return(n*factorial_recursive(n-1))
number=int(input("enter the number"))
print("factorial using recursion",factorial_recursive(number))
"""
#quiz: print fibonacci series
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("enter the number"))
print("fibonacci series:",fibonacci(number))


