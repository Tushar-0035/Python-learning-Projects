class employee:
    no_of_leaves = 8   #this is called public variable: because ise ham kisi bhi class m use kr skte h
    _protect= 12    #this is called protected variable: ise bs ham usi class m use kr skte h jo employee k andr aati ho
    __priv= 11  #this is called private variable: ye variable only isi class m run hoga isse bnne wali kisi bhi dusri
    #class m run nhi ho skta

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

em=employee("tushar","19","student")
print(em._protect)              #print krne ka tarika h protected variable ko
print(em._employee__priv)       #print krne ka tarika h private variable ko