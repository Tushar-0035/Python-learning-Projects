num1=input("enter 1st number\n")
num2=input("enter 2nd number\n")
try:
    print("the sum of two numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)
print("this is very important")