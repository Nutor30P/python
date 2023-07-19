### Error Types ###

# Syntax Error

# Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

# >>> while True print('Hello world')

#   File "<stdin>", line 1, in ?

#     while True print('Hello world')

#                    ^

# SyntaxError: invalid syntax

print "Hello world"

# Runtime Errors

# The next category of errors is runtime errors. Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Runtime errors are also called exceptions because they usually indicate that something exceptional (and bad) has happened.

# >>> 10 * (1/0)

# Traceback (most recent call last):

#   File "<stdin>", line 1, in ?

print(10 * (1/0))

# ZeroDivisionError: integer division or modulo by zero

# >>> 4 + spam*3

# Traceback (most recent call last):

#   File "<stdin>", line 1, in ?

# NameError: name 'spam' is not defined

print(4 + spam*3)

# Semantic Errors

# The third category is semantic errors. If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, your program will not do the right thing. It will do something else. Specifically, it will do what you told it to do.

# Identation Error

# Identation errors are the most common error in python. It is caused when the identation is not proper.

# Example:

def func():
print("Hello World")

func()

# Output:

#   File "main.py", line 2
#     print("Hello World")

# IndentationError: expected an indented block

# Name Error

# Name errors are caused when a variable is not defined.

# Example:

# print(a)

# Output:

# Traceback (most recent call last):

#   File "main.py", line 1, in <module>

#     print(a)

# NameError: name 'a' is not defined

# Index Error

# Index errors are caused when an index is not found in a list or a tuple.

# Example:

a = [1,2,3]

print(a[3])

# Output:

# Traceback (most recent call last):

#   File "main.py", line 3, in <module>

#     print(a[3])

# IndexError: list index out of range

# Attribute Error

# Attribute errors are caused when an attribute is not found in an object.

# Example:

a = 1

print(a.append(2))

# Output:

# Traceback (most recent call last):

#   File "main.py", line 3, in <module>

#     print(a.append(2))

# AttributeError: 'int' object has no attribute 'append'

# Key Error

# Key errors are caused when a key is not found in a dictionary.

# Example:

a = {'a':1,'b':2}

print(a['c'])

# Output:

# Traceback (most recent call last):

#   File "main.py", line 3, in <module>

#     print(a['c'])

# KeyError: 'c'

# Type Error

# Type errors are caused when an operation or function is applied to an object of an inappropriate type.

# Example:

a = 1

print(a + "Hello")

# Output:

# Traceback (most recent call last):

#   File "main.py", line 3, in <module>

#     print(a + "Hello")

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

