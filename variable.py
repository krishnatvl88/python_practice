# Declaring simple variable
a=100
print(a)

# Declare variable and initialize it
f=0
print(f)

#Redeclaring the above variable to new value
f = 'guru99'
print(f)

#concatenate variables
'''a="Guru"
b = 99
print(a+b)'''

#Declare integer as string
a="Guru"
b = 99
print(a+str(b))


# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)

someFunction()
print(f)


f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
print(f)
f = "changing global variable"
someFunction()
print(f)


#deleting the variable
f=10
print(f)

del f
print(f)
