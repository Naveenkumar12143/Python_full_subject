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


# mul(3,6)
# mul(2.3,3.1)
# mul(4,2.5)
# mul("5",2)
# mul("naveen", "praveen")  # TypeError: can't multiply sequence by non-int of type 'str'


# Exception handling for above logic


def add(a, b):
    try:
        print(a+b)
    except TypeError:
        print("user provided incorrect values")
    except ValueError:
        print("Invalid input type")
    except NameError as john:
        print(john)
    except ValueError as val_error:
        print(val_error)
    except Exception as naveen:
        print(naveen)

    else:
        print("No exception occurred ")
    finally:
        print("Ravi, subhash, naveen, Raju")


# add(4,3)
# add(9, "naveen")
# add("naveen", 3.6)

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


# try:
#    fk = open("Nithin.txt", "w+")
#    fk.write("This is my test file for exception handling!")
# except IOError:
#    print("error occurred, write permissions deleted for the file")
# else:
#    print("Written content in the file successfully")
#    fk.close()

# print("ravi")
# print("ramu")


# try:
#    fw = open("karthik.txt","w")
#    fw.write("This is my test file for exception handling!!")
# except IOError:
#    print("error occurred , write permissions deleted for the file")
# except Exception as nvn:
#     print(nvn)
# else:
#    print("Written content in the file successfully")
# finally:
#     print("we are indians")
    # fw.close()
    # print(fw.closed)

# print("Done!")


"""
This produces the following result −

Written content in the file successfully
"""

"""
This example tries to open a file where you do not have the write permission, so it raises an exception −
"""
# try:
#     fr = open("software.txt","r+")
#     fr.write("something")
# except TypeError:
#     print("error occurred, w r f ")
# except Exception as m:
#     print(m)
# else:
#     print("written content in the file successfully")
# finally:
#     print("do hard work")
#     fr.close()
#     print(fr.closed)
#
# print("king")
# print("queen")

"""
This produces the following result −

Error: can't find file or read data
"""
# Argument of an Exception

def v_convert(var):
   print(int(var))
   try:
      return int(var)
   except ValueError as x:
       print(x)
   except TypeError as ka:
       print("**Type error:", ka)
   except Exception as m:
       print(m)

# Call above function here.
# x = v_convert(12.5)
# e = v_convert("13.5")
# y = v_convert([65656])

# print(x)
# print(e)
# print(y)
# print("cricket")
# print("foot ball")

"""
Output
The argument does not contain numbers
invalid literal for int() with base 10: '13.5'
"""

# The try-finally Closed

# try:
#   fh = open("testfile.txt", "w+")
#   fh.write("This is my test file for exception handling!!")
# finally:
#    print("Hi, Irrespective of try block final block code will be execute")
#    fh.close()
#    print(fh.closed)


# Nested try block

# try:
#    fh = open("testfile.txt", "w+")
#    fh.write("This is outer try block")
#    try:
#       fh.seek(0,0)
#       data = fh.read()
#       print(data)
#       fh.write("This is my test file for exception handling!!")
#       print("john")
#    except IOError:
#       print("Error occurred in inner try block")
# except IOError:
#     print ("Error: can\'t find file or read data")
# finally:
#    print ("Going to close the file")
#    fh.close()
#    print(fh.closed)


"""
How to handle any exception ? If we don't know which exception may occur 
"""
def add(a,b):
    try:
        print(a+b)
    except Exception as error:
        print(error)

# add(40, 50)
# add(9, "nani")

# x = int(input("enter any x value "))
# print(x, type(x))
# y = int(input("enter any y value "))
# if x < 10 and y < 10:
#     print("Nani")
#     print("Naveen")
# else:
#     print("sai")
#     print("sofiya")

