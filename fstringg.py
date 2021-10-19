me="a boy"
a="this is %s"%me
print(a)

#another method:
me="a boy"
ag=19
a="this is %s and his age is %s"%(me,ag)
print(a)

#another method:
me="a boy"
ag=19
a="this is {} and his age is {}"
#a="this is {1} and his age is {0}: iska mtlb h jo 1 index pr h vo pehle print hoga fir dusre index wala print hoga
b=a.format(me,ag)
print(b)

# now use of f-string: this means fast and easy way
me="a boy"
ag=19
a=f"this is {me} and his age is {ag}"
print(a)

# f-string m ham variable expression ka and module ka bhi use kr skte h
#example:
import math
me="a boy"
ag=19
a=f"{25*5},{math.cos(180)}"
print(a)

