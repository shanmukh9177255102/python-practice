s = 'Welcome to the Geeks World'
print(s[1], s[-1])

# list with mixed int and string
# List[len(List)-3] == list[-3]
b = ["Geeks", "For", "Geeks", 4, 5]
print("Accessing element from the list")
print(b[0])
print(b[2])

print("Accessing element using negative indexing")
print(b[-1])
print(b[-3])

# initiate empty tuple, they are immutable against list type
tup1 = ()
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)
tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0], tup1[-1], tup1[-3])

# there is no char type & true, false are not valid keywords ( True, False  are valid).

# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")
    
# check if item exist in set    
print("Geeks" in set1)

# initialize empty dictionary
d = {}
d = dict()
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Accessing an element using key
print(d['name'])
# Accessing a element using get
print(d.get(3))

