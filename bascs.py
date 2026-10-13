#Integer
price = 200;
ratio = 12.3;

x= 2
y = 4
z =8
print(x, y, z);

print(price);
print(ratio);

#Strings
greetings = "Hey, How are you doing today?";
statement = 'Am learning ';
statement2 = 'python';

print(greetings);
print(statement + statement2);

# Declaration Variables
myNumber = 9;
first_name = "Ouma"

#combination of string and Integer
age =20;
name = "Ouma Isaac";
learning = "Learning Data Analysis";

# print("My name is "+ name + age +"years old" + learning);

#  Arithmetic Operations 
"""
a) addition
b) subtraction
c) multiplication
d) division
e) modulus
f) exponentiation
"""

point =23;
point2 = 98;

myF = point + point2;
mathF = point * point2;
subF = point - point2;
divF = point / point2;
modF = point % point2;
expF = point ** point2;
print(myF);
print(mathF);
print(subF);
print(divF);
print(modF);
print(expF);

#Comparison Operations
"""
a) greater than
b) less than
c) greater than or equal to
d) less than or equal to
e) equal to
f) not equal to
"""
myGreater = point > point2;
myLess = point < point2;
myGreaterEqual = point >= point2;
myLessEqual = point <= point2;
myEqual = point == point2;
myNotEqual = point != point2;

print(myGreater);
print(myLess);
print(myGreaterEqual);
print(myLessEqual);
print(myEqual);
print(myNotEqual);

#Boolean Operations
"""
a) and
b) or
c) not
"""

bool1 = True;
bool2 = False;

print(bool1 and bool2);
print(bool1 or bool2);
print(not bool1);

#Assignment Operations
"""
a) addition assignment
b) subtraction assignment
c) multiplication assignment
d) division assignment
e) modulus assignment
f) exponentiation assignment
g) floor division assignment
h) bitwise AND assignment
i) bitwise OR assignment

"""
height = 99
length = 12

height += length
myAdd = height

height = 99
height -= length
mySub = height

height = 99
height *= length
myMul = height

height = 99
height /= length
myDiv = height

height = 99
height %= length
myMod = height

height = 99
height **= length
myExp = height

height = 99
height //= length
myFloorDiv = height

height = 99
height &= length
myBitwiseAnd = height

height = 99
height |= length
myBitwiseOr = height

print(myAdd, mySub, myMul, myDiv, myMod, myExp, myFloorDiv, myBitwiseAnd, myBitwiseOr)


# Exercise 2
# Do arithmetic, Assignment, Comparison and Boolean operations on the following values (100, 67, 47) and print the results


#Logical Operations
"""
a) and
b) or
c) not
"""
x = 12
y= 5
print(x > 10 and y < 10)
print(x > 10 or y < 10)
print(not (x > 10))

#List
x = [1, 2, 3, 4, 5]
print(x)

"""
x.append(6)
x.extend([7, 8, 9])
x.index(3)
x.insert(2, 10)
x.sort()
x.remove(2)
print(x)
"""
"""
y=["apple", "banana", "cherry"]
print(y)

y.append("orange")
y.extend(["kiwi", "mango", "grapes"])
y.index("banana")
y.insert("Watermelon")
y.remove("banana")
y.sort()
print(y)
"""
#List
x = [10, 2, 13, 4, 5]
"""

x = x.append(6)
x = x.extend([7, 8, 9])
x.index(3)

#x = x.index(3)
#x = x.insert(6, 7)
# x.remove(2)
# x.insert(2, 5)
# x.sort()

x.remove(13)
x.clear()
x.copy(9)
x = x.count(2)
x.reverse()
x  = x.pop(3)
print(x)

x.append()
x.extend([7, 8, 9])
x.index(3)
x.insert(2, 10)
x.sort()
x.remove(2)
x.clear()
x.copy()
x.count()
x.pop()
x.reverse()

"""

y=["apple", "banana", "cherry"]
y.append("pineapple");
print(y);

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


#conditions
"""
a = 9
b = 9

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equals to b")
else:
    print("a is less than b

"""



























































































































































