class employee:
    no_of_leaves = 8  #this is called class variable
    pass
    def __init__(self,name,age,post):
        self.name = name
        self.age = age
        self.post = post

#........................CLASS METHOD..........................................

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


tush = employee("tushar","19","student")
verma = employee("verma","22","programer")

tush.change_leaves(23)
print(employee.no_of_leaves)
print(tush.name)
