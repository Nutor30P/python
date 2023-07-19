##String##

my_string = "Hello World"

my_other_string = 'Hello World'

print(my_string)
print(my_other_string)

# String Concatenation

my_string = "Hello" + " " + "World"

print(my_string)


# String Formatting

name = "John"
age = 23

print("%s is %d years old." % (name, age))

# String Methods

my_string = "Hello World"

print(my_string.upper())

print(my_string.lower())

print(my_string.split())

print(my_string.find("World"))

print(my_string.count("l"))

print(my_string.replace("World", "Universe"))

print(my_string.strip())

print(my_string.isnumeric())

print(my_string.isalpha())

print(my_string[0])

print(my_string[0:5])

print(my_string[6:])

print(my_string[-1])

print(my_string[-5:-1])

print(my_string[::-1])

print(my_string[::2])

print(my_string[1::2])

print(my_string[1:8:2])


# String Formatting 

name = "John"
age = 23

print("{} is {} years old.".format(name, age))

print("{0} is {1} years old.".format(name, age))

print("{name} is {age} years old.".format(name="John", age=23))

print("{name} is {age} years old.".format(name=name, age=age))

print("{name} is {age} years old.".format(**locals()))

print(f"{name} is {age} years old.")

print(f"{name.upper()} is {age} years old.")

print(f"{name} is {age + 5} years old.")

print(f"{name} is {age:<10} years old.")

print(f"{name} is {age:>10} years old.")

print(f"{name} is {age:^10} years old.")

print(f"{name} is {age:=^10} years old.")

# String Escape Sequences

my_new_line = "This is a new line \n"

print(my_new_line)

my_tab = "This is a tab \t"

print(my_tab)

my_backslash = "This is a backslash \\"

print(my_backslash)

my_single_quote = "This is a single quote \'"

print(my_single_quote)

my_double_quote = "This is a double quote \""

print(my_double_quote)

my_backspace = "This is a backspace \b"

print(my_backspace)

my_carriage_return = "This is a carriage return \r"

print(my_carriage_return)

my_form_feed = "This is a form feed \f"

print(my_form_feed)

my_vertical_tab = "This is a vertical tab \v"

print(my_vertical_tab)



# String Operators

my_string = "Hello World"

print(my_string + "!!!")

print(my_string * 3)

print("Hello" in my_string)

print("Hello" not in my_string)

# String Slicing

lenguaje ="Python"

a, b, c, d, e, f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
