# .......Diamond shape prblm vo hoti h jisme confusion paida ho jata h ki konsi class konse method ko use kre......
# .....But python m ye confusion itna bada nhi hota kyuki isme easily pta lg jata h jaise ki below example de rakha h..
class A:
    def methd(self):
        print("this is me A")
class B(A):
    def methd(self):
        print("this is me B")
class C(A):
    pass
class D(B,C):
    pass
a=A()
b=B()
c=C()
d=D()
d.methd()