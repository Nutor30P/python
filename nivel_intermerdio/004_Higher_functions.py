### higher order functions

# A function that takes a function as an argument, or returns a function as a result is called a higher order function.

# Example 1: Passing a function as an argument to another function:

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))

print(operate(dec,3))


# Example 2: Returning a function from another function:

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

# Outputs "Hello"

new()

# Example 3: Python program to illustrate functions

# can be passed as arguments to other functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)

# Example 4: Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))


#built in higher order functions

# map() function

# map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# Syntax :

# map(fun, iter)

# Parameters :

# fun : It is a function to which map passes each element of given iterable.

# iter : It is a iterable which is to be mapped.

# NOTE : You can pass one or more iterable to the map() function.

# Returns :

# Returns a list of the results after applying the given function

# to each item of a given iterable (list, tuple etc.)

# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .


#with lambda
numbers = (1, 2, 3, 4)

result = map(lambda x: x * x, numbers)

print(list(result))

#with function

numers_2 = (1, 2, 3, 4)

def square(x):
    return x * x

result_2 = map(square, numers_2)

print(list(result_2))

# filter() function

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# Syntax :

# filter(function, sequence)

# Parameters :

# function : function that tests if each element of a

# sequence true or not.

# sequence : sequence which needs to be filtered, it can

# be sets, lists, tuples, or containers of any iterators.

# Returns :

# returns an iterator that is already filtered.

# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

#with lambda

numbers_3 = (1, 2, 3, 4)

result_3 = filter(lambda x: x % 2 == 0, numbers_3)

print(list(result_3))

#with function

numbers_4 = (1, 2, 3, 4)

def even(x):

    return x % 2 == 0

result_4 = filter(even, numbers_4)

print(list(result_4))

# reduce() function

# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

# Working :

# At first step, first two elements of sequence are picked and the result is obtained.

# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.

# This process continues till no more elements are left in the container.

# The final returned result is returned and printed on console.

# NOTE : reduce() is defined in “functools” module, need to import to use it, if direct call to reduce() is made then it works with global namespace and no import is required.

#with lambda

from functools import reduce

numbers_5 = (1, 2, 3, 4)

result_5 = reduce(lambda x, y: x + y, numbers_5)

print(result_5)


