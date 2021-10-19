l=10 #global variable
def func1(n):
    #l=5 #local variable
    global l #agar ham yha global keyword ka use nhi krenge to ye error dega kyuki ye global variable m incr. hora h
    l=l+15
    print(l)
    print(n,"I have printed")
func1("Its me")
#print(l)