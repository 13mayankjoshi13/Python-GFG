def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

fun(name="Olivia", age=30, city="New York")

#**kwargs lets a function accept any number of keyword arguments. These arguments are collected into a dictionary, with keys as argument names and values as their corresponding values.