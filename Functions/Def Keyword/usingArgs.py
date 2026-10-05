def fun(*args):
    for arg in args:
        print(arg)

fun(1, 2, 3, 4, 5)

#*args allows a function to accept a variable number of positional arguments, which are collected into a tuple, making the function flexible to handle multiple inputs.