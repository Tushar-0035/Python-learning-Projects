list1=[["tushar",1],["vansh",2],["himanshu",3],["nikhil",4]]
dict1=dict(list1)
#print(dict1)
#print(list1)
#print(list1[3])
"""
for item,lollipop in list1:
    print(item,lollipop)
"""
for item,lollipop in dict1.items():
    print(item,lollipop)

#if you want only key from dict.
#for item in dict1:
    #print(item)

"""
quiz: make a list and check the items in the list if items are numerical and greater than 6
then print the items.
"""
"""
list2=["tomato","potato",76,3,5,"ladyfinger",14,int,float,6,3,77,43]
for item in list2:
    if str(item).isnumeric() and item>=6:
        print(item)
"""