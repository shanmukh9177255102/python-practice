"""
Logical: and, not,or

"""
a = True
b = False
print(a and b)
print(a or b)
print(not a)

"""
Identity: is , is not

"""
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

"""
Membership : in, not in

"""

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Terenary operator
a, b = 10, 20
min = a if a < b else b
print(min)

