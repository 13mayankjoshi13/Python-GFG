a = "5"
b = 't'
n = int(a)

print(n)
print(type(n))

print(int(b))
print(type(b))



"""Output

5
<class 'int'>
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipython-input-1957009883.py in <cell line: 0>()
      9 print(type(n))
     10 
---> 11 print(int(b))
     12 print(type(b))
ValueError: invalid literal for int() with base 10: 't'"""