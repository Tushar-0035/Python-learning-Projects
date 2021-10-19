d1={}
#print(type(d1))
d2={"tushar":"biryani","neetu":"momos","manisha":"maggie"}
#print(d2)
#print(d2["tushar"])
d2["himanshu"]="biscuit"
#print(d2)
del d2["himanshu"]
#print(d2)
d3=d2.copy()
del d3["tushar"]
#print(d3)
#print(d2.get("tushar"))
d2.update({"himanshu":"biscuit"})
#print(d2)
print(d2.keys())
print(d2.items())
