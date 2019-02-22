#1. Print Hello World

'''
print("Hellow World")
'''

#2. Variable Usage

# Define same variable with 2 diff values, Recent one will be overridden
'''
x="david"
x=5
print(x)
'''

# Define 2 variables with string values x and y
'''
x = 'Hello '
y = 'Test '
print(x + y)
'''

#Define 2 variables with one as integer and other as string
'''
x = 5
y = "John"
print(x)
print(y)
'''

#Define 2 variables 1 as integer and other as string and add/concatenate
'''
x = 5
y = "John"
print(x + y)  #This is not allowed as we cant concatenate or add string and integer
'''

# Numbers
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
'''

# Float can also be scientific numbers with an "e" to indicate the power of 10.
'''
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
'''

# Complex numbers are written with a "j" as the imaginary part:
'''
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
'''

# Casting
# Integers
'''
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)
'''

# Floats
'''
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)
'''

# Strings
'''
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)
'''

# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.

# Get the character at position 1 (remember that the first character has the position 0):
'''
a = "Hello, World!"
print(a[1])
'''

# Substring. Get the characters from position 2 to position 5 (not included):
'''
b = "Hello, World!"
print(b[2:5])
'''

# The strip() method removes any whitespace from the beginning or the end:
'''
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
'''

# The len() method returns the length of a string:
'''
a = "Hello, World!"
print(len(a))
'''

# The lower() method returns the string in lower case:
'''
a = "Hello, World!"
print(a.lower())
'''

# The upper() method returns the string in upper case:
'''
a = "Hello, World!"
print(a.upper())
'''

#The replace() method replaces a string with another string:
'''
a = "Hello, World!"
print(a.replace("l", "J"))
'''

# The split() method splits the string into substrings if it finds instances of the separator:
'''
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
'''

# demo_string_input.py
'''
print("Enter your name:")
x = input()
print("Hello, " + x)
'''

# Python Comparison Operators

# ==

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)