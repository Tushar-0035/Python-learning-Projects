class employee:
    no_of_leaves = 8
    pass

    def printdetails(self):
        print(f"name is {self.name} age is {self.age} and post is {self.post}")

    def __init__(self,name,age,post,):
        self.name = name
        self.age = age
        self.post = post

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

class programmer(employee):  #this is called single inheritence ek class ke andar dusri class bnana

    def __init(self,name,age,post):
        self.name= name
        self.age = age
        self.post = post

tush = employee("tushar","19","student")
verma = employee("verma","22","instructor")
shera = programmer("shera","21","programmer")
tush.change_leaves(23)
print(employee.no_of_leaves)
# print(verma.name)
# tush.printdetails()
shera.printdetails()
print(shera.name)