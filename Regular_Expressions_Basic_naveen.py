__author__ = "Naveen kumar"
"""
Regular expression usually called as RegEx Built-in Module name is re
RegEx can be used to check if a string contains the specified search pattern.

Regular expressions provide a flexible and concise means to match strings of text. 

For example, a regular expression could be used to search 
through large volumes of text and change all occurrences of "cat" to "dog"
"""
import re
"""Syntx : re.match(pattern,string)
match () searches for the sub-string , which should be at the beginning of the string
search() searches for the required sub-string anywhere in the given sentence (but only 1st occurrence).
The group() function returns the string matched by the re """

string = "C:/Users/HP/Desktop/important/Regular_Expressions_Basic_naveen.py"
raw_string = r"C:/Users/HP/Desktop/important/Regular_Expressions_Basic_naveen.py"

string = " The biriyani is very tasty"
pattern = r"biriyani"

if re.match(pattern,string):
    print("The match is found")
else:
    print("The match is not found")


#output : The match not found


if re.search(pattern,string):
    print("The match is found")

else:
    print("The match is not found")

"""
Using Dot ( . )
. Dot  Matches any single character(any special character) except newline character.
"""
string = "The chicken is very tasty"

string = "The ch\ncken is very tasty"
# string = "The ch\tcken is very tasty"
pattern = r"ch.cken"

# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match fond is: ",result)
# else:
#     print("The match is not found")



"""
Using \w
\w - Lowercase w. Matches any single letter, digit or underscore. ( [a-z] or [A-Z] or [0-9] or _ )
"""

string = "cricket9 is outdoor game in India"

string ="cr_cket9 is outdoor game in india"
# pattern =r"cr\wck\wt\w"


# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match fond is: ",result)
# else:
#     print("The match is not found")


"""Using \W
\W - Uppercase W. Matches any character not part of \w (lowercase w)."""


# string = "p#t@on is a computer language"
# pattern =r"p\Wt\Won"
#
#
# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match fond is: ",result)
# else:
#     print("The match is not found")



"""
Using \s ( Lower Case s )
\s - Lowercase s. Matches a single whitespace character like: space, newline\n, tab\t, return\r.
"""

# string = "Naveen kumar is a bad boy "
# string = "Naveen\tkumar is a bad boy" # tab space
# string = "Naveen\nkumar is a bad boy" #New line
# pattern = r"Naveen\skumar"
#
# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match fond is: ",result)
# else:
#     print("The match is not found")


"""
Using \S ( Upper Case S )
\S - Uppercase s. Matches any character not part of \s (lowercase s).
searching only single other than space (ex: [a-z][A-Z][0-9]and [any special symbol])
"""

# string = "iam looking be@uty#u& "
# pattern = r"be\Suty\Su\S"
#
# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match fond is: ",result)
# else:
#     print("The match is not found")


"""
Using \d ( Small Case d )
\d - lower Case d. Matches any digit from 0 to 9 """

string = " My_code is 597878 80 97 91 77 28 74 2202 93508278999999999"

# pattern = r"\d"
# pattern = r"\d+"
# pattern = r"\w+"
# pattern = r'\d{4}' # \d\d\d\d # should have at least 4 then only it will match the pattern
# pattern = r'\d{10,15}' # Search for digits which are in a range of min 4 digits to max 7 digits

# if(re.search(pattern,string)):
# 	result = re.search(pattern, string).group()
# 	print("The match found is : ", result)
# else:
# 	print("The match is not found")

# Similar to the above said notations

# \t - Lowercase t. Matches tab.
# \n - Lowercase n. Matches newline.


# ====================================================================================================
#           Difference between Match and Search
# ====================================================================================================

#match() function checks for a match only at the beginning of the string (by default) whereas Search
"""
pattern = "vegtable"
sequence = "Cake and vegtable"

re.search(pattern, sequence).group()

# Output : vegtable
"""


# Match when the string is not in the beginning
"""
pattern = "S"
sequence1 = "HotSweet"
re.match(pattern, sequence1)

# Output : No match since "S" is not at the start of "HotSweet"
"""


# Match when the string is in the beginning
"""
sequence2 = "Sweet

re.match(pattern,sequence2).group()
# Output : 'S'
"""

