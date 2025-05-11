print("Hello, world")
print("hello", "world")

# single line comment


"""
Multi line comment
"""

# All statements same level of indentation are considered part of same block.

# condition
if 10 > 5:
    print("tab indentation")
print("no identation")

# Input, Output 
name = input("Enter name")
print("Hello", name)

# taking multiple inputs
name, gender, age = input("Enter name, gender, age").split()
age = int(age)

# conditional checks
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# find data types
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a)) # <class, str>
print(type(b)) # <class, int>
print(type(c)) # <class, float>
print(type(d)) # <class, tuple>
print(type(e)) # <class, list>
print(type(f)) # <class, dict>

# output formatting

amount = 150.75
print("Amount: ${:.2f}".format(amount))
# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")


# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
"""
%d – integer
%f –  float
%s –  string
%x – hexadecimal
%o –  octal

"""
print("The age is %d" %age)

# assignments
a = b = c = 100
x, y, z = 1, 2.5, "Python"
print(x, y, z)
print(a, b, c) 

# typecasting: int(), float(), str()

# scope: Local, Global
a = "global"
def f():
    global a # to use global a
    a ="local"
    print(a) # prints global
print(a) # prints global

"""
Python variables hold references to objects, not the actual objects themselves.
Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.
SHARED REFERENCING
"""
x = 5
y = x # y references object holding 5 in memory
x = "Geek" # x references object holding "Geek" in memory.
print(x,y) # Geek 5

del x # deletes x, Geek garbage collected.

# SWAP 2 variables
a, b = b, a

# count string length
slen = len(a)


