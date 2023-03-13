__author__ = "Naveen kumar"

# n = [5,66,46,3.8,"Naveen"]
# print(len(n))
# n = (5,66,46,3.8,"Naveen")
# print((n))

"""
Topic: Dictionaries & Nested Dictionaries

Dictionary is a key value pair  {Narendra: 31, qualification: "M.tech"}
  (or)
Dictionary is an unordered, mapping from
unique immutable key to mutable/Immutable values.

unique(No duplicate key is allowed)
x =10
x =20
print(x)
"""

# ###########========================================================
"""practice string questions"""
# print("hello"+'3.5')
# print('1'+'4.5')
# print(r"\nhello")
# print("\t\tworld\n\nation")
# print("hello\example\test.txt")
# print("hello\example\test.txt")

# print("D", end = ' ')
# print("C", end = ' ')
# print("B", end = ' ')
# print("A", end = ' ')

# print(format("Welcome", "10s"), end = '#')
# print(format(111, "4d"), end='#')
# print(format(924.656, "3.2f"))


'''No duplicate key is allowed in dictionaries.
When duplicate keys encountered during assignment, the last assignment wins'''

# p = {'Name': 'NARENDRA', 'Age': 61, 'Role': 'farmer', 'Name': 'Udaya Bhaskara rao '}
# print(len(p))  # gives 3 (items) only because dictionary will not allow duplicate keys
# print(p)

# list()
# tuple()
# dict() # input is list(tuples) or tuple(tuples)
# """ list of tuples can be converted as dictionary using 'dict()' function """
c = [("Naveen",1999),("Raghu",1888),("pawan",1555)]
# b = dict(c)
# print(b) ##{'Naveen': 1999, 'Raghu': 1888, 'pawan': 1555}

# l = ['NARENDRA', 'SURENDRA', 'nk', 'Sravya',"Chandra", "Sai"]
# m = [27, 28, 24, 44, 25, 7]
# n =zip(l,m)
# print(n)  # it provides the zip object/<zip object at 0x00000231CCEF81C0>
# k1 =list(zip(l,m))
# print(k1) # it provides list of tuples
# k2 = tuple(zip(l,m))
# print(k2)
# print(dict(zip(l,m))) # simple way

z = {'Name': 'NARENDRA', 'Age': 29, 'Status': 'Married'}
# print(z['Name'])
# print(z['Age'])
# z["Status"] ='lucky'
# print(z)

# ########   Updating Dictionary  ########
# g ={'Hi': "how r u", "Hello": "nice to meet you", "Ok": "bye"}
# g["cricket"] = "game" # adding new elements in dictionary
# print(g)
# g["cricket"] = "passion"  # updating the value
# print(g)

d = {"name": ["Narendra", "Salma", "Babji", 1.5], "Age": (27, 28, 25), 1995:["Naveen" , "Babjan"], "srinivas": [3, 44, 2],
     "priyanka": {'Name': 'NARENDRA', 'Age': 26, 'Status': 'Married'}}
# print(type(d) ,len(d))
# print(d["name"])
# print(d["name"][2][3])

# print(d["Age"][2])
# print(d[1995][1])
# print(d["priyanka"])
# print(d["priyanka"]["Age"])
# print(d["priyanka"]["Name"])
# print(d["priyanka"]["Name"],["Age"],["status"])


############### Delete Dictionary Elements############

'''You can either remove individual dictionary elements or clear the entire contents of a dictionary.
You can also delete entire dictionary in a single operation.'''

# i ={'Hi': "how r u", "Hello": "nice to meet you", "Ok": "bye"}
# del i['Ok']
# print(i)
# del i['Hello']
# print(i)
# i.clear()  ## remove all entries in dict
# print(i)

##############   Built-in Dictionary Functions & Methods  #############

"""
 d.copy() for copying dictionaries
    c = b.copy()  # {'Akshat': 1979, 'ravi': 1268, 'NARENDRA': 2162}
    "dict" constructor can also be used to copy dictionaries
    d = dict(c)  # {'ravi': 1268, 'Akshat': 1979, 'NARENDRA': 2162}

 object.copy() for copying dictionaries
"""

n = {"Babji": 1985, "Babjan": 1995, "Jai": 1989, 'Sri krishna': 1994, 'NARENDRA': 1990, "Naveen": 1995,"Salma": 1994,
     "Kiran": 1993, "Srinath": 1991, "Srinivas": 1993}

     ########## deep copy#############
# print(n)
# v = n
# print(v)
# print(id(n),id(v))  # deep copy

"""  "dict" constructor can also be used to copy dictionaries """

# w =dict(n)
# print(w)
# print(id(n),id(w))

############# shallow copy ##########

# o = n
# print(o)
# print(id(n),id(o))

#############   adding 2 dictionaries   ############
"""
Extend dictionary with "update"
    x = {"abc": 123, "def": 456}
    d.update(x)
    print(d)
Note: we can't concatenate 2 dictionaries like list/tuple/strings by using + operator
"""
# d = {'Sri krishna': 1994, 'NARENDRA': 1990, "Salma": 1994, "Kiran": 1993, "Sai": 1991, "Srinivas": 1993}
# f = {'Hi': "how r u", "Hello": "nice to meet you", "Ok": "bye"}
# d.update(d)
# print(d)

