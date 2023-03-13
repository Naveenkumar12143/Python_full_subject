__author__ = "Narendra Boyina"
import re

"""
Using ^ Caret
^ - Caret. Matches a pattern at the start of the string.
"""


string = 'praveen kumar and Naveen kumar'
pattern = r'^praveen'  #The match found is :  praveen
pattern = r'^naveen'  #The match not found :



# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match found is : ",result)
# else:
#     print("The match not found")


"""
Using $ - Dollar Symbol
$ - Matches a pattern at the end of string.
"""

string = "my name is naveen kumar"
pattern = r'kumar$'  #The match found is :
pattern = r'naveenkumar$'  #The match not found :


# if re.search(pattern,string):
#     result = re.search(pattern,string).group()
#     print("The match found is : ",result)
# else:
#     print("The match not found")


"""
Using [abc] - Matches a or b or c.
[abc] - Basically matches atleaset one element that are present within in the square brackets
"""

string = 'boy boll box booooe  bills bracket boundary'
pattern =r'bo[ylx]'

# if re.search(pattern,string):
#     # result = re.search(pattern,string).group()  #The match found is :  boy
#     result = re.findall(pattern,string) # findall wll reurn list of elements"The match found is :['boy', 'bol', 'box']"
#     print("The match found is : ",result)
# else:
#     print("The match not found")


# re.search(r'Number: [0-9]', 'Number: 5').group()
# Output : Number: 5
"""
Using \ ( Back Slash) 
If the character following the backslash is a recognized escape character,
then the special meaning of the term is taken. For example, \n is considered as newline.
However, if the character following the \ is not a recognized escape character,
then the \ is treated like any other character and passed through.
"""

string = r'Hi this is my Naveen\kumar and Ravi\teja' # My string contains Black slash

pattern = r'Naveen\\kumar'
pattern = r'Ravi\\teja'

if re.search(pattern,string):
    result = re.search(pattern,string).group()
    print("The match found is : ",result)
else:
    print("The match not found")



