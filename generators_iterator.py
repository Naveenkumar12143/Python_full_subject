__author__ = "Narendra Boyina"

"""
What is a Generator function ?

A generator function is a normal function except that it contains yield expression
in the function definition making it a generator function.
Generators are a way of implementing iterators.

To get the next value from a generator, we use next().
"""
# Generator Function :
"""" Execute the below code in python idle/interpreter don't execute in pycharm tool.
For better understanding purpose use python interpreter """


# Generator Function :

def sunny():
    print("Ashok")
    print("Harinath")
    yield ("Narendra")
    print("Anand Yadav")
    print("Surendra")
    print("devendra")
    print("veerendra")
    yield ("End")
#
# >>x = sunny()
# >>next(x)
# Ashok
# Harinath
# 'Narendra'
# >> > next(x)
# Anand
# Yadav
# Surendra
# devendra
# veerendra
# 'End'
# >> > next(x)

# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#11>", line
# 1, in < module >
# next(x)
# StopIteration
#
"""
What happens when we compile the Generators ?

	1. When we compile the Generators, a Generator Object is created but all its code is not completely run.
	2. Execution of the code in a generator stops once a yield statement has been reached.
	3. Once yield statement is encountered, it returns a value.
	4. When the function is called next time using "next(object),
	the execution continues from the state in which the generator was left after the last yield.
This continues until it raises a StopIteration exception.
"""
"""
What are Generator Expressions ?

Generator Expressions are much like List Comprehensions but
 the Generator expressions returns an object on which we can iterate using next()
"""
# Example of Generator Expression
""""""
# >>> gen_exp = (n+1 for n in range(1,4))
# >>> next(gen_exp)
# 2
# >>> next(gen_exp)
# 3
# >>> next(gen_exp)
# 4
# >>> next(gen_exp)
#
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     next(gen_exp)
# StopIteration
# >>>



"""
# What is an Iterator ?
#
# Iterator is an object which allows a programmer to iterate through all the elements of a collection.
#
# In a normal language,
# we can say, an Iterator is an object which is used to iterate over a group of elements.
#
# """
# >>> sample = [1,3,5]
# >>> x = iter(sample)
# >>> next(x)
# 1
# >>> next(x)
# 3
# >>> next(x)
# 5
# >>> next(x)
# Traceback (most recent call last):
#   File "<pyshell#47>", line 1, in <module>
#     next(it)
# StopIteration
#
"""
Explanation of the Example :

	1. Create a list of 3 elements 1,3 and 5.
	2. Creating an iterator "it" using iter().
	3. The list "sample" is passed to the iter function and the returned object is stored in "it"
	4. The first time, next is called, it returns first element "1"
	5. The second time, next is called, it returns the second element "3"
	6. The third time, next is called, it returns the third element "5"
	7. The fourth time, next is called, an error "StopIteration" is returned since there are no more
Elements to return.
"""