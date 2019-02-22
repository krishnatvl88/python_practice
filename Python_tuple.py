#Tuple assignment
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

#tuple packing
x = ("Guru99", 20, "Education")
print(x[2])

#tuple unpacking
(company, emp, profile) = x
print(emp)

#Tupe Comparision -> Checks first element
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

#first two elements are same then go for next element check
a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

#first element is smaller and hence check second element and print
a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")