__author__ = "Naveen kumar"

import string, random

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# user_data = ''.join(string.ascii_letters + string.punctuation+string.digits)
# print(user_data)
#
# user_data = ''.join(string.ascii_letters+string.digits)
# print(user_data)
#
# print(random.choice(user_data))

""" practice programs  """

# print([random.randint(0, 15)for i in range(6)])  # list comprehension
# password generation

# print([random.choice(user_data) for no_of_values in range(4)])

import random

# n =[]
# for no_of_values in range(0,7):
#     a = random.choice(user_data)
#     n.append(a)
# y = " ".join(n)
# print(y)

# print(" ".join([random.choice(user_data)for no_of_values in range(7)]))

""" ############ math module ###################### """
import math
# print(math.factorial(5))
# print(math.sqrt(81))  # square root always provide float value
# print(math.pow(2,5))  # power function provides float output


from math import *

# print(factorial(4))
# print(sqrt(4))
# print(pow(5,8))

from math import factorial

# f = [factorial(x) for x in range(10)]
# print(f)   # output:  len of factorial of numbers till 20 [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]

# f = {(factorial(x)) for x in range(10)}
# print(f)   # output:  len of factorial of numbers till 20 [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11,

# m = {(factorial(s) for s in range(20))}
# print(m)