"""def add(a,b):
    return (a+b)
print(add(2,6))
"""

#lambda function ki help s hme function nhi bnana pdta
minus=lambda x,y:x-y
#def minus(x,y):
 #   return x-y
print(minus(9,4))

a=[[1,23],[4,2],[5,10]]
a.sort(reverse=True,key=lambda x:x[1])
print(a)
