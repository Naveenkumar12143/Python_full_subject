__author__ = "Naveen kumar"
"""Comprehensions:
1. List Comprehensions
2. set Comprehensions
3. Dictionary Comprehensions


1. List Comprehensions
Syntax: Variable = [expression(element) for element in iterable [if else]]

2. set Comprehensions
Syntax: Variable = {expression(element) for element in iterable [if else]}
set function eliminates duplicate objects present if any
result set will not store in order because set is an unordered

3. Dictionary Comprehensions
Syntax:Variable =  {key_expr:value_expr for item in iterable [if else]}

In another way:
==============
A list comprehension generally consist of these parts :

Output expression,
Input sequence,
A variable representing a member of the input sequence and
An optional predicate part.
For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 0] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
"""

"""
List Comprehensions examples
Syntax: Variable = [expression(element) for element in iterable]
Example 1:
=========
"""
iterable = "my name is chintha naveen kumar iam from anantapur distric".split()
print(iterable) #['my', 'name', 'is', 'chintha', 'naveen', 'kumar', 'iam', 'from', 'anantapur', 'distric']
n = []
for name in iterable:
    v = len(name)
    n.append(v)
print(n)

print([len(element) for element in iterable])


"""Syntax: Variable = [expression(element) for element in iterable]"""

Naveen = "why sometimes I have believed others blindly it's my mistake".split()
# print([len(element) for element in Naveen])

"""below list contains square of all even numbers from 1 to 20"""

# even_square = []
# for x in range(1, 21):
#     if x % 2 == 0:
#         a = x**3
#         even_square.append(a)
# print(even_square) #[8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

print([x **2 for x in range (1,21) if x % 2==0]) #[2, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# print([naveen **2 for naveen in range (1,21) if naveen %2==1 ])

""" by using list comprehension above generation is same as"""
# Example 2:

"""Nested Conditionals
With a Python list comprehension, it doesn’t have to be a single condition; you can nest conditions. 
Here’s an example.
"""

"""print the list of numbers b/w 1 to 30, which are divisible by 2 and divisible by 2 """

u =[]
for div in range(1,31):
    if div%2==0:
        if div%2==0:
            u.append(div)

# print(u) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# print([div for div in range(1,31)if div%2==0 if div%2==0])
# output :[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

u =[]
for john in range(1,31):
    if john%2==0 and john%2==0:
        u.append(john)

# print(u) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# print([john for john in range(1,31)if john%2==0 and john%2==0])
#output  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

""" performing squares for which are divisible by 2 and divisible by 4  """
# print([element*2 for element in range(1, 41) if element%2==0 and element%4==0])

"""print the list of numbers b/w 1 to 10, which are not divisible by 2 and  not divisible by 3 """
# print({nvn for nvn in range(1,21)if nvn%2!=0 and nvn%3!=0})

######    set Comprehensions examples   ######
"""
Syntax: Variable = {expression(element) for element in iterable}
set function eliminates duplicate objects present if any
result set will not store in order because set is an unordered
"""

# data = "my name is chintha naveen kumar iam from anantapur distric".split()
# print(data)
# print({len(element) for element in data})

#######    Dictionary  Comprehensions examples   ######
"""Examples for Dictionary Comprehensions:
syntax = {key_expr:value_expr for element in iterable}"""
# list()  []
# tuple() ()
# dict()  {}
# set()

# square_dict = dict() # {} is a empty dictionary
# print(square_dict)

# mul = dict()
# for sum in range(1,20):
#     mul[sum] =sum+sum
# print(mul)

# print({sum: sum+sum for sum in range(1,21)})

''' dictionary comprehension'''

add = [5,4,3,2,1]
# print({c:c+c for c in add}) #{5: 10, 4: 8, 3: 6, 2: 4, 1: 2}

sub =(1,5,6,8,9)
# print({n: n-n for n in sub}) #{1: 0, 5: 0, 6: 0, 8: 0, 9: 0}

mul = (2,4,5,7)
# print({mul: mul*mul for mul in mul}) #{2: 4, 4: 16, 5: 25, 7: 49}

power = (1,2,4,3)
# print({power: power**power for power in power})#{1: 1, 2: 4, 4: 256, 3: 27}

square = (2,4,5,6,8,9)
# print({s: s**2 for s in square})

"""
Delete recuring in string
Given a string as your input, delete any reoccurring character, and return the new string.
"""

name = "chintha naveen kumar"
r = []
for y, char in enumerate(name):
    if char not in name[:y]:
        r.append(char)

# print(r) #['c', 'h', 'i', 'n', 't', 'a', ' ', 'v', 'e', 'k', 'u', 'm', 'r']
# print(''.join(r)) #chinta vekumr

# print([char for y,char in enumerate(name) if char not in name[:y]])
# print(" ".join(r)) #c h i n t a   v e k u m r

"""
Usage of help() and dir() function in Python?
Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 

Help() function: The help() function is used to display the documentation 
===============  string and also facilitates you to see the help related to modules, keywords, attributes, etc.
Dir() function: The dir() function is used to display the defined variables/methods/inbuilt functions.
===============
"""
# print(help(input))
# print(help(sum))
# print(help(enumerate))
# x = input(" enter first Name")
# print(x)

################################################################
#################   Practice programs ###############
###################################################################

# a = [(i*2) for i in range(11)]
# print(a)

# square = {(n**2) for n in range(10)}
# print(square)

# A = [3,2,5]
# A = [[i,i**i] for i in A]  # list comprehension
# print("A value is : ", A)

# f = [len(str((factorial(x)))) for x in range(20)]
# print(f)
# print(type(f))



# print({i:i*i for i in range(5)})   #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print({i:i**i for i in range(5)})  #{0: 1, 1: 1, 2: 4, 3: 27, 4: 256}
# print({i:i+i for i in range(5)})  #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


# A5 = {i:i**i for i in A1}  # dictionary comprehension
# print("A5 value is : ", A)

# names_1 = ["Narendra", "Bhagyasree", "Raj", "Mahalakshmi"]
# names_2 = [name.lower() for name in names_1]
# print(names_2[2][0])

# print([i+j for i in "abc" for j in "def"])
d = {x.upper(): x*3 for x in 'acbd'}
print(d)