#Do an exercise that comprise of tuples, sets and dictionaries and print the results
#Use your creativity to do the exercise


x =(35,55, 65, 75, 85)
print(type(x))
print(x)

w={39, 46,82,12}
print(type(w))
print(w)

k={"name":"khalif", "address":"Garissa", "status":"single"} 
print(type(k))
print(k["status"])


h={"work": "online business", "location": "islii",}
print(type(h))
print(h["location"])


#Functions in tuples
"""
Adding two tuples
Removing an item from a tuple
"""
isTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9);
isTuple1 = (11, 12, 13, 14, 15);
#isTuple2 = isTuple + isTuple1;
isTuple += isTuple1;
print(isTuple);

my_tuple = (10, 30, 50)
my_tuple1 = list(my_tuple)
my_tuple1.append(60,)
my_tuple = tuple(my_tuple1)
print(my_tuple)


myTuple =(20, 30 , 68, 80, 98);
myTuple2 =list(myTuple);
myTuple2.remove(68);
myTuple = tuple(myTuple2);
print(myTuple);


isTuple1 = (11, 12, 13, 14, 15);
isTuple2 = (16, 17, 18, 19, 20);
isTuple1 += isTuple2;
print(isTuple1);








