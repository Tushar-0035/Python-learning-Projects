from prettytable import PrettyTable
mytable=PrettyTable(["student name","class","section","marks"])
mytable.add_row(["Tushar","B.tech","B","98%"])
mytable.add_row(["Yash","B.tech","D","96%"])
mytable.add_row(["Arya","B.tech","A","75%"])
mytable.add_row(["Aditya","B.tech","A","85%"])
print(mytable)
