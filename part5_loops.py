cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")
#-------------------
n = 4
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

for letter in 'geeksforgeeks':
    pass # empty control statement
print('Last Letter :', letter)

fruits = ["apple", "orange", "kiwi"]

#-----------------------
for fruit in fruits:
    print(fruit)

fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break