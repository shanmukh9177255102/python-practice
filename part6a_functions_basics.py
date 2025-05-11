# defining function
def func():
    print("Hello")

# calling function    
func()

#--anonymous function--
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

#_-------------------

def subNumbers(x, y):
    return (x-y)

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

#--------------------keyword arguments----------
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

#-----------Non-keyword args------------
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

"""
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. 
There are 2 special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)

"""

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)
  
def square(x):
    return x ** 2
  
# Calling fun and passing square function as an argument  
res = fun(square, 5)
print(res)

#----------- variable arguments  *args, **kwargs --------

def fun(*args):
    for arg in args:
        print(arg)

# Calling the function with multiple arguments
fun(1, 2, 3, 4, 5)

def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

# Calling the function with keyword arguments
fun(name="Alice", age=30, city="New York")

#----- class demo ----
class Person:
    # Constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute
    
    # Method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")

# Create an instance of the Person class
p1 = Person("Alice", 30)

# Call the greet method to display the greeting message
p1.greet()

#---return--part1
def fun():
    name = "Alice"
    age = 30
    return name, age

name, age = fun()
print(name)  
print(age)   # Output: 30

#-----return--part2
def fun1(msg):
    def fun2():
        # Using the outer function's message
        return f"Message: {msg}"
    return fun2

# Getting the inner function
fun3 = fun1("Hello, World!")

# Calling the inner function
print(fun3())

#-----local, global scopes -----
"""
We only need to use the global keyword in a function if we want to do assignments or change the global variable. 
global is not needed for printing and accessing
"""
# This function modifies the global variable 's'
def f():
    global s
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s) 

# Global Scope
s = "Python is great!" 
f()
print(s)

#---pass by value, reference----
def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst) 
print(lst) # [10,11,12,13,14,15]

#--case2--
def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)
