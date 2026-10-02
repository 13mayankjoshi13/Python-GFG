# Precedence of 'or' & 'and'
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

    """Explanation:

and has higher precedence than or.
So name == "John" and age >= 2 is checked first.
Since name == "Alex" is already true, whole condition passes.
To fix this, use parentheses:

if (name == "Alex" or name == "John") and age >= 2:

Here, parentheses ensure the or part is checked first."""