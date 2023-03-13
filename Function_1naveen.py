__author__ = "Naveen kumar"
"""
The purpose of a function is code re-usability.
Once the basic structure of a function is finalized,
you can execute it by calling it from another function or directly from the Python prompt.

Function Syntax:

def fun_name([arguments]):
    '''[doc_string]'''
    function_suite
    return [Value/s]

Types of functions  : 2
1. Non-recursive functions & 2. Recursive function """

"""
Non recursive functions 
1. function without arguments
2. functions with arguments/ positional/ Required arguments
3. functions with Default arguments
4. functions with Variable-length arguments (* args) Ex: *narendra
5. functions with Keyword arguments (**args) / (**kw args) Ex: **surendra
6. function with command line arguments
optional: functions with Keyword based arguments
"""
""" function without arguments """


def print_my_info():
    print("naveen")
    print("praveen")
    print("****^^^^****")


# print_my_info() # the purpose of function is code re-usability
# print_my_info()
# print_my_info()
# print_my_info()

"""function with positional arguments"""


def genarate_email(e,f):
    """
    this function will genarate email.
    :param e: first name
    :param f: last name
    :return: personal email id
    """
    print(e+"_"+f+"@gmail.com")


# Now you can call printme function
# genarate_email("naveen","kumar")  # programmer friendly
# e = input("enter first name")
# f = input("enter last nmae")
# genarate_email(e,f)               # user friendly
# a = input("enter first name")
# b = input("enter last nmae")
# genarate_email(a,b)           # user friendly
# o = input("enter first name")
# p = input("enter last nmae")
# genarate_email(o,p)

'''
Function with Arguments also known as Required Arguments 

Required arguments are the arguments passed to a function in correct positional order. 
Here, the number of arguments in the "function call" should match exactly with the "function definition".
 '''


def print_me(nk,pk,nvn): # Function definition is here
    """ this prints a passed string into this function """
    print(nk,pk,nvn)


# Now you can call printme function
# print_me(45,65,35)
# print_me(11,22,)

'''
OUTPUT:
When the above code is executed, it produces the following result −

Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 3 argument (2 given)
TypeError: print_me() missing 1 required positional argument: 'nvn'
'''


'''
Function with Default Arguments
A default argument is an argument that assumes a default value if a value is not provided 
in the function call for that argument. 
The following example gives an idea on default arguments, 
it prints default age if it is not passed
'''

def person_info(name,age=23): # Function definition is here
    """ this prints a passed info into this functions"""
    print("name: ",name)
    print("Age:",age,"year/s")


# Now yu can call printinfo function
# person_info()
# person_info("Naveen")
# person_info("mintu", 6)
# person_info("Naveen kumar",)

def nvn(c,n, x=25,y=50):
    print(c,n,x,y)
    print(x, n, y, c)
    print(c+n+x+y)


# nvn()
# nvn(5)
# nvn(13,15)
# nvn(5,6,8,9,)


"""
 Variable-length Arguments:
 You may need to process a function for more arguments than you specified while defining the function. 
 Syntax for a function with non-keyword variable arguments is given below −
"""
"""
def function_name([formal_args,], *var_args ):
   "function_docstring"
   function_suite
   return [expression]

An asterisk (*) is placed before the variable name that holds the values of all non-keyword variable arguments.
This tuple remains empty if no additional arguments are specified during the function call.
Following is a simple example −

Function definition is here

"""


def print_info(arg,*var_tuple):
    """ this function performs variable length arguments
    other than 1st arguments remaing values will be stored in tuple
    """
    print("arg is: ", arg)
    print(var_tuple)
    return


# now you can call printing function
# print_info() #NameError: name 'printinfo' is not defined. Did you mean: 'print_info'?
# print_info(10)
# print_info(33,76)
# print_info(2,5,8)
# print_info(33,65,"naveen",45.7,"hi")


def sample_calculator(N,*v):
    print(N,v)
    # calculator addition
    # for z in v:
    #     N = N+z
    # print(N)
    # calculator multiplication
    # for g in v:
    #     N = N*g
    # print(N)

# sample_calculator(1,3)
# sample_calculator(0,2,5,6,7)


'''
Keyword  based Arguments
Keyword based arguments are related to the function calls. 
When you use keyword arguments in a function call, 
the caller identifies the arguments by the parameter name.

This allows you to skip arguments or place them out of order because 
the Python interpreter is able to use the keywords provided to match the values with parameters. 
You can also make keyword calls to the printme() function in the following ways −
'''


def printinfo(salary,name,age,y,company):
    print("sal: ",salary)
    print("Name: ",name)
    print("age: ",21)
    print("y value is: ",26)
    print("company: ",company)

# Now you can call printinfo function
# printinfo(34343,"allu",32,44,"rock")
# printinfo(45000,name="Naveen",company="ibm",y = 26,age = 21,)



##========= Practice programs =================

def neha(list):
    v = list[0]
    for e in list:  # iterate inner list
        if v < e:
            v = e
    return v

# values = [[4,6,8,22],[5,8,97]]
# for row in values:
#     print(neha(row), end=" ")

# data =[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
# def lucky(n):
#     x = n[0][1]
#     for row in n:
#         for elements in row:
#             if x < element:
#                 x = element
#     print(x)
#
# neha(data[0])

# u = [2,11,4,32,67,[43]]
#
# v = list(u)
# print(id(u),id(v))
# u = [2, 4, 3, [43]]
# k = list(u)
# u[3][0] = 99
# u[1] = 81
# print(k)

# def sai(a, *b,c =5,**k):
#     print(a,b,k,c)
#     # print(range (10))

# sai(a=10,b=20)
# sai(5,2,5,6,7)

# def sai(a,b =5 ,*v,**k):
#     print(a,b,v,k)

# sai(5,2,6,7,10,13,17,27,n =33,c=5,m='n+4jk',z = 2.5)

# def func(x, y = 1):
#     z = x * y + x + y
#     return z
#
# print(func(2,func(3)))

# def func(x = 1 ,y = 2):
#     z = x * y + x + y
#     return z
#
# print(func(2, func(3)))

# def func(x, y):
#     z = x * y + x + y
#     return z
#
# func(2, func(3,4))

# min = (lambda x, y: x if x < y else y)
# print(min(101*99, 102*98))
#
# print(102*98)

class A:
    x = 10

    def __init__(self, y, z):
        self.y = y
        self.z = z

    def update_y(self):
        self.y = self.y * self.z


A1 = A(3, 4)
A2 = A(5, 6)

A.x = 30
# A1.y + A2.x