from prettytable import PrettyTable
#Specify the column names
mytable=PrettyTable(["student","class","section","percentage"])
#add rows
mytable.add_row(["Tushar","12","A","89.4 %"])
mytable.add_row(["Arya","12","c","69 %"])
mytable.add_row(["Yash","12","B","92.18 %"])
mytable.add_row(["Aditya","12","A","84.6 %"])
mytable.add_row(["sonu","12","A","65 %"])
print(mytable)