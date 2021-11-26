#Generators: generators ek trha k iterators hote h jinhe ek baar traverse kiya jata h
def fact(n):
    f=1
    for i in range(1,n):
        f=f*i
        yield f   #isse generator ki pehchan hoti h
g= fact(6)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())