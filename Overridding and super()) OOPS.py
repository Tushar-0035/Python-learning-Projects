class A:
    classvar1= 98
    def __init__(self):
        self.var1= "this is instance variable var1 in B"
        self.classvar1="this is classvar1 in class A"
        self.special="special"

class B(A):
    def __init__(self):
        super().__init__()

        self.var1="this is instance variable var1 in B"
        self.classvar1="this is classvar1 in class B"
        # print(super().classvar1)

a=A()
b=B()
# print(b.classvar1)
#print(b.special)  agr ham ise print krenge to ye error dega kyuki ye override ho chuka h to class A ka init constructor
#chalega hi nhi........and agr hame print krna h to hame super() function ka use krna hoga jaise ki line no. 10 mai hora h
print(b.special,b.var1,b.classvar1)  #ye class B ke variable (var1 and classvar1) ko print krdega kyuki hamne super() pehli use kr liya tha
#because ye pehle super() constructor m jayega fir niche class B m aayega to variables change ho jayega.
