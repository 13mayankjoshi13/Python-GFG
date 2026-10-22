import array as arr
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)

res = b[3:8]
print(res)

res = b[5:]
print(res)

res = b[:]
print(res)

Output
array('i', [4, 5, 6, 7, 8])
array('i', [6, 7, 8, 9, 10])
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

