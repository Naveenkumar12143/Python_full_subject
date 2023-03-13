"""
operators 2
"""

__author__ = "Naveen kumar"

"""
6. Bitwise operators
================
It operates bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111. ( 128 64 32 16 8 4 2 1 code)
"""
# print("******`** Bitwise operators ********")

x = 12
y = 4
# print("x&y value is", x & y)
# print("x|y value is", x | y)
# print("x^y value is", x ^ y)

# a = 12
# b = 8
# print("a&b value is", a & b) # & Binary AND
# print("a|b value is", a | b) # | Binary OR
# print("a^b value is", a ^ b) # ^ Binary XOR if both are 1 then result is 0

# y = 5
# print(" ~ y value is",~y )# ~ Bitwise Complement -(5+1) = -6
# Bitwise Complement of value is -(value+1) ==> -(-6+1)  ==> -(5) ==> 5

# x = 8
# print("~ value is ", ~x)

# a = -8
# print("~a value is", ~a)


a = 15
# print("a<<3 value is", a << 3) # << Binary Left Shiftprint
# print("a<<2 value is", a << 2)
# print("a>>3 value is", a >> 3)


b = 9
# print(" b>>2 value is", b>>2) # << Binary Right Shiftprint
# print(" b>>3 value is", b>>3)


# c = 47
# print("c>>3 value is ", c>>3)

# d = 16
# print("d<<2 value is ", d<<2)
# print("d>>3 value is ", d>>3)

z = 15
# print("~ z value is", ~z)

# int = -15
# print("~ int value is", ~int)


"""
7. Membership operators:
   ====================
The membership operators in Python are used to test whether a value is found
within a sequence (such as strings, lists, or tuples.)
Two membership operators exist in Python"""


"""
in – evaluates to True if the value in the left operand appears in the sequence
found in the right operand
"""
# print("******** Membership operators ********")

# print('Hello' in 'Hello world!')
# print('hello' in 'Hello W0rld!')
# print("what" in "which where")
# print("50" in "40 60 70")
# print("Naveen" in "Naveen praveen")
# print("+" in "- ^ & *")
# print("&" in " &")

"""not in – evaluates to True if the value in the left operand doesn’t appear in
the sequence found in the right operand"""

# print("Hi" not in "Hello How")
# print("car" not in " car bus cycle")
# print("john" not in "sai ravi raju")
