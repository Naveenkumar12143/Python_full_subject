__author__ = "Naveen kumar"


def kw_fun(*narendra, **rohith):
    print(narendra, rohith)


num_list = [1, 5, 3]
num_tuple = (4, 8, 6)
d = {'a': 7, 'c': 9}

# kw_fun() #() {}
# kw_fun(11, 2.2, "Narendra")   # (11, 2.2, 'Narendra') {}
# kw_fun(nv=9,pv=22,rp=12,) #() {'nv': 9, 'pv': 22, 'rp': 12}
# kw_fun(1, 66, "naveen", a=1, b=2.5, c="praveen") #(1, 66, 'naveen') {'a': 1, 'b': 2.5, 'c': 'praveen'}

# kw_fun(*num_list, **d) #(1, 5, 3) {'a': 7, 'c': 9}
# if user provides in list of elements still it takes into tuple
# kw_fun(*num_tuple, **d) #(4, 8, 6) {'a': 7, 'c': 9}
# if user provides in tuple of elements still it takes into tuple
# kw_fun(99,55, *num_list) #(99, 55, 1, 5, 3) {}
# kw_fun(1, 2, *num_tuple) #(1, 2, 4, 8, 6) {}
# kw_fun(q="win", **d) # () {'q': 'win', 'a': 7, 'c': 9}
# kw_fun(55,89, *num_tuple, n=14,**d) #(55, 89, 4, 8, 6) {'n': 14, 'a': 7, 'c': 9}

"""
passing arguments while defining a function.
order:

def func_name(positional_args, default_args, *args, **kwargs):
    doc_string
    function_suite
    :return
"""

# order of elements while writing a function: required, default, *args, **kwargs

def func_name(a, b, d=20, e=40, *nv, **pk):
    print(a, b, d, e, nv, pk)


# func_name()  # TypeError: func_name() missing 2 required positional arguments: 'a' and 'b'
# func_name(5)  # TypeError: func_name() missing 1 required positional argument: 'b'
# func_name(3,8)  # 3 8 20 40 () {}
# func_name(14,6,7,8) # 14 6 7 8 () {}
# func_name(1,4,6,3,44,66) # 1 4 6 3 (44, 66) {}
# func_name(5,7,0,6,77,x=5,y=98) # 5 7 0 6 (77,) {'x': 5, 'y': 98}

"""
Pass by Reference vs Value
All parameters (arguments) in the Python language are passed by reference. 
It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example −
"""
#1 Call by value
# CALL BY VALUE
# Function definition is here

lucky =[11,22,44]


def think_us(lucky):
    """This changes a passed list into this function"""
    print("Values inside the function before change: ",lucky)
    # john =[2,4,6]
    # john.append("naveen")
    lucky.append("praveen")
    print("values inside the function after change:",lucky)



# think_us(lucky)
#lucky = think_us(lucky) ## Always calling function will be replaced with it's return value/values
# print("Values outside the function: ", lucky)

'''
The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist. 
The function accomplishes nothing and finally this would produce the following result −
Values inside the function:  [2,4,6]
Values outside the function:  [11,22,44]
'''

# 02 Call by reference
hi = [23,64,85]

def v(hi):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", hi)
    hi.append("hello")
    hi[2] = "rockstar"
    a = ["bye",57,"see","you"]
    print(a)
    print("Values inside the function after change: ", hi)


# Now you can call changeme function
# v(hi)  # Always calling function will be replaced with it's return value/values
 # Values inside the function before change: ", hi)  #[23, 64, 85]
# Values inside the function after change: ", hi) #[23, 64, 'rockstar', 'hello']
# Values outside the function: [23,64,85]


# There is one more example where argument is being passed by reference and the reference
# is being overwritten inside the called function.


# '''
# #NOTE: when you call by reference the value outside the function gets changed
# functions continuation (class 2) and lambda function


# functions continuation (class 2) and lambda function

"""
The return Statement
The statement return [expression] exits a function, optionally passing back an expression to the caller.
 A return statement with no arguments is the same as return None.

All the examples given below are not returning any value. You can return a value from a function as follows −
"""

# Function definition is here

def sum_mul_dev(arg1,arg2,arg3,arg4):
    """
    this function will perform addition and multiplication
    :param arg1: have to provide telugu marks
    :param arg2: have to provide engish marks
    :param arg3: have to provide math marks
    :param arg4:
    :return:
    """
    n = 10
    total = arg1 + arg2 + arg3 + arg4
    mul = arg1 * arg2 * arg3 * arg4
    dev = arg1 - arg2 - arg3 - arg4
    print("inside the function total values: ",total)
    print("inside the function multiplication value: ", mul)
    # print("inside the function subtraction values: ", dev)
    # print(n)

    # return total,mul

# sum_mul_dev(10,20,30,40)
# total = sum_mul_dev(2,3,5,7)
# print("outside the function total values: ",total)
# print("outside the function multiplication value: ", mul)


# c =sum_mul_dev(4,3,2,1)
# print("outside the function total values: ",c)
# print("outside the function multiplication value: ", n)

# x,y =sum_mul_dev(7,4,2,1,)
# print("outside the function total values: ",x)
# print("outside the function multiplication value: ", y)


"""
Scope of Variables (Name space):
=================

All variables in a program may not be accessible at all locations in that program. 
This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier.
There are two basic scopes of variables in Python −

1. Global variables
2. Local variables

#Global vs. Local variables
Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.
This means that local variables can be accessed only inside the function in which
they are declared, whereas global variables can be accessed throughout the program body by all functions.

When you call a function, the variables declared inside it are brought into scope.
Following is a simple example −
"""

skype = 50  # This is global variable.

def sum(arg1,arg2,arg3):
    # Add both the parameters and return them."
    skype = arg1 + arg2 + arg3
    print("Inside the function local total : ", skype)
    return


# Now you can call sum function
# sum(25,5,40)
# skype = sum(25,5,40)  # Here total is local variable.
# print("outside the function global skype: ",skype) #outside the function global skype:  None


########### Recursive functions ########
# An example of a recursive function to find the factorial of a number

def calculator_factorial(s):
    """ this is a  recursive function
    to find the factorial of an integer"""
    if s == 2:
        return 2
    else:
        return(s *calculator_factorial(s-1))




number = 5

# number = int(input("Enter number for factorial: "))
nvn = calculator_factorial(number)
print(nvn)
print(calculator_factorial(4))
# print("The factorial of {0} is {1} ".format(number, calculator_factorial(number)))


"""
Explanation of above example

In the above example, calc_factorial() is a recursive functions as it calls itself.

When we call this function with a positive integer, it will recursively call itself by decreasing the number.

Each function call multiples the number with the factorial of number 1 until the number is equal to one. 
This recursive call can be explained in the following steps.



calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call

"""

# Interview question :
# =================
def nvn(a,*b,**c):
    print(a,b,c)
    print(a)
    print(b)
    print(c)


# nvn(1,2,3,4,5,"Bhagyasree",x =11, y=12,z=13)
# out put # 1 (2, 3, 4, 5, 'Bhagyasree') {'x': 11, 'y': 12, 'z': 13}

def cal(a, b, x):
    c = a + b
    d = a * b
    x -= 50
    print(c)
    print(d)
    print(x)
    return c, d, x

# cal(3,5,4)
# raja, vinod, kavya = cal(2, 3, 4) # calling function will be replace with it's return values
# print(raja, vinod, kavya)

# we can use different variables (identifiers) for capturing  return values
# mounika, sunny, naziya = cal(2, 1.5, 5)
# print

# we can capture retutn values in single variable (but it will store in tuple)
# john = cal(2,3,2)
# print(john)


