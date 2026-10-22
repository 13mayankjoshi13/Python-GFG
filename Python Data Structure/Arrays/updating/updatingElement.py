import array
a = array.array('i', [1, 2, 3, 1, 2, 5])
​
# update item at index 2
a[2] = 6
print(a)
​
# update item at index 4
a[4] = 8
print(a)

Output
array('i', [1, 2, 6, 1, 2, 5])
array('i', [1, 2, 6, 1, 8, 5])
