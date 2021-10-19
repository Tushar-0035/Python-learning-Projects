# ......Object introspection means: iska mtlb hota h kisi bhi object k bare m janna ki vo kis type ka h vo kis
#  class s aaya h and etc.
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}{lname}@gmail.com"
    def explain(self):
        return f"this is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is deleted"
        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None


skillf=employee("skill","f")
print(skillf.email)
# print(type(skillf))  #this is called introspection
print(id(skillf))
print(dir(skillf))  #dir function hame object k bare m batata h ki uske andr kon kon s methods and attributes or
                     # instance varoiables h

import inspect
print(inspect.getmembers(skillf))