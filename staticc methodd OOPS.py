class employee:
    no_of_leaves = 8  #this is called class variable
    pass
# ........................static method........................... ye hamara simple method hota jisme hame na to self
    #milta h aur na hi cls milta h as a argument.
    @staticmethod
    def simple_print(string):
        print("My name is " + string)
tush=employee()
tush.simple_print("tushar")
