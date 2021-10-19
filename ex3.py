n=18
nguesses=1
while (nguesses<=9):
    num=int(input("guess the number between 1 to 100: \n"))
    if num<n:
        print("greater number please")
    elif num>n:
        print("smaller number please")
    else:
        print("you win")
        print(nguesses,"no.of guess you took to finish")
        break
    print(9-nguesses,"no. of guess left")
    nguesses=nguesses+1

if(nguesses>9):
    print("game over")






