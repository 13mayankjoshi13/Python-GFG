def fun(func, arg):
    return func(arg)
  
def square(x):
    return x ** 2
  
res = fun(square, 5)
print(res)

#Functions are first-class objects, which means you can pass functions as arguments to other functions, allowing you to call it inside that function.