__author__ = "Naveen kumar"

""" ############ Data validation Technics ############"""
###################################################################################################
"""
isidentifier : Return True if the string is a valid Python identifier, False otherwise.
"""
# a = "_naveen_3"
# print(a.isidentifier())

# a = "5naveen_3"
# print(a.isidentifier())

##################################################################################################
'''The method isalpha() checks whether the string consists of alphabetic characters only
This method returns true if all characters in the string are alphabetic and
there is at least one character, false otherwise'''

# data_1 = "virendersehwag"
# data_2 = "hello Welcome to banglore"

# print(data_1.isalpha()) # No space & digit in this string
# print(data_2.isalpha())

#####################################################################################################
'''This method returns true if all characters in the string are alphanumeric or character, false otherwise'''
# z = "in2022"  # No space in this string
# print(z.isalnum())
# h = "pychram_23.6"
# print(h.isalnum())
# h = "pychram_23"
# print(h.isalpha())
# h = "pychram"
# print(h.isalpha())
#
# i = "hi hello iam naveen i am learning .python"
# print(i.isalnum())

#####################################################################################################
'''The method isdigit() checks whether the string consists of digits only'''
# hi = "123456"  # Only digit in this string
# print(hi.isdigit())
# hello = "ABC123456"  # Only digit should be in this string
# print(hello.isdigit())
# print(hello.isalnum())
# print("1234567".isdigit())  # True #Useful when converting to int
##################################################################################################
"""
        Return True if the string is a lowercase string, False otherwise.
"""
# data = "my name is Naveen kumar	Qualification is B.tech"
# print(data.islower())
# data = "this is string example wow ............!...."
# print(data.islower())  # returns true if all characters in the string are lowercase, false otherwise
###################################################################################################
"""
isupper()  Return True if the string is an uppercase string, False otherwise.
"""
# data = "my name is Naveen kumar	Qualification is B.tech"
# print(data.isupper())
# data = "NAVEEN & MAHALAKSHMI"
# print(data.isupper())

'''This method returns true if the string is a
 title cased string(each word 1st letter should capitalise),false otherwise'''
# john = "Naveen Kumar "
# print(john.istitle())
# john = "My Name is John	Qualification is M.sc"
# print(john.istitle())
###################################################################################################
###################################################################################################
"""
        Return True if the string is a whitespace string, False otherwise.
"""
# raju = "my name is Boyina Narendra Qualification is M.tech"
# print(raju.isspace())
# data = "                  "
# print(data.isspace())
###################################################################################################
###################################################################################################

"""The method max() returns highest alphabet in the string like x/y/z (based on ASCII conversion)"""
"CapitalA ASCII value is 65 (B=66,C=67,D=8) and small a ASCII value 97 (a=97, b=98, c=99,d=100)"
# a = "Murali"
# print(max(a))
# print(min(a))

##################################################################################################
"""
replace:
=======
syntax: str.replace("sub-str", "replace_sub_str", [occurrence])
Return a copy with all occurrences of substring old replaced by new.
count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.
    If the optional argument count is given, only the first count occurrences are  replaced.
"""

# a = "Banglore"
# b = a.replace("l", "b")
# print(b)
# print('xyxyxyxyxyxxyxy'.replace('x','c')) # ByByBBxBzB replaced in all occurrences
# print('xyxyxyxyxyxxyxy'.replace('xy','ch', 2)) # replaced in only 2 occurrences
# print('xyxyxyxyxyxxyxy'.replace('y','tn',4)) # replaced in only 4 occurrences

"""game = input("enter name")
rolle = input("enter rolle")
order = input("enter batting order")
print("He is {0} and {0}'s rolle is {1} and {0}'s order is {2} ".format(game,rolle, order))"""

#################### Practice #######################
# a = "".join(["chintha","naaveen","kumar"])
# print(a)
# a = " ".join(["chintha","naaveen","kumar"])
# print(a)
# b = (["#chintha","@naaveen","_kumar"])
# c = " * ".join(b)
# print(c)

