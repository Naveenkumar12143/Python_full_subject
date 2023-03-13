__author__ = "Naveen kumar"
"""
#################   Introduction of list   #####################

 Importance of list:
 ==================
Until now we have initialised the variable with single value
 a = 10

 here we can't store more than one value in a variable
 like
 a = 10
 a = 20

when you have printed value of a, 20 will be printed,
i.e we can't store more than one value in a single variable directly.

but by using List, we can assign multiple values to a single variable inside []
Ex: x = [10, 20, 18, 19, 85, 2]  ==> list index starts with "Zero" x[0] is 10

We don't have arrays, we have Python list.
lists are super dynamic, because they allow you to store more than one value in a single variable.

list is a most versatile data type available in python which can be written
 as list coma separated values B/W Square brackets

list ==> heterogeneous & mutable sequence

Different ways to create a list
Creating homogeneous list x =  [1, 2, 3, 4, 5]
Creating heterogeneous list y= ["hello", 472, 22.5, "good morning", 732, "hello", 74.5])
"""

"""split function on string returns a list"""
c = "Naveen praveen raju ravi karthik".split(" ")
# print(c) # split function on string returns a list
# print(type(c))



"""
use split() to divide a string in to multiple sub-strings and store in list data type, 
without any argument, split() divides on white spaces
inbuilt function #string.split(:)
"""
# a = " hello naveen how are you"
# b = a.split()
# print(b)
# x = "john -hello hi-where are you-from"
# y = x.split("-")  # Whenever - comes it will separate as a string
# print(y)

"""
(if we give any parameter like : * & it will split when ever * comes it will separate the string)
 2nd parameter in the split()is number of string need to be done,
 if possibility is there then only it will separate tha many strings'''
"""
# n = "Line1--Naveen----Line2--abc-Line4--abcd----kumar"
# print(n.split("----"))
# print(n.split("--", 2))  # first 2 occurrences
print(" hello naveen how are you".split(" ", 4))
#####################################################################################
"""
call the join()method on the separator string
join()-ing on an empty separator is an important & fast way of concatenating collection of strings
"""
h = ["john" ,"hello hi", "where are you from"]
o =" * ".join(h)
print(o)
# h = ["john" ,"hello hi", "where are you from"]
# o =" ### ".join(h)
# print(o)
# s = "".join(["boyina", "narendra", "surendra"])
# print(s)  # ans: "boyinanarendrasurendra"
# h = "".join(["chintha","naveen","kumar"])
# print(h)

"""
############## Elements accessing  ###################
Syntax: variable = instance[SA : EA : step]
index always starts with Zero ends with -1
"""
""" @@@@@  Single element accessing   @@@@@@
Syntax:  variable = instance[index]
"""
data = [444, 1.5, 7.5, "Naveen", 472, 'ravi', 'Suresh', 'Aruna','Sree', "Sai"]
# print(type(data))
# print(data[5])  # ravi
# print(data[-4])  # Suresh (Last element is at index -1))
# print(data[-2])
##############################

"""
@@@@@  range of elements accessing   @@@@@@
variable = instance[SA : EA]
"""
# print(data[1:8])
# print(data[3:6])
# print(data[2:-3])

"""slicing works with negative indexes
Required o/p is as a list, except 1st element and last element"""

n = ['lakshmi', 'Naveen', 'sree', 'Raju']
# print(n[1:-1])

"""Omitting the stop index slices to the end"""
# print(n[1: ])

"""Omitting the start index slices from the beginning."""
n = ['Rajyalakshmi', 'Narendra', 'Bhagyasree', 'Raj']
# print(n[ :2])

"""Omitting the start & stop indexes slices from the beginning to the end ==>a full slice
deep copy creates separate memory"""
# print(n[ : ])
# print(n)

# o = "a"
# print(ord(o))

# N = "A"
# print(ord(N))

# k = 87
# print(chr(k))

###################################################################################
"""step element accessing"""
z = ['Raghu', 'Naveen', 'Bhagyasree', 'Raj',4.5, "Naresh", "Praveen"]
# print(z[1:5:2])
# print(z[ : :3])
# print(z[ : :-1])   # Reverse the lst
# print(z[ : : -2])
# print(z[ : : -5])
# x = "madam"
# print(x == x[::-1])
# y ="suresh"
# print(y == y[::-1])


# lst1 = [5, 12, 14, 18, 19, 85, 25]
# lst2 = ["Narendra", "Surendra", "Mahalakshmi","Raj", "n"]
# lst1[5] = 999  # 85 is replaced by 999 dynamically (replace with +ve index)
# print("Modified list is : ", lst1)
# lst2[-3] = "rahul"  # replace with -ve index
# print(lst2)
# lst2[3] = 45
# print(lst2)

###====Built-in List Methods================
#  Insert items with seq.insert(index,item)"""
u = ['we', 'me', 'kamal', 'python', 'Swathi','into', 'sequence','DURGA']
# print(u, type(u))

# u.insert(5, "lucky")  # User Can insert string
# print(u)  #
# u.insert(2, 11.5)  # User Can insert float value
# print(u)

""" count no of repeated elements in a list. Syntax: seq.count(Element)"""
# # #Syntax: list.count(obj) ==>obj -- This is the object to be counted in the list.
s = ['Iam', 'taking', 'guidance', 'from', 'Naveen', 'in', 'understanding', '55','65','44.7','int']
# g = s.count("from")
# print(g)
# j = s.count("in")
# print(j)
# u = s.count("hello")  # given string is not available in the list So count is 0
# print(u)
# o = s.count("naveen")  # case sensitive so it assumes that no string, So count is 0
# print(0)

"""We can find the index for required element in the list
Syntax:list.index(obj) ==>obj -- This is the object to be find out."""

# w = ['Iam', 'taking', 'guidance', 'from', 'Naveen', 'in', 'understanding', '55','65','44.7','int']
# r = w.index("55")
# print(r)
# print(w[2:])  # omitting ending address
# print(w[6:])
# print(w[w.index("in") :])

# #====================We can reverse the list =============

"""
Note : difference b/w them
x.reverse() return None. i.e we can't store result of x.reverse()
but result of x[::-1]  can be stored in other variable.  
"""

# x = ['SaLMA', 'Anand', 'Sri', 'Srikanth', 'Giri', 'Swathi','Srinivas', 'Ashok', 'Tejaswi', 'Haritha', 'Srinivas', "jai", 'Radha', 'Lakshmi', "pankaj", "narendra"]
# x.reverse()
# print(x)
# t =x[ : : -1]
# print(t)


""" difference B/W append and extend methods"""
# a = ["Nanna"]
# print(a)
# a.append("hero")
# print(a)
# print(len(a))

# c = ["john",645,"hi",7.6,"jgjgjghg"]
# a.append(c)
# print(a)
# print(len(a))
# r = ["john",645,"hi",7.6,"jgjgjghg"]
# a.extend(r)
# print(a)


# a = ['Nanna', 'Amma', 7.5]  #list
# b = ("Hi",444,"hello","hello", 3.4)  # tuple--> Immutable object
# a.extend(b)
# print(a)
# print(b)

''''we can add 2 lists by using extend method.
the difference b/w concatination and extend is 
(if we use concatenate operator "+" we need to store the result in another variable)
but extend method will combine both lists and stored in 1st list variable '''

" concatenate lists with + operator """
# a1 = [1,3,5,7,"naveen","kumar"]
# b2 = [5,4,6,"hi","hello"]
# a1.extend(b2)
# print(a1)
# c3 = a1 + b2
# print(c3)
# print(b2)
# print(a1)

#==============================================================================

# s = ['show', 'how',2,3,4,5,'to', 'Narendra', 'into', 'sequence',"Surendra", "Narendra"]
# del s[3]
# print(s)
# del s[8]
# print(s)

# a = s.index("into")
# del s[a]
# print(s)

w = ['show', 'how',2,3,4,5,'to', 'Narendra', 'into', 'sequence',"Surendra", "Narendra"]


# del w[w.index("sequence")]
# print(w)


# s = ['show', 'how', 'to', 'Narendra', 12,'into', 'sequence', "Narendra"]
# s.remove("into")

# c = [1,3,5,7,"naveen","kumar"]
# c.clear()
# print(c)

"""returns last element and remove it"""

# h = [1,3,5,7,"naveen","kumar"]
# i =h.pop()
# print(i)
# s = ['show', 'how', 'to', 'Narendra', 12,'into', 'sequence', "Narendra"]
# m =s.pop()  # This print statement is for display the removed element
# print(m)   # displays the list after deletion of last element

# r = ["hello",472,"good morning",732,"1111hello","shubhashini", "rindha","priyanka"].pop()
# print(r)  # displays deleted element

# h = 4.5
# print(int(h))

# y = 5
# print(float(y))

"""list() constructor"""

# s = (2, 4.5, 66)  # tuple
# k = list(s)
# print(k,(type(k)))
# k.insert(2,"Naveen")
# print(k)
# print(tuple(k))  # tuple() constructor

""" "in" and "not in "operators test for membership( in keyword, used for check availability)"""

z = ["SaLMA", 234,"Anusha", "Anand", "Sri", "Ashok", "Srikanth", 22.2, "Giri", "Swathi", [1, 78,"venu", 85.2], "Srinivas",
     "Ashok", "Tejaswi","Haritha","Radha","Lakshmi", "Durga Narendra"]
# print(len(z))
# print("Swathi" in z)
# print("Raju" in z)
# print("Raju" not in z)
# print("Swathi","Sri" in z)
# print([1, 78, "venu", 85.2] in x)
# print(78 in x)

#####################################################
#################   Practice programs ###############
#####################################################
# a = ["SaLMA",234, "Anand", "Sri", "Giri","Swathi",1,78,85.2,"Srinivas","Ashok", "Tejaswi","Haritha","Srinivas"]
# print(a)
# p = a[: :3]
# print(p)
# l = (1,2,3,4)
# print(len(l))
# print(l[0])
# q = a[1:5:]
# print(q)
# m = a[: : -2]
# print(m)
# z = a[1]
# print(z)
# z = a[3]
# print(z)
#
# del a[7]
# print(a)
#
# a.remove("Ashok")
# print("^^^^^^", a, "$$$$$")

##'''Accessing Values in Lists ,Updating Lists & Delete List Elements'''
# a="I am taking guidance from Naveen in understanding Python"
# b=a.split()
# print(b)
# print("Value available at index 2 : ",b[3]) # Accessing Values in Lists
# b[2] = "support"                            # Updating Lists
# s=" - " # s='space'
# c =s.join(s)

# v = ["Hi",444,"hello",472,"good morning",732,"hello",74.5,"hello","yugesh", 34,56.3,"n",89, "Kiran"] # l is a object for the list
# print("No of times element available in list :",l.count("yugesh"))
# print(v.count("hello"))
# p = v[3]
# print(p)
#
# n = [5,6,7,8,"djjjjjj"]
# m = ["fun","run",5,87,89]
# o =n+m
# print(o)

