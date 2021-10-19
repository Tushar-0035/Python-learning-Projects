# *args ka mtlb hota h ham apni list mai function ko bina change kre hue kuch bhi add kr skte h
def funcargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(F"{key} is a {value}")
a=["Tushar","Arya","Yash","Nikhil","aditya"]
nor="this is normal arguments"
kw={"\ntushar":"intelligent boy","arya":"handsome boy","yash":"good fighter"}
funcargs(nor,*a,**kw)
