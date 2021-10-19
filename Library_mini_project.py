class library:
    def __init__(self,library_name,listofbooks):
        self.library_name = library_name
        self.listofbooks = listofbooks

    def displaybook(self):
        print(f"list of books is {self.listofbooks}")

    def lend_book(self):

    def add_book(self):
        pass
    def return_book(self):
        pass
A=library("S.K library",["engg. Mathematics","General awareness","human values","c programming","data structures"])
print(A.listofbooks)
A.displaybook()

