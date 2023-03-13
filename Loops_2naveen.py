__author__ = "Naveen kumar"


## ==> for loop with "Strings" concept

# s = "john"
# for r in range(s):  ##TypeError: 'str' object cannot be interpreted as an integer
#     print(s)


# s = "pawan kalyan"
# for r in range(len(s)):
#     print(r)
# print(s[2])



# s = "pawan kalyan"
# for r in range(len(s)):
#     print(s[r])


# p = "python"
# for a in (p):
#     print(a)

################################################################
################################################################

"""==> for loop with [List] concept
==> for loop we can use 2 ways in [list] concept
==> 1st way
"""
""" Question: 
given input: "Nenu Nanna Amma sree Mahalakshmi Annyya Vadina lakshya-sree "
Requied Output:
Nenu
Nanna
Amma
sree
Mahalakshmi
Annyya
Vadina
lakshya-sree
This is my beautiful family
"""

# q = "Nenu Nanna Amma sree Mahalakshmi Annyya Vadina lakshya-sree ".split()  # return list of elements
# print(q)
# for index in range(len(q)):
# 	print(q[index])
# print("This is my beautiful family")

#  ==>2nd way

# n = "hi hello how are you mr chintha naveen kumar".split()
# for v in n:
#     print(v)
##============================================================================

"""==> for loop with enumerate concept
enumerate will give the index for the out sequence (list/tuple/dictionary of elements"""
#EXAMPLES

# a = 13,39
# print(a)  #(13, 39)


# a,b = 13,39
# print(a)  #13

# a,b = 13,39
# print(b)  #39

# a = ['Nenu', 'Nanna', 'Amma', 'Bhagyasree', 'Mahalakshmi', 'Annyya', 'Vadina', 'lakshya-sree', 'Raj']
# for i in enumerate (a):
#     print(i)
#
# for index, element in enumerate(a):    # we can use for  enumerate for tuple
#     print(index,"$$$$$$$$$$$$",element)
# print(type(index))   ##<class 'int'>
# print(type(element)) #<class 'str'>
#
# a = ["allu", 23, 6, 8.5, 93, "narendra", 4,"Maha lakshmi", 45,66,324,3.45]
# for subash ,naveen in enumerate(a):
#     print((subash+1,"$$$$$$$$$$",naveen))
#
##########################################################
## == > for loop with (tuple) concept
# h = ("raju","ravi","rahul","ramudu","radha","ram","roopa")
# for z in h:
#     print(z)
#
# for index,element in enumerate(h):
#     print(index,"^^^^^^^^***^^^^^^",element)

# h = ("raju", "ravi", "rahul", "ramudu", "radha", "ram", "roopa")
# for index,element in enumerate(h):
#     print(index +1, "^^^^^^^^***^^^^^^", element)

# h = ("raju", "ravi", "rahul", "ramudu", "radha", "ram", "roopa")
# # for k in range(len(h)):
# #     print(k)
#
# # for k in  h[:-4]:
# #     print(k)
#
# for k in  h[:7:2]:
#     print(k)

################################################################
"""==> for loop with {dictionary} concept
By default looping over a dictionary, gives access to all the keys
"""
y = {"firstName": "Naveen",
     "lastName": "kumar",
     "age": 20,
     "sex": "M",
     "salary": "xxxxx",
     "registered": True}
""" In dictionary for loop, "i" by default it considers the keys only """
# for u in y:
#     print(u)
# print(y.keys())
# print(y.values())
#
# for u in y.keys():
#     print(u)
#
# for u in y.values():
#     print(u)
#
# for key,value in y.items():
#     print(key,"**  #$^&#  **",value)


# for naveen, vineela in y.items():
#       print(naveen,"----->", vineela)

n = {"firstName": "Narendra",
     "lastName": "Boyina",
     "age": 27,
     "sex": "M",
     "salary": "xxxxx",
     "registered": True}

# for f,(u,v) in enumerate(n.items()):
#     print(f+1, u,  v)
#

################################################################
################################################################
""""== > for loop with {set} concept"""

# a = {"Nenu", "Nanna", "Amma", "Annyya", "Vadina", "Nanna","Nenu"}
# c = a
# print(c)
# for t in a:
#     print(t) # o/p is arranged because set is Unordered collection of unique data


###############################################################
