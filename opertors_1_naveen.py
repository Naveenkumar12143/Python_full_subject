"""__author__ = "Naveen kumar"

operators are classified in to 3 types
1. Unary operators (python don't support Unary operators) Ex: a++ a-- ++a --a 
2. binary operators (Require 2(bi) operands (a, b) to perform operation)
3. ternary operators 
"""
# import keyword
# print(keyword.kwlist)


"""  Binary operators"""

"""
1. Arithmetic operators

Arithmetic operators are used to perform mathematical operations like addition,
subtraction, multiplication, division, floor division,  modulus..etc.
"""
#print("******** Arithmetic operators ********")

## this will be perfornm addition
# a = 6
# b = 3
# print('a + b=', a+b)

## Subtract right operand from the left
# a = 8
# b = 3
# print ('a - b=', a-b)

## Multiply two operands
# a = 7
# b = 3
# print('a * b =', a*b)

## Divide left operand by the right one(always results into float)
# a = 4
# b = 12
# print('a / b =', a/b)

## Modules - reminder of divison of left right (a % b (reminder of  a/b) )
# a = 4
# b = 26
# print ('a % b =', a%b)

## Floor divison with integer - division that results into whole numberadjusted to the left in the number line
# a = 6
# b = 30
# print('a // b =', a//b)

## Floor divison - with floot values
# a = 6.0
# b = 3.0
# print('a // b =', a//b)

## ** acts as power
# a = 5
# b = 4
# print('a ** b =',a**b)

"""
2. Comparison operators
=======================
Comparison operators are used to compare values.
It either returns True or False according to the condition.
"""
# print("******** Comparison operators ********")
# x = 10
# y = 15
# print('x > y', x>y)

# x = 10
# y = 15
# print('x < y',x<y)

# x = 12
# y = 8
# print('x >= y',x>=y)

# x = 16
# y = 11
# print('x <= y', x<=y)

# x = 20
# y = 20
# print('x == y',x==y)

# x = 55
# y = 45
# print('x == y',x==y)

# x = 7
# y = 16
# print('x != y', x!=y)

# x = 15
# y = 15
# print('x != y',x!=y)

"""
3. Logical operators
===================
Logical operators are the and, or, not operators"""

# print("******** Logical operators ********")
# math_work = True
# easy_work = True
# print('math_work and easy_work',math_work and easy_work)
#
# naveen = False
# kumar = False
# print('naveen or kumar',naveen or kumar)
#
# a = True
# b = False
# print(' not a',not a)
#
# x = False
# y = True
# print(' not x', not x)
#
# num = True
# john = True
# print('not num', not num)

# hi = False
# hello = False
# print('not hi',not hi)

"""
4. Assignment operators
======================
Assignment operators are used in Python to assign values to variables. these operators are extension of Arthametic operators
a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same.
It is equivalent to a = a + 5.

Operator Example Equivalent to

+=  =====> x += 5 ===>  x = x + 5
-=  =====> x -= 5 ===>  x = x - 5
*=  =====> x *= 5 ===>  x = x * 5
/=  =====> x /= 5 ===>  x = x / 5
%=  =====> x %= 5 ===>  x = x % 5
//= =====>  x //= 5 ===>  x = x // 5
**= =====>  x **= 5 ===>  x = x ** 5
"""

# print("******** Assignment operators ********")
# a = 5
# a += 14
# print(a)

# b = 9
# b -=4
# print(b)

# c = 12
# c *= 5
# print(c)

# d = 5
# d /=10
# print(d)

# e = 7
# e %=5
# print(e)

# f = 8
# f //=4
# print(f)

# g =3
# g **=5
# print(g)

"""
5. Identity operators
=================
"is" and "is not" are the identity operators in Python.
They are used to check if two values (or variables) are located on the same part of the memory.
identity operators will return True or False
"""

# print("******** Identity operators ********")
# n1 = 29999
# print(id(n1))
# y2 = 29999
# print(id(y2))
# print(n1 is y2)
# print(n1 is not y2)

# a1 = 'naveen'
# print(id(a1))
# b1 = 'naveen'
# print(id(b1))
# print(a1 is b1)
# print(a1 is not b1)