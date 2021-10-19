class employee:
    no_of_leaves = 8  #this is called class variable
    pass

tush = employee()
verma = employee()

tush.name="TUSH" #this all called instances variable
tush.age = "19"
tush.post = "software engineer"

verma.name="VERMA"
verma.age="20"
verma.post = "web developer"
print(verma.__dict__) #ye "dict" yha pr dictionary ke liye use hota h

employee.no_of_leaves = 9 #agr ham class ki help s class variable ki value ko change krte h to value change ho jayegi
#tush.no_of_leaves = 9    # isse nhi hogi change
print(employee.no_of_leaves)