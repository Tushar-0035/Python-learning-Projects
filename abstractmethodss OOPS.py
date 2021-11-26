from abc import ABC,abstractmethod
class shape(ABC):          #yha iss class ka mtlb h ki ye kehta h ki agr shape class s inherit krre ho to jo ye mthod h
                           #ise apni dusri class m define kro
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type="rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return(self.length*self.breadth)

a=rectangle()
print(a.printarea())
#print(a.type)
