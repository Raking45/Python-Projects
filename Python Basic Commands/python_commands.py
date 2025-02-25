"""
Description:  Python commands to practice & learn.
Author: Robert King
Date: Feb 16, 2025 
"""

# To install a packages use: pip install package-name

# Use # for single line comments or """" for multi-line comments """" and ''' for multi-line comments '''

# Use empty print commands for whitespace
print()

# print command displays a message or object.
# print string
print("Print Command String Output")
print("Hello World!")
print()

# print integer
print("Print Command Integer Output")
a = 10
print(a)
print()

# print list
print("Print Command List Output")
b = [10, 20, 30]
print(b)
print()

# print tuple
print("Print Command Tuple Output")
c = (10, 20)
print(c)
print()

# type command is used to determine the type or class of an object
print("Type Command Output")
d = 2
print(type(d))
print()

# range command is used to generate a sequence of integers. Syntax: range(start, stop, step)
print("Range Command Output")
print(list(range(10)))
print()

# round command is used to round a floating-point number to a specified precision in decimal digits. Syntax: round(number, digits)
print("Round Command Output")
print(round(3.14159, 2))
print()

# input command is used to receive input from the user. Syntax: input(message)
# This command stops the program until user provides input.  (Uncomment to run)
"""name = input("Enter your name: ")
print(name)"""

# len command or len() function is used to find the length of an object. Syntax: len(object)
print("Len Command Output")
e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(e))
print()

# if-else command is used to implement conditional logic
"""
Syntax:
if condition:
  Code to be executed if the condition is True
else:
  Code to be executed if the condition is False  
"""
# Check if a number is even or odd and print result
print("If-Else Command Output")
f = 2
if f % 2 == 0:
  print("Given value is even!")
else:
  print("Given value is odd!")
print()

# elif command extends conditional logic by allowing the program to check multiple conditions sequentially
"""
Syntax:
if condition_1:
  Code to execute if condition_1 is True
elif condition_2:
  Code to execute if condition_2 is True
else:
  Code to execute if neither condition_1 nor condition_2 is True
"""
# Grading system to assign grades based on student's score
print("ELIF Command Output")
score = 88
# Uncomment line below to manually input a score
#score = int(input("Enter the student's score: "))
if score >= 100:
  grade = "A+"
elif score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
print(f"The student's grade is: {grade}")
print()

# Lists are ordered collections of items that can be indexed.  First element index begins at 0.
print("List & Index Output")
my_list = ["Debian", "Kali", "Arch", "CentOS"]
print(my_list)
print(my_list[3])
print(f"My favorite OS is {my_list[1]} Linux!")
print()

# Strings can be manipulated using concatenation, slicing, and formatting
print("Strings Concatenated Using the + Operator")
str_1 = "Hello"
str_2 = " World!" #Make sure to add extra blank space if you are concatenating strings
print(str_1 + str_2)
print()

# Python string methods:

# capitalize() converts the first character to uppercase
print("capitalize() Output")
names = ["robert", "jesica", "isabella", "jason"]
names_1 = ["ROBERT", "JESICA", "ISABELLA", "JASON"]
print(names[1].capitalize())
print()

# casefold() converts string into lowercase
print("casefold() Output")
print(names_1[0].casefold())
print()

# center() returns a centered string
print("center() Output")
txt = "Linux"
x = txt.center(20, " ")
print(x)
print()

# count() returns the number of times a specified value occurs in a string
print("count() Output")
txt = "Truly I tell you, if anyone says to this mountain, 'Go, throw yourself into the sea,' and does not doubt in their heart but believes that what they say will happen, it will be done for them. Therefore I tell you, whatever you ask for in prayer, believe that you have received it, and it will be yours."
txt_1 = "Mark 11:23–26"
x = txt.count("I") # Case sensitive
print(x)
print()

# encode() returns an encoded version of the string
print("encode() Output")
txt = "My name is Robert"
x = txt.encode()
print(x)
print()

# endswith() returns true if the string ends with the specified value
print("endswith() Output")
txt = "Python is fun."
x = txt.endswith(".")
print(x)
print()

# expandtabs() sets the tab size of the string
print("expandtabs() Output")
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
print()

# find() searches the string for a specified value and returns the position found
print("find() Output")
txt = "Welcome to learning string methods."
x = txt.find("learning")
print(x)
print()

# format() formats specified values in a string
print("format() Output")
txt = "For only ${price:.2f} dollars!"
print(txt.format(price = 99))
print()

# format_map() formats specified values in a string
print("format_map() Output")
a = { 'x': 'Robert', 'y' : "King" }
print("{x}'s last name is {y}".format_map(a))
print()

# index() searches the string for a specified value and returns the position found
print("index() Output")
txt = "We are learning about string methods!"
x = txt.index("about")
print(x)
print()

# isalnum() returns true if all characters in a string are alphanumeric
print("isalnum() Output")
txt = "123Street" # Any whitespace will make this False
x = txt.isalnum()
print(x)
print()

# isalpha() returns true if all characters in a string are in the alphabet
print("isalpha() Output")
txt = "Robert"
x = txt.isalpha()
print(x)
print()

# isascii() returns true if all characters in a string are ascii characters
print("isascii() Output")
txt = "Robert48"
x= txt.isascii()
print(x)
print()

# isdecimal() returns true if all characters in a string are decimals
print("isdecimal() Output")
txt = "1234"
x = txt.isdecimal()
print(x)
print()

# isdigit() returns true if all characters in a string are digits
print("isdigit Output")
txt = "1234567890"
x = txt.isdigit()
print(x)
print()

# isidentifier() returns true if the string is an identifier
print("isidentifier() Output")
txt = "Robert"
x = txt.isidentifier()
print(x)
print()

# islower() returns true if all characters in the string are lower case
print("islower() Output")
txt = "this is all lower case"
x = txt.islower()
print(x)
print()

# isnumeric() returns true if all characters in the string are numeric
print("isnumeric() Output")
txt = "1234567890"
x = txt.isnumeric()
print(x)
print()

# isprintable() returns true if all characters in the string are printable
print("isprintable() Output")
txt = "Is this printable?"
x = txt.isprintable()
print(x)
print()

# isspace() returns true if all characters in the string are whitespaces
print("isspace() Output")
txt = "  "
x = txt.isspace()
print(x)
print()

# istitle() returns true if the string follows the rules of a title
print("istitle() Output")
txt = "The Two Towers"
x = txt.istitle()
print(x)
print()

# isupper() returns true if all characters in the string are upper case
print("isupper() Output")
txt = "PYTHON IS GREAT"
x = txt.isupper()
print(x)
print()

# join() converts the elements of an iterable into a string
print("join() Output")
tuple_1 = ("Robert", "Jesica", "Isabella", "Jason")
x = "#".join(tuple_1)
y = " # ".join(tuple_1)
print(x + ' uses join("#")')
print(y + ' uses join(" # ")')
print()

# ljust() returns a left justified version of the string
print("ljust() Output")
txt = "Python"
x = txt.ljust(10)
print(x, "is the greatest programming language!")
print()

# lower() converts a string into lower case
print("lower() Output")
txt = "ThIs IS A MeSsED Up STriNG"
x = txt.lower()
print(x)
print()

# lstrip() returns a left trim version of the string
print("lstrip() Output")
txt = "     Three Tabs Before & After     "
x = txt.lstrip()
print(x)
print()

# maketrans() returns a translation table to be used in translations
print("maketrans() Output")
txt = "Hello Rob"
table = str.maketrans("R", "B")
print(txt.translate(table))
print()

# partition() returns a tuple where the string is parted into three parts
print("partition() Output")
txt = "I love programming in Python!"
x = txt.partition("programming")
print(x)
print()

# replace() returns a string where a specified value is replaced with a specified value
print("replace() Output")
txt = "I love programming in JavaScript!"
x = txt.replace("JavaScript", "Python")
print(x)
print()

# rfind() searches the string for a specified value and returns the last position it was found
print("rfind() Output")
txt = "Programming in Python is fun."
x = txt.rfind("Python")
print(x)
print()

# rindex() searches the string for a specified value and returns the last position it was found
print("rindex() Output")
txt = "Programming in Python is fun."
x = txt.rindex("Python")
print(x)
print()

# rjust() returns a right justified version of the string
print("rjust() Output")
txt = "Python"
x = txt.rjust(10)
print(x, "is fun.")
print()

# rpartition() returns a tuple where the string is parted into three parts
print("rpartition() Output")
txt = "Programming in Python is fun!"
x = txt.rpartition("in")
print(x)
print()

# rsplit() splits the string at the specified separator, and returns a list 
print("rsplit() Output")
txt = "Python, Java, JavaScript"
x = txt.rsplit(", ")
print(x)
print()

# rstrip() returns a right trim version of the string
print("rstrip() Output")
txt = "     Python      "
x = txt.rstrip()
print("It's fun to program in", x,"!" )
print()

# split() splits the string at the specified separator, and returns a list
print("split() Output")
txt = 'Python is the "most powerful language you can still read".'
txt_1 = "Paul Dubois"
x = txt.split()
print(x)
print(txt_1)
print()

# splitlines() splits the string at line breaks and returns a list
print("splitlines() Output")
txt = 'Python is the \n"most powerful language you can still read".'
txt_1 = "Paul Dubois"
x = txt.splitlines()
print(x)
print(txt_1)
print()

# startswith() returns true if the string starts with the specified value
print("startswith() Output")
txt = "Hello World!"
x = txt.startswith("Hello")
print(x)
print()

# strip() returns a trimmed version of the string
print("strip() Output")
txt = "     This string had three tabs before and after.      "
x = txt.strip()
print(x)
print()

# swapcase() swaps cases, lower case becomes upper and vice versa
print("swapcase() Output")
txt = "Hello, I am Robert"
x = txt.swapcase()
print(x)
print()

# title() converts the first character of each word to upper case
print("title() Output")
txt = "the two towers"
x = txt.title()
print(x)
print()

# translate() returns a translated string
print("translate() Output")
dict_1 = { 82: 66 } #ASCII Codes( 82 = R, 66 = B)
txt = "Hello Rob"
print(txt.translate(dict_1))
print()

# upper() converts a string to upper case
print("upper() Output")
txt = "why is it so loud!"
x = txt.upper()
print(x)
print()

# zfill() fill the string with a specified number of 0 values at the beginning
print("zfill() Output")
txt = "Python"
x = txt.zfill(20)
print(x)
print()