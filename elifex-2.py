num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
print("1. + for addition","2. - for subtraction","3. * for multiply","4. / for divide")
operator=input("enter your choice: ")
if num1==45 and num2==3 and operator=="*":
    print("555")
elif num1==56 and num2==9 and operator=="+":
    print("77")
elif num1==56 and num2==6 and operator=="/":
    print("4")
elif operator=="+":
    num3=num1+num2
    print(num3)
elif operator=="*":
    num3=num1*num2
    print(num3)
elif operator=="-":
    num3=num1-num2
    print(num3)
elif operator=="/":
    num3=num1/num2
    print(num3)
else:
    print("error,please check input!")