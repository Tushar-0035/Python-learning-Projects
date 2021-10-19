class employee:
    no_of_leaves = 8
    pass

    def printdetails(self):
        print(f"name is {self.name} age is {self.age} and post is {self.post}")

    def __init__(self,name,age,post):
        self.name = name
        self.age = age
        self.post = post

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

class player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name= name
        self.game = game
    def printplayer(self):
        print(f"name is {self.name} game is {self.game}")

class coolprogrammer(employee,player):      #this is called multiple inheritence
    languages = "python"
    def printlanguage(self):
        print({self.languages})

tush = employee("tushar","19","student")
verma = employee("verma","22","instructor")

shera = player("shera",["cricket"])
veera = coolprogrammer("veera","21","programmer")
# print(shera.no_of_games)
shera.printplayer()
veera.printdetails()
veera.printlanguage()