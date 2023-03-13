__author__ = "Naveen kumar"

"""
strings are homogeneous immutable sequence of unicode characters 
(By default unicode characters in python 3.X But in python 2.X "are a ASCII text")

# a = unicode('Naveen')
# a = u'Naveen'
# a = "Naveen"


strings can be represented using single/ double/ triple codes 
(But triple codes we are using to comment the lines.
 ==> it (""" """) is also string but Interpreter treated as  multi-commented lines,
  will not be executed 
"""

# Ex ('Naveen' == "Naveen")


"""
############## Elements accessing  ###################
Syntax: variable = instance[SA : EA : step]
SA means Starting address
EA means Ending address
index always starts with Zero ends with -1
"""
"""@@@@@  Single element accessing   @@@@@@
Syntax:  variable = instance[index]
"""

c ="naveen"
# print(type(c))
# a = c[0] # variable = instance[index]
# print(a)
#
# print(c[0])
# print(c[2])
# print(c[5])
# print(c[-1])
# print(c[-3])
# print(c[-5])
# print(c[-4])


"""
@@@@@  range of elements accessing   @@@@@@
variable = instance[SA : EA]
"""
b = "Chintha Naveen Kumar"
# print(len(b))
# print(b[0:3]) # we have to give end index always number+1
# print(b[0:6])
# print(b[0:8])
# print(b[5:13])
# print(b[4:17])
# print(b[3:16])

b = "Chintha Naveen Kumar"
# print(b[6:16])
# print(b[2:12])
# print(b[4:-2])
# print(b[6:-4])
# print(b)

# print(b[ :3])  # omitting starting address
# print(b[ :7])

# print(b[4:12])  # omitting ending address
# print(b[2:18])

# print(b[:]) # omitting both
# print(b)

# print(b[ :-3])
# print(b[ :-6])
# print(b[7:-3])
# print(b[-4:-2])


""" @@@@@  Step elements accessing @@@@@@
variable  = instance[SA : EA: step]"""

a = "virender sehwag"
# print(a[ : :3]) # last parameter is related to difference (start, stop, step)
# print(a[ : :2])
# print(a[0: : 2])
# print(a[3: :2])
# print(a[5:  :4])
# print(a[1 : :4])
# print(a[2 : :5])
# print(a[3:8:2])

#################Built-in String Methods ###################
x = "my name is Chintha Naveenkumar my qualification is Bsc.degree"

# print(x)
# print(type(x))


# print(x.upper()) # Converts all lowercase letters in string to uppercase.
# print(x.lower()) # Converts all uppercase letters in string to lowercase.
# print(x.swapcase()) # MY NAME IS cHINTHA nAVEENKUMAR MY QUALIFICATION IS bSC.DEGREE
# print(x.title()) #
# print(x.capitalize())

''' In the output, only 1st letter will be Capital
remaining letters will be modified as small letters'''
######################################################################
''' 
Syntax: obj.center(__width,[__fillchar]) 
=====================================
The method center() returns centered in a string of length width.
Padding is done using the specified fill char.Default filler is a space.
                        (Or)
Returns a space-padded string with the original string centered to a total of width columns'''
a= " python software "
# print(len(a))
# print(a.center(45))
# print(a.center(65, '*'))
# print(a.center(65, ' '))
# print(a.center(90, '-'))

"""obj.rjust(__width,[__fillchar]):
================
Returns a space-padded string with the original string right-justified to a total of width columns.
This method returns the string right justified in a string of length width.
Padding is done using the specified filled char (default is a space).
The original string is returned if width is less than len(s)"""

# a = 8.9
# b = 2
# c = 5
# print(a//b//c)

# n = (6.7//7//9)
# print(n)

# x=10
# if x%2==0:
#     print("even number")
# else:
#     print("odd number")

# x= 67
# if x>50:
#   if x>90:
#     print("excellent")
#   else:
#     if x>80:
#       print("good")
#     else:
#       print("fair")
# else:
#   if x>30:
#     print("average")
#   else:
#     print("poor")

# a='pqrstuv'
# i='j'
# while i in a:
#     print(i)

# s="Upgrad"
#
# for i in range(len(s)):
#     if s[i] in 'a':
#         s[i]='*'
#
# print(s)

import random


# Take input
# inp=input('Please Enter a charcter:' )
# # write your code here
# if inp.isdigit():
#     print('Integer')
# elif inp.isalpha():
#     print('Alphabet')
# else:
#     print('Special charcter')

# print(ord('D'))
# print(ord('D')+1)
# print(ord('D')-1)
# print(chr(8))
# # print(chr(68),str(+1))
#
# print(chr(68))
# print(ord('D'))
#
# b = 8
# print(b+1)
# print(b-1)

# string = input()
# x = ''
#
# for i in string:
#     if i not in 'aeiouAEIOU':
#         x = x+i
#     else:
#         pass
# print(x)

L = ['one','two','three', 'four', 'five', 'six']
print(sorted(L))
print (L)