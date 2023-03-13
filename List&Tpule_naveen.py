__author__ = "Naveen kumar"
# ############ Accessing Nested lists #############
n = [1, "Raju", [44.5, 55, "ganesh"], "narendra"]
# print(len(n))
# print(n[2])
# print(n[0])
# print(n[-1])
# print(n[-2][1])
# print(n[-3])
# print(n[2][2][1:-3])
# print(n[1][-1])
# print(n[2][2][2])
# print(n[3][3:])


"""
In python we are having 2 copy technics.
1. deep copy 
2. shallow copy
deep copy creates separate memory location for the 2nd list so that if you change element in the 2nd list, 
then 1st list will not be changed """
l = ['n','k','s','v',['nk','sv']]
# print(l)
# print(l[:])
# m = l[ : ]  # Also known as deep copy (creates separate memory location)
# print(l,id(l))
# print(m,id(m))
# m[0] = 'i'
# print(l)
# print(m)

# #####  or #######
import copy
# l = ['a', 'b', ['ab', 'ba']]
# m = copy.deepcopy(l)
# m[1] = 'i'
# print(l)
# print(m)
# print("************")

"""Shallow copy uses same memory location for the 2nd list
so that if you change element in the 2nd list , then 1st list values also will change """
# n1 = ['n','k','s','v',['nk','sv']]
# n2 = n1
# n1[2] ='boolen'
# print(n1,id(n1))
# print(n2,id(n2))

"""
Repeat lists using the * operator
 (also known as shallow copy, does not create separate memory location,
 if one inner list change means all the other lists will be  modified)"""
# d = [5,6,7]
# print(d)
r = [[5,6,7]]
e = r*3 # Repeat inner list
print(e) # [[5, 6, 7], [5, 6, 7], [5, 6, 7]]
e[2].append(9)
print(e) # [[5, 6, 7, 9], [5, 6, 7, 9], [5, 6, 7, 9]]
e[1].remove(6)
print(e)

############### tuple ##############################
"""
"" ==> string
[] ==> list
() ==> tuple
"""
# a = 50
# a = [50]
# a = (50)
# print(a)
# b = [33,456,"ramu",44.6]
# print(b)
# y = (65) ## it will give y =65 , it will not give in tuple because tuple requires atleast 2 elements
# print(y)
# print(len(y)) ## no of elements 1

# z = 22,33,44
# print(z)

"""
Tuple is hetrogenious immutable object
Tuples are used to return multiple values from a function.

You can’t add elements to a tuple. There’s no insert(), append() or extend() method for tuples,
You can’t remove elements from a tuple. Tuples have no remove() or pop(), clear() methods,

You can find elements in a tuple since this doesn’t change the tuple.
You can also use the "in" operator to check if an element exists in the tuple.

So, if you’re defining a constant set of values and
you’re going to do with it is iterate through it, use a tuple instead of a list.
tuple will be faster than working with lists and also safer, as the tuples contain “write-protect” data.
"""

# naveen = 90
# naveen = 100
# print(naveen)
# v = 234,"raju",34.6, 45
# print(v)
"""creating homogeneous tuple"""
z = (1, 2, 3, 4, 5, 6)

"""creating heterogeneous tuple"""
u = (1, "Narendra", 44.5, [22,44,"Surendra","LakshyaSree"], (1,"N",444))

""" 
1. We can't take single element inside the tuple, if we try to take  then it will give error
2. Still if we want to take single element inside tuple we have to take like this (element, ) 
Ex: variable = (5, )

Note: when we have assign multiple values to a single object then output will store as tuple
Ex: 
x = 10,20,30
print(x)

o/p: (10, 20, 30)
"""
""" Converting a tuple into list"""

A = (1, "Narendra", 44.5, [22,44,"Surendra","LakshyaSree"])  # tuple
B = list(A)
# print(B, type(B))   # [1, 'Narendra', 44.5, [22, 44, 'Surendra', 'LakshyaSree']] <class 'list'>
# B.insert(2,"raju")
# print(B)

# print(B)
# c = tuple(B) # Converting a list into tuple
# print(c)
# print(A) # original tuple


" " " Converting a list into tuple" " "
# h = [33,456,"ramu",44.6]
# i =tuple(h)
# print(i,type(i)) # (33, 456, 'ramu', 44.6) <class 'tuple'>

###====Built-in tuple Methods (2)====================
# x = (1, "Narendra", 2, 47.2, 2, "c", [22,44,"Surendra",2,"LakshyaSree"], 2)
# print(x.count(2))
# print(x.index("c"))

"""tuple indexing and tuple accessing"""
k = (1, "Narendra", 12, 47.2, "c", [22, 44, "Surendra", 2, "LakshyaSree"], 2)
# print(k[3]) #47.2
# print(k[-3]) #c
# print(k[-2])  #[22, 44, 'Surendra', 2, 'LakshyaSree']
# print(k[-2][-1])
# print(k[-2][1])
# print(k[-2][-3])

#### Range of elemnets Accessing  #######
""" extracts part of a tuple ==>slice = seq[start:stop]"""
# print(k[2:4]) #(12, 47.2)
# print(k)
# print(k[3:6]) #(47.2, 'c', [22, 44, 'Surendra', 2, 'LakshyaSree'])

"""accessing works with negative indexes
 # Required o/p is as a list, except 1st element and last element"""
# print(k[1:-1]) #('Narendra', 12, 47.2, 'c', [22, 44, 'Surendra', 2, 'LakshyaSree'])
# print(k[ :5 ])

s = [5, "Raju", [44.5, 55, "ganesh"], "arena","Naveen","praveen"]
"""Omitting the stop index slices to the end"""

# print(s[1: ])  #['Raju', [44.5, 55, 'ganesh'], 'narendra', 'Naveen', 'praveen']

"""Omitting the starting address, slices from the beginning."""
# print(s[:3])  # [5, 'Raju', [44.5, 55, 'ganesh']]
# print(s[:1])

"""Omitting the ending address, access from the respective index till end"""
# print(s[3:]) #['narendra', 'Naveen', 'praveen']


### step element accessing from a tuple
x = ('show', 'how', 'to', 'index', 'into', 'sequence')
# print(x[1:3:2])
# print(x[::-2]) #('sequence', 'index', 'how')
# print(x[::-1])  #('sequence', 'into', 'index', 'to', 'how', 'show')

# q =("Divya","Devija", "Swathi", "bhagyasree", "roopa","aparna")
# print(min(q))
# print(max(q))
# A = 65
# a = 97

#### Tuple concatination
z =("naveen","praveen","venu",4.5,"sree",6, "nk")
a = (1,2,3)
d = z + a
# print(d)
# print(z)
# print(a)
# print("rahul" in z) # Membership Output:False
# print("nk"  in z)  # Membership Output:True

""" .format()"""
"""name = input("enter name")
print("my name is {}".format(name))"""

# a =  (6,3,45,57)
# b = [33,44,55,56,5.6,7.8]
# c =("Naveen",273,4,"sree",45,6.5)
# print("Length of the tuple is {0} Length of list is  {1} 2nd tuple Length is {2}".format(len(a), len(b), len(c)))



####################################################################################
"""
The partition() method divides a string into three, around a separator: prefix,separator,suffix
partition() method returns tuple
Syntax: # String.partition("substring") ==> will return tuple
"""
# a = "cricketlover"
# b = a.partition("forget")
# print(b)
# xy = "sachin:india".partition("forget")
# print(xy)

# x = "unforgetable"
# s = x.partition("forget")
# print(s)
# print(a,type(a))
# print(b,type(b))
# print(xy,type(xy))

""" Tuple unpacking is useful to de-structure the result """
# departure, separator, arrival = "sachin:india" .partition(":")
# print(departure)
# print(separator)
# print(arrival)

# ###============ Practice & Interview Questions List&Tuple ======================

l = ["Naveen","sehwag",33,456,"ramu",44.6]
# print(l[0])
# print(len(l))
# print(l[0][2])
# print(l[1][2:5])

# "Small interview Question:

"""Question : a = [[1], [1]]
# Required Output : [[1, 1], [1, 1]]"""
a = [[1], [1]]
a[0] = [1,1]
a[1] = [1,1]
print(a)
"""Can you modify List elements which are placed in Tuple ?
a=(1,2,3,[16,17,23],45,67)"""
### Ans:Yes we can modify


# b = ('Iam', 'taking', 'guidance', 'from', 'Narendra', 'in', 'understanding', 'Python')
# print(max(b))
# print(min(b))
#Returns item from the list, with min value.

# h = (5,6,7,8,99,101,)
# y = h[0:2]+(55,)+h[3:]
# print(y)

"""a = [1, 2, 3, (16, 17, 23), 45, 67]
a[3][3]=25
print(a)  # TypeError: 'tuple' object does not support item assignment
##List elements we can modify .
# Here I have tried to modify Tuple elements which are placed in List  (It not happen)."""

d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i)