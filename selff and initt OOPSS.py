class employee:
    no_of_leaves = 8
    def __init__(self,name,age,post):  #ise khte h constructor ye argument dene k liye use kiya jata h
        self.name= name
        self.age= age
        self.post = post
    def printdetails(self):  #self: self ka mtlb h vo object jiski baat ki jari h
        return f"name is {self.name} age is {self.age} and post is {self.post}" #yha pr self vo ho jayega jispr ham
    # printdetails func use krenge i.e tush pr ya verma pr.
tush = employee("tushar","19","engineer")
verma = employee("verma","20","web developer") #isme ham bina __init__ k agr arguments dete h to ye error show krega

# tush.name="TUSH"
# tush.age = "19"
# tush.post = "software engineer"

# verma.name="VERMA"
# verma.age="20"
# verma.post = "web developer"

print(verma.printdetails())
print(verma.name)
print(verma.age)
