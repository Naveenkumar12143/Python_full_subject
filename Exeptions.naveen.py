__author__ = "Naveen kumar"

"""
What is Exception?
An exception is a Python object/event that represents an error.
An exception occurs during the execution of a program 
that disturbs the normal flow of the program's instructions.

In general,when a Python script encounters a situation that it cannot cope with,
it raises an exception.

Handling an exception
If you have some suspicious code that may raise an exception,
you can defend your program by placing the suspicious code in a try: block. 
After the try: block, include an except: statement,
followed by a block of code which handles the problem as elegantly as possible.

"""

def mul(x,y):
    print(x*y)


# mul(3, 6)
# mul(2.3, 3.1)
# mul(4, 2.5)
# mul("5", 2)
# mul("naveen", "praveen")  # TypeError: can't multiply sequence by non-int of type 'str'
# print("python")
# print("narendra sir")



def add(a, b):
    try:
        print(a+b)
    except TypeError:
        print("user provided incorrect values")
    except ValueError:
        print("user provided wrong values")
    except TypeError as vineela:
        print(vineela)
    except ValueError as val_error:
        print(val_error)
    except Exception as narendra:
        print(narendra)

    else:
        print("No exception occurred ")
    finally:
        print("Vineela, subhash, naveen")



# add(4, 3)
# add(3, "naveen")
add("praveen", "naveen")

"""Syntax
Here is simple syntax of try....except...else blocks −

try:
   You do your operations here (suspicious code )
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 

finally:
    Execute single /multiple statements irrespective of exception block
"""

"""
Example : 1 
This example opens a file, writes content in the, file 
and comes out gracefully because there is no problem at all −
"""

