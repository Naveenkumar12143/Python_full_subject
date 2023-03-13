__author__ = "Narendra Boyina"
import re

# Repetitions

# the re module handles repetitions using the following special characters:


# Using Plus Symbol +
# +  Checks for one or more characters to its left.


# string = 'Hoooos is very good Hoooooooood'  # My string contains Black slash
# string = 'Hoooos is very good Hoowoood Hood'  # My string contains Black slash
# string = 'Hoooos is very good Hooooo@9999999oooosfqwertyuioood Hood'  # My string contains Black slash
# pattern = r'H\S+d'
# pattern = r'H\w+d'

# if (re.search(pattern, string)):
#     res = re.search(pattern, string).group()
#     # res = re.findall(pattern,string)
#     print("The match found is : ", res)
# else:
#     print("The match is not found")

"""
Using Start Symbol *
* - Checks for zero or more characters to its left.
"""

# string = 'match end of the story' # Zero occurrence
# string = 'mmmmmatch end of the story'
# string = 'mmmmaymmmatch end of the story'
# pattern = r'm*atch'

# if (re.search(pattern, string)):
# 	res = re.search(pattern, string).group()
# 	print("The match found is : ", res)
# else:
# 	print("The match is not found")

"""
Note : The + and * qualifiers are said to be greedy
"""


"""Using Question Mark ?
? - Checks for exactly zero or one character to its left.
"""

# string = 'blue Color is looking very beautiful'  #The match found is :  Color
# string = 'blue Colour is looking very beautiful'  #The match found is :  Colour
# string = 'blue Colouur is looking very beautiful'  # will not allow more than one occurrence
# pattern = r'Colou?r'
#
# if (re.search(pattern, string)):
# 	res = re.search(pattern, string).group()
# 	print("The match found is : ", res)
# else:
#     print("The match is not found")



# ====================================================================================================
#           Using { m } , {m, } and  {m , n }
# ====================================================================================================

# {x} - Repeat exactly x number of times.
#
# {x,} - Repeat at least x times or more.
#
# {x, y} - Repeat at least x times but no more than y times.
# ====================================================================================================

# string = 'john Na\tve\tn kumar Mobiless_ 7655s 565432875438 N\tm\tbe r i_s 95 02 75638765439 h@y#i$ A687@on Hello'

# pattern = re.compile(r'Na.ve.n')  # The match found is :  Na	ve	n
# pattern = re.compile(r'Nave.n')  # The match found is :  Nave	n
# pattern = re.compile(r'i\ws')  # The match found is :  i_s
# pattern = re.compile(r'h\Wy\Wi\W')  # The match found is :  h@y#i$
# pattern = re.compile(r'N\sm\tbe\sr')  # The match found is :  N	m	be r
# pattern = re.compile(r'A\S\S\S\Son')  # The match found is :  A687@on
# pattern = re.compile(r'\d')  # The match found is :  7
# pattern = re.compile(r'\d+')  # The match found is :  7655
# pattern = re.compile(r'\d{5,9}')  # The match found is :  565432875
# pattern = re.compile(r'^john')  # The match found is :  john
# pattern = re.compile(r'Hello$')  # The match found is :  Hello


# if (re.search(pattern, string)):
# 	res = re.search(pattern, string).group()
# 	print("The match found is : ", res)
# else:
# 	print("The match is not found")


# ====================================================================================================
#           Using Grouping ( )
# ====================================================================================================
# Suppose that, when you're validating email addresses and want to check the user name and host separately.
#
# This is when the group feature of regular expression comes in handy.
# It allows you to pick up parts of the matching text.
#
# Parts of a regular expression pattern bounded by parenthesis() are called groups

import re

string = 'Email id is naveenk_12143@gmail.com and he don\'t want to share his contact number'

pattern = r'( \w+)@(\w+.com)'


# if (re.search(pattern, string)):
# 	res = re.search(pattern, string)
# 	print("The complete match found is : ", res.group())
# 	print("The first part of the match is : ", res.group(1))
# 	print("The second part of the match is : ", res.group(2))
# else:
#      print("the match is not found")


# ====================================================================================================
#           Using findall
# ====================================================================================================
# findall(pattern, string, flags=0)

# Finds all the possible matches in the entire sequence and returns them as a list of strings.
# Each returned string represents one match.
str = 'Please contact us at: virenderraju5._1@gmail.com, support@gmail.com, xyz@hotmail.com'

pattern = re.compile(r'[\w.]+@[\w.]+')
#
# if re.search(pattern, str):
# 	res = re.findall(pattern, str)
# 	print("The match found is : ", res)
# 	print("Printing individual email id")
# 	for email in res:
# 		print(email)
# else:
# 	print("The match is not found")

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
"""
255.255.255.255

for 1st 255 purpose below pattern
250 - 255  ==> 25[0-5]
200 - 249  ==> 2[0-4][0-9]
100 - 199  ==> 1[0-9][0-9]
1-99       ==> [1-9]?[0-9]  # ? mark mean zero or 1 occurrence, ip address will not start with zero, so started with 1


Using \ ( Back Slash)
If the character following the backslash is a recognized escape character,
then the special meaning of the term is taken. For example, \n is considered as newline.
However, if the character following the \ is not a recognized escape character,
then the \ is treated like any other character and passed through.

Above pattern should occur 4 times but last we does not require .(dot)

So 3 times we are repeating same pattern by using {3}
same pattern we have repeated again at the end
"""

def validate_ip(Ip):
    """pass the regular expression and the string in search() method"""
    if (re.search(regex, Ip)):
        print("valid Ip address")
    else:
        print("invalid Ip address")

# Ip_1 = "214.153.82.19"
# validate_ip(Ip_1)  #valid Ip address
#
# Ip_2 = "194.51.189.246"
# validate_ip(Ip_2)  #valid Ip address

# wrong = "261.386.439.564"
# validate_ip(wrong)  # invalid Ip address