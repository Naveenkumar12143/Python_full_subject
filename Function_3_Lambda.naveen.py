__author__ = "Naveen kumar"

"""
lambda function: It   

1)These functions are called anonymous because they are not declared in the standard manner 
by using the "def" keyword.
2)You can use the "lambda" keyword to create small anonymous functions.
3)Lambda forms can take any number of arguments but return just one value in the form of an expression. 
They cannot contain commands or multiple expressions.
Function definition is here

variable = lambda arguments: operation
Syntax:  variable = lambda arg1 [arg2,arg3,.....argn]:expression
Note: variable works as a function name

 interview purpose: 
 lambda function is a single line anonymous function, it can take any no of inputs but 
 it can able to return only one value.
"""

i = 5
j = 10
k = 2


def raju(i,j,k):
    v = i + j
    u = v * k
    w = u/2
    nvn = u - v
    return v,u,w,nvn

# calling function
# v,u,w,nvn =raju(i,j,k)
# print(v,u,w,nvn)

# nv,pv,rk,ms = raju(5,4,3,)
# print(nv,pv,rk,ms)

# y = lambda i,j,k:((i+j)*k)/3
# print(y(2, 4, 3))


# move = lambda arg1,arg2: arg1 + arg2
# print(move) # it will give the memory location because you have not a passed any inputs


# calling function
# print("value of total:",move(55,35)) #valueof total: 90
# print("value of total:",move(500,400))


catch = lambda n: n+n
# catch = lambda n:n**n
# print(catch)  # it will give the memory location because you have not a passed any inputs


# calling function
# print(catch(2))
# print(catch(4))
# print(catch(6))
# print(catch(7))

# 2. Map Function
# =============

"""
map() :
map() will apply the same function to every element of iterable/sequence and 
return a list of the results.


Syntax :
map(function_name, iterable, ...)
"""
g = []
for i in range(1,5):
    s = i**i
    g.append(s)

# print(g) #[1, 4, 27, 256]

# Ex : Create a list of squares for the first 5 numbers
def print_add(z):
    c = z ** z
    return c

# calling function
# catch = list(map(catch, [1, 2, 3, 4, 5]))
# print(catch)


# calling function
# add = list(map(lambda z: z**z, [2, 4, 3, 5]))
# print(add)

# Note:- Need not necessarily use a lambda function print(list(map(square, iterable)))
# Filter Function:
# ================

""""
3. filter() :
The function filter(function_name, iterable) offers way,  to filter out all the elements of a list, 
for which the function returns True. 
(or)
Filter items out of a sequence, returns filtered list
"""

def is_odd(z):
    if z + 2 == 0:
        return z


# z = filter(is_odd,range(10,55))
# z = list(filter(is_odd,range(10,55)))
# print(z)

# or

# print(list(filter(lambda z: z % 2 == 0, range(10, 26))))  # [10, 12, 14, 16, 18, 20, 22, 24]
# print(list(filter(lambda z: z % 2 == 1, range(10, 55))))


"""zip() function: 
it will take multiple lists say list1, list2, etc and transform them into a single list of
 tuples by taking the corresponding elements of the lists that are passed as parameters.

zip always creates the tuple in the order of iterables from left to right.
execute the below code in 2.7.x version it will give list of tuples.
 """

x = [2,5,9,4]
y = ['s','j','k','l','o']


# zipped_list = zip(x, y)   # execute only in python 2.7.x version
# print(zipped_list)   #<zip object at 0x00000245B3A14080>
# print(list(zipped_list)) #[(2, 's'), (5, 'j'), (9, 'k'), (4, 'l')]

# or

# v = list()
# print(v)
# print(list(zip(x,y)))

# In Python3, zip methods returns a zip object instead of a list. This zip object is an iterator

# hi = [ 5,10,15,20,50]
# chai = ['a', 'b', 'c', 'd', 'e']


# zipped_list = zip(hi,chai)
# p = list(zipped_list)
# print(p) #[(5, 'a'), (10, 'b'), (15, 'c'), (20, 'd'), (50, 'e')]


# # zip with more than 2 lists

list1 = ['A', 'B', 'C','n',]
list2 = [10, 20, 30, 40]
list3 = ["Naveen", "Surendra", "sree","praveen"]

# x = list(zip(list1, list2,list3))
# print(x) #[('A', 10, 'Naveen'), ('B', 20, 'Surendra'), ('C', 30, 'sree')]
# print(dict(x))  # error


"""whenever the given lists are of different lengths, zip stops generating tuples when the first list ends"""
h = dict(zip(('a','b','c','d','e','f'),(1,2,3,4,5)))

print(h)


"""
Unzip a list of tuples
To unzip a list of tuples we zip(*listP_of_tuples). Unzip creates separate list."""

x = [1, 2, 3]
y = [1.1, 2.2,3.3]

# print(list(zip(x,y))) #[(1, 1.1), (2, 2.2), (3, 3.3)]

x = (1,2,4)
y = (1.1, 2.2,5.9)

# print(list(zip(x,y))) #[(1, 1.1), (2, 2.2), (4, 5.9)]

zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]

t,f = zip(*zipper_list)
# print(t)  # (1, 2, 3)
# print(f)  #('a', 'b', 'c')

# reverse apply of unzip
# print(list(zip(t,f)))  # [(1, 'a'), (2, 'b'), (3, 'c')]


# For loop on zip concept
# Python program that uses zip on list

items1 = ["blue", "red", "green", "white"]
items2 = ["sky", "sunset", "lawn", "pillow"]

# print(list(zip(items1, items2)))
# Zip the two lists and access pairs together.
# for x, y in zip(items1, items2):
#    print(x, "====>",y)



# enumerate concept with zip
# Here is how to iterate over two lists and their indices using enumerate together with zip:

alist = ['a1', 'a2', 'a3']
blist = ['5', '10', '15']

# for i, (a, b) in enumerate(zip(alist, blist)):
#     print(i+1, a, b)
