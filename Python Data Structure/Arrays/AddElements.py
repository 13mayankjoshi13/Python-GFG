import array as arr
a = arr.array('i', [1, 2, 3])
print(*a)

a.insert(1, 4)  # Insert 4 at index 1
print(*a)
