def outer(msg):
    def inner():
        return msg
    return inner

f = outer("Hello")
print(f())