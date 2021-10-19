#__________________MAP_____________________________
"""
lis=["23","5","10","15"]
lis=list(map(int,lis))

#for i in range(len(lis)):
#    lis[i]=int(lis[i])
lis[3]=lis[3]+1
print(lis[3])
"""

#another method: use of lambda func with map func
sq=[1,2,3,4,5]
a=list(map(lambda x:x*x,sq))
print(a)

#_____________________FILTER_________________________
lis1=[1,23,8,2,5,6,78]
def is_greater_5(num):
    return num>5
greater_5=list(filter(is_greater_5,lis1))
print(greater_5)

#_____________________REDUCE_________________________
from functools import reduce
#reduce fun ko use krne k liye hme ise import krna pdta h functool module m s

lis2=[1,2,3,4,5]
#agr hme "sum" print krna h sbhi item ka jo list m present h to hum reduce func ka use kr skte h
sum=reduce(lambda x,y:x+y,lis2)
print(sum)



