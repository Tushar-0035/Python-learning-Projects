veg=["potato","tomato","branjal","ladyfinger"]
i=1
for item in veg:
    if i%2!=0:
        print(f"please buy {item}")
    i+=1
#another method
#enumerate func: isse hm kisi bhi list m s koi s bhi item ko delete kr skte h easy way m
veg=["potato","tomato","branjal","ladyfinger"]
for index,item in enumerate(veg):
    if index%2==0:
        print(f"\nplease buy {item}")