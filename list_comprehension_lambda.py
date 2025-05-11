#  List comprehesion: new way of creating list  
# syntax = [expression for item in iterable if condition]
a = [2,3,4,5]
res = [val ** 2 for val in a]
res = [val for val in res if val % 2 == 0]
print(res)

# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

# Flattened arrray
matrixData = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenedArray = [val for row in mat for val in row]
print(flattenedArray)


# lambda expressions
# syntax:   lambda arguments : expression
# Using lambda
sq = lambda x: x ** 2
print(sq(3))

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0))

# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

# -----------------map,filter,reduce------------------

# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
