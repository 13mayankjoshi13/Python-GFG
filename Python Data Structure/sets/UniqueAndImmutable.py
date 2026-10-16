# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
s[1] = "Hello"
print(s)

#output: {'Geeks', 'for'}
#TypeError: 'set' object does not support item assignment
