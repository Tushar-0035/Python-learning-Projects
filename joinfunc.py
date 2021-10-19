lis = ["chowmien","burger","momos","chillipotato"]
#normally ham ese "and" ko use krke words ko join kr skte h for loop lga kr
"""
for item in lis:
    print(item,"and",end=" ")
print("other chineese food")
"""

#another method :join function
a=" and ".join(lis)
print(a,"and other chineese food")
#we can use commas and other seperating word
a=" , ".join(lis)
print(a,", other chineese food")
