### lamdas ###

# Lambdas are one line functions. They are also known as anonymous functions in some other languages. You might want to use lambdas when you don’t want to use a function twice in a program. They are just like normal functions and even behave like them.

# Lambda functions are used extensively along with built-in functions like filter(), map()

# Syntax:
# lambda arguments: expression

# Example:
# lambda x: x * x


# Example 1: Create a lambda function that adds 10 to the number passed in as an argument, and print the result:

# x = lambda a : a + 10

# print(x(5))

# Example 2: Lambda functions can take any number of arguments:

# x = lambda a, b : a * b

# print(x(5, 6))


sum=lambda first, second : first + second

print(sum(5,6))

