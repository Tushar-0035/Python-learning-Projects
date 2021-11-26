"""
Decorators is a function which accepts the another function as a parameter and returns the function.
A decorators takes the result of a function,modifies the result and returns it.
we use @function_name to specify a decorator to be applied on a another function.
"""
def decor(num):
    def inner():
        print("function before enhancing")
        num()
        print("after enhancing")

    return inner
@decor
def who_is_tush():
    print("He is very good boy")
    print("And very punctual")
#who_is_tush= decor(who_is_tush) #ese bnate h decorator....aur jo uper short m @decor likha h vo iska short tarika h
#ham vo hi use krna prefer krte h
who_is_tush()
#uses of decorators: jab hame ek hi kamm 10 function k sath krna ho