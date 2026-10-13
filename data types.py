#Data types
"""
tuples
sets
Dictionaries
"""
x = (10, 20, 30, 40, 500)
print(type(x))
print(x)

y = {12, 2, 67, 89, 20}
print(type(y))
print(y)

z = {"name": "John", "age": 30, "city": "New York"}
print(type(z))
print(z["city"])

myTuple = ("apple", "banana", "cherry")
myTuple1 = ("orange",)
myTuple += myTuple1
print(type(myTuple))
print(myTuple)

#sets
mySet = {1, 2, 3, 4, 5}
myset1 = {6, 7, 8, 9, 10}
mySet.update(myset1)
print(type(mySet))
print(mySet)

my_set = {"john", "peter", "maria"}
mySet1 ={"abdi",}
mySet.update(mySet)
print(type(my_set))
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {"Isaac", "Benja", "Raul"}
set3 = {12, "Brilliant"}

set4 = set1.union(set2, set3)
#set4 = set1 | set2 | set3
print(set4)

tuple0 = (100, 200, 300, 400, 500)
list0 = {3, 4, 7}
k = list0.union(tuple0)
print(k)

my_set0 = {"a", "b", "c", 1, 2, 3, 4}
my_tuple0 = (1, 2, 3, 5)
p = my_set0.difference(my_tuple0)
print(p)


my_dict = {"Name":"Benard", "age":20, "Leaning":"Python"}
my_dict1 = {"city": "Bondo", "Residence": "Milai"}
my_dict.update(my_dict1)
print(my_dict)


