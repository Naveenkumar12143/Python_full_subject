__author__ = "Naveen kumar"

data = "my name is naveen kumar  qualification is Bsc.Degree"

# b = data.upper()
# print(b)
# print(b.endswith("BSC.DEGREE"))
# print(data)

# print(data.endswith("Bsc.Degree"))
# print(data.endswith("bcom.degree"))
# print(data.endswith("bsc.degree")) # python is case sensitive        print(data.startswith("my"))



# data = "my are name is naveen kumar  qualification is Bsc.Degree"
# print(data.startswith("my"))
# print(data.startswith("MY"))
#

''' 
count() method
Syntax: obj.count(sub-str, [start= 0,end=len(string)])

the method count() returns the number of occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation'''

# data = "My name is Naveen kumar. my designation is code developer"
# print(data.count('is'))
# print(data.count('i'))
# print(data.count('is', 5 ,65))  # 5 is starting address 65 is the ending address
# print(data.count('e', 2 ,70 ))  # 2 is starting address 70 is the ending address

"""
find: returns the index if available otherwise returns -1
Syntax: obj.find(sub-string, beg=0, end=len(string))
Return Value : Index if found ,and -1 otherwise'''
"""

# data = "My name is Naveen kumar. my designation is code developer"
# a = "Nav"
# print(data.find(a))
# b = "am"
# print(data.find(b))
# c = "Is "  # case sensitive so, it gives us -1 as output
# print(data.find(c))
# i = "nave" # case sensitive so, it gives us -1 as output
# print(data.find(i))
# g = "kumar"
# print(data.find(g, 1, 33)) # search starts from 10 & end at 33
# e = "nation"
# print(data.find(e))

#####################################################################################
# data = "********sensors are working properly without having any issue*******"
# print(data.rstrip("*"))

#####################################################################################
# data = "********sensors are working properly without having any issue*******"
# print(data.strip("*"))
#####################################################################################
# data = "Naveen kumar"
# print(data.zfill(111))

"""
index: 
======
Syntax: str.index(sub-str, [beg=0 end=len(string)])
Return Value : Index (int) if found otherwise raises ValueError exception if str is not found'''
Note: Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as access notation.
"""
# data = "this is Naveen kumar and Praveen kumar,Bsc.Btech"
# print(data.index("Naveen"))
# data = "naveen"  # case sensitive so
# print(data.index(data)) # it is giving exception


###################################################################################
"""The + operator can be used for string concatenation """
# a = "naveen"
# b = "praveen"
# c= a + b
# print(c)
# print(a+ " " +b)
# print(a)
# print(b)

###################################################################################
# # strings are immutable, so the += operator re-binds the reference to a new object
# s = "new"
# print(s)
# s += "brand"  # s = s+ "brand"
# print(s)
# s += "land"  # s = s+ "land"
# print(s)


# z = 55
# z = "B.sc"
# z =  76.9
# print(z)

# y = [34, "raju", 58.2]
# print(y)


