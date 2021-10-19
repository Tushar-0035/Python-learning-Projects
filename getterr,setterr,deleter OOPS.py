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


A=employee("Tushar","verma")
B=employee("shiva","mittal")
#print(A.explain())
A.fname="tush"  #ham yha pr fname ko change krna chate h but ye nhi hoga change
#print(A.email)  #agr ham iss print statement s print krenge email to whi ayegi tusharverma wali email.
#print(A.email())  #ye aayegi modified hokr jo ki email methods k through aari h
#print(A.email)  #agr ham chate h ki function ko call na krna pde to ham apne method m property decorator ka use krte h
A.email= "this.that@gmail.com"
print(A.email)
del A.email     #iske liye deleter bnana hota h jisse ham kisi ko delete kr skte h: jaise ki uper bnaya hua h
print(A.email) #agr ham ise ab print krenge to ye none ko print kr dega...kyuki oop m kuch bhi delete nhi hota isiliye
                 # ham none de dete h deleter method m.