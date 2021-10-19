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
def num():
    print("i am very good boy")
    print("And very punctual")
num()