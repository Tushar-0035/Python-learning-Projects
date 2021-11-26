class library:
    def __init__(self,library_name,listofbooks):
        self.name = library_name
        self.list = listofbooks
        self.lendDict = {}

    def displaybook(self):
        print(f"we have following books in our {self.name}")
        for book in self.list:
            print(book)

    def lendbook(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has been updated.you can take book now")
        else:
            print(f"book is already used by {self.lendDict[book]}")

    def addbook(self,book):
        self.list.append(book)
        print("Book has been added to the book list")

    def returnbook(self,book):
        self.lendDict.remove(book)

if __name__ == '__main__':
    A=library("S.K library",["c programming","engineering mathematics","Data structure","Database"])
    while(True):
        print(f"welcome to the {A.name}.enter your choice")
        print("1.display book")
        print("2.lend book")
        print("3.add book")
        print("4.return book")
        user_choice = int(input())
        if user_choice == 1:
            A.displaybook()
        elif user_choice == 2:
            book=input("enter the name of the book that you want to lend: ")
            user = input("enter the name: ")
            A.lendbook(book,user)
        elif user_choice == 3:
            book = input("enter the name of the book that you want to add")
            A.addbook(book)
        elif user_choice == 4:
            book = input("enter the book that you want to return")
            A.returnbook(book)
        else:
            print("not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="q" and user_choice2!="c"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue

