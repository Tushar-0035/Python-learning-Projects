# python comprehension basically is a method to present the list,dict,sets in a
# short manner
# list comprehension:
# to print n numbers:

# lis=[i for i in range(5)]
# print(lis)

# isme ham if ka use bhi kr skte h like:
lis = [i for i in range(100) if i%3==0]
print(lis)

# dictionary omprehension:
dict = {i:f"item{i}" for i in range(5)}
print(dict)

# sets comprehension:
set={dresses for dresses in ["dress1","dress2","dress1","dress2"]}
print(set)  #isme only dress1 and dress2 hi print honge kyuki ye set h aur isme
# duplicacy allow nhi hoti