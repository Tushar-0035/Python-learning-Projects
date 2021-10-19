class employee:
    no_of_leaves = 8
    pass
    def __init__(self,name,age,post):
        self.name = name
        self.age = age
        self.post = post

    def printdetails(self):
        return (f"name is {self.name} age is {self.age} and post is {self.post}")


    def __add__(self, other):    #this is called dunder method: jo bhi double underscore s start hota h
        return(self.age + other.age)

    def __truediv__(self, other):
        return (self.age/other.age)

    def __repr__(self):      #ye method object ko print karane m use hota h
        return (f"employee({self.name},{self.age},{self.post})")

    def __str__(self):
        return self.printdetails()

tush = employee("tushar",19,"student")
verma = employee("verma",22,"programer")
#print(tush+verma)     #this is called operator overloading
# print(tush/verma)
print(tush)    #ye only str hi print karega
print(repr(tush))  #agr hme object ko print karana h to __repr__ ka use krte h and if str methods bhi ho to yha print
# str hi hoga na ki repr agr hame repr ko print karan h to use call krna hoga like print(repr(tush)).



