__author__ = "Naveen kumar"
"""
if condition is True:
    this statement/ statements will execute

"""
"""
C language:
===========
void main()
{
if x<10
    {
    =======
    =======
    =======
    }
else
{
=============
============
===========
===========
==========
}
}
"""
# nvn = input("enter any number")
# print(nvn,type(nvn))
#nvn = int(input("enter any number"))
#print(nvn,type(nvn))
#if nvn < 18:
#    print("given number less than 18")
#    print("{} is less than 18".format(nvn))
#    print("$$$$$$$$$$$$")
#print("lucky")
#print("jihn")

#N = input("Enter any number: ")  # taking input from user
#N = N.upper()
#if  N== "NAVEEN":
#    print("given number less than 18")
#    print("{} is less than 18".format(N))
#    print("****************$")
#print("lucky")
#print("jihn")

#number = int(input("Enter any number"))
#number = 32
#if number % 4 == 0 and number % 8 == 0:
#     print(number, "is divisible by 4 and 8")
#     print("44$$$$$$$$#####@@@@@@@&&&&&&&")
#print("Narendra")


"""
# if else Syntax:
==============
if expression:
   statement(s)
else:
   statement(s)
"""
#Narendra = int(input("Enter any number: "))
#if Narendra < 10:
#     print("given number less than 10")
#     print("*************************")
#else:
#     print("given number greater than 10")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#print("Bhagyasree")
#print("Mahalakshmi")


#u = input("Enter any name: ")
#u =u.lower()
#if u == "winner":
#     print("given number less than 10")
#     print("*************************")
#else:
#     print("given number greater than 10")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#print("Bhagyasree")
#print("Mahalakshmi")

"""
if elif else Syntax:
==================

if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)

Note: for this syntax, I will explain with real time example in next file

"""
# x = int(input("Enter any number: "))
# if x <= 100:
#     print("given no is less than 100")
#     print("Narendra")
# elif x >100 and x <= 200:
#     print("given no is less than 200 more than 100")
# elif x > 200 and x <= 300:
#     print("given no is less than 300 more than 200")
# elif x > 300 and x <= 400:
#     print("given no is less than 400 more than 300")
# else:
#     print("given no is  more than 400 ")
# print("lucky")
# print("dummu")

"""
Ternary operator 
How can the ternary operators be used in python? 

Ternary operator will be given as:

Ans: The Ternary operator is the operator that is used to show the conditional statements. 
This consists of the true or false values with a statement that has to be evaluated for it.

Syntax:

The Ternary operator will be given as:
[on_true] if [expression] else [on_false]

Result = x if x < y else y

Example:

The expression gets evaluated like if x<y else y, in this case if x<y is true then the value is returned as big=x and if it is incorrect then big=y will be sent as a result.

"""

# x, y = 115,135
# small = x if x < y else y
# print(small)

x,y = 205,333
largest_number = x if x>y  else y
print(largest_number)


"""
The assert keyword is used when debugging code. 
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. 
You can write a message to be written if the code returns False, check the example below.
"""
# x = input("Enter name:") ##  if the condition doesnot satisfy, The below code doesn't provide any information
# if x == "Naveen":
#     print("qwerty")


# x = input("Enter nnumber:")
# #if condition returns False, AssertionError is raised:
# assert x == "Narendra", "x should be 'Narendra'"

x = int(input("Enter nnumber:"))
assert x < 10, "x should be grater than 10"
