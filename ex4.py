num=int(input("how many row you want to print\n"))
boon=int(input("enter 0 or 1\n"))
new=bool(boon)
if(new==True):
    for i in range(1,num+1,1):
        for j in range(1,i+1,1):
            print("*",end=" ")
        print()
elif(new==False):
    for i in range(1,num+1,1):
        for j in range(num,i-1,-1):
            print("*",end=" ")
        print()



