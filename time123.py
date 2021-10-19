import time

initial=time.time()

for i in range(10):
    print("this is tushar")
    time.sleep(2) #sleep function 2 second tk rokega fir print krta h
print("for loop ran in",time.time()-initial,"seconds")

initial2=time.time()
i=0
while(i<10):
    print("this is tushar")
    i+=1
print("while loop ran in",time.time()-initial2,"seconds")

localtime=time.asctime(time.localtime(time.time())) #here asctime is present to change tuple into given time format
print(localtime)