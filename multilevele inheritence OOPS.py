class electronic_device:
    no_of_elcgadget = 3
    def __init__(self,name1,name2,name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    def printlist(self):
        print(f"1.{self.name1} 2.{self.name2} 3.{self.name3}")

class pocket_gadget(electronic_device):            
    pocket_gadget = "smartphones"
    def ispocket_gadget(self):
        print({self.pocket_gadget})

class phone(pocket_gadget):
    # no_of_elcgadget = 12
    def __init__(self,type1,type2,type3):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3


    def types(self):
        print(f"1.{self.type1},{self.type2},{self.type3}")

A= electronic_device("laptop","refrigerator","LED")
B= pocket_gadget("watch","bluetooth","headphones")
C= phone("android","ios","microsoft")
C.types()
print(C.no_of_elcgadget)
