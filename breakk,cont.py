
i=0
while(True):
    if(i+1<5):
        i=i+1
        continue
    print(i+1)
    if(i==9):
        break
    i=i+1
#quiz:
"""
while(True):
    num= int(input("enter the number"))
    if(num<=100):
        continue
    print("congratulation! you have entered number greater than 100")
    if(num>100):
        break
"""