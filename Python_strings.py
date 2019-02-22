# Accessing values in strings
var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])


#Concatenation
a = "guru"
b = 99
print(a+str(b))
print(a*2)

# [] - Gives letter from index
f = "Helloworld"
print(f[2])

# [:] - Gives the characters from the given range
f = "Helloworld"
print(f[2:5])

# in - Membership-returns true if a letter exist in the given string
f = "Helloworld"
print("o" in f)

# not in - Membership-returns true if a letter exist is not in the given string
x = "helloworld"
print("z" not in x)

# %r - It insert the canonical string representation of the object (i.e., repr(o)) %s- It insert the presentation string representation of the object (i.e., str(o)) %d- it will format a number for display
name = 'guru'
number = 99
print('%s %d' % (name,number))

# + - It concatenates 2 strings
x="Guru"
y="99"
print(x+y)

# * - Repeat
x = "Guru"
y = "99"
print(x * 2)


# re-assigning a variable to another string
x = "Hello World!"
#print(x[:6])
print(x[0:6] + "Guru99")

#String replace()
oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)

# to upper case
string="python at guru99"
print(string.upper())

# to lower case
string="python at guru99"
print(string.lower())

# to capitalize
string="python at guru99"
print(string.capitalize())

#join function
print(":".join("Python"))

#Reverse string
string="12345"
print(' '.join(reversed(string)))

#Split strings
word="guru99 career guru99"
print(word.split(' '))

#Split with r
word="guru99 career guru99"
print(word.split('r'))

#Immutable
x = "Guru99"
x.replace("Guru99","Python")
print(x)
