__author__ = "Narendra Boyina"

"""
In general, statements are executed sequentially.
There may be a situation when you need to execute a block of code several number of times.

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
I would like to explain "for loop" in different way
    ==> for loop with range concept
    ==> for loop with "Strings" concept
    ==> for loop with [List] concept
    ==> for loop with (Tuple) concept
    ==> for loop with {dictionary} concept
    ==> for loop with {set} concept
    ==> for loop with enumerate concept
    ==> for loop with while loop
    ==> for loop with if condition
    ==> while loop &  while with break and continue
range is a type of sequence used to representing arithmetic progression integers
range is a constructor returns a list.
range(5)==> range(0,5)==> [0, 1, 2, 3, 4]
syntax: range(start, stop, step value)
==> Prefer enumerate() for counters
==> enumerate() yields(index,value)tuples

"""
"""

"""
# c = 0  # initialization
# while c < 19:  # test condition
#     print(c)
#     c = c+1
# print("john")


# for x in range(0,25): # where x is iteration
#     print(x)
# print("winner")


# q = []
# for f in range(0,11):
#     q.append(f)
# print(q)

# q = []
# for f in range(5,11):
#     q.append(f)
# print(q)

# q = []
# for f in range(0,190,19):
#     q.append(f)
# print(q)  ######[0, 19, 38, 57, 76, 95, 114, 133, 152, 171]


#######$$$$$$$$$$$  PRACTICE QUESTIONS $$$$$$$$$$#########
"""Required Output :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
# z = []
# for v in range(1,11):
#     z.append(v)
# print(z) ###[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Required Output :  [1, 3, 5, 7, 9]"""

# l = []
# for k in range(1,10,2):
#     l.append(k)
#     print(l)
#
"""Required Output :  [0, 10,20,30,40,50,60,70,80,90]"""
# u = []
# for p in range(0,100,10):
#     u.append(p)
#     print(u)

""" Required Output : Reverse the given list
                      OR [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]"""
# t =[]
# for j in range(10,0,-1):
#     t.append(j)
# print(t)
#

""" Required Output : Reverse the given list
                      OR[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
 """

# u = []
# for p in range(100, 0, -10):
#     u.append(p)
#     print(u)


""" Required Output : Reverse the given list[14,12,9, 7, 5, 3, 1]"""
# o =[]
# for a in range(14,0,-2):
#     o.append(a)
# print(o)

#####################$$$$$$$$$$$$$####################
a = []
for i in range(0, 20, 2):
     a.append(i)
print(a)

# n =[]
# for e in range(50,0,-5):
#     n.append(e)
# print(n)  ##[50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
#

##################################################################################################
##### user friendly program  #######
# i = int(input("starting address: "))
# j = int(input("ending address: "))
# k = int(input("step address: "))
#
# m = []
# for s in range(i,j,k):
#     m.append(s)
# print(m)

# output = []
# starting_address = int(input("starting address"))
# ending_address = int(input("ending address"))
# for number in range(starting_address, ending_address):
#     if number%7 == 0 or number%5 == 0:
#         output.append(number)
#
# print(output)


# output =[]
# starting_address = int(input("starting address: "))
# ending_address = int(input("ending address"))
# for number in range(starting_address, ending_address):
#     if number%10==0 and number%15 ==0:
#         output.append(number)
# print(output)
#

