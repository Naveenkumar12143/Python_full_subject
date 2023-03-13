__author__ = "Narendra Boyina"
"""
This is a User defined module
performs following functions
[addtion]
"""
def Bhagyasree():
    print("W/o Narendra Boyina")
    print("Completed M.tech")
    print("Simple,obedient and Understanding Nature")
# Bhagyasree()

def add(a,b):
    """
    it will perform addition
    :param a: 1st input
    :param b: 2nd input
    :return: return addition value
    """
    c = a +b
    print(c)
    return c

# c = add(2,3)

def abc(c,d,a=24,b=10):
    """
    This function performs
    :param c:
    :param d:
    :param a:
    :param b:
    :return:
    """
    print(a,b,c,d)
    return

# abc(12,24,13,15)


def printinfo(arg1, *vartuple ):
    """
    this function performs variable length arguments
    other than 1st argument's value, remaining values will be stored in tuple
    :param arg1:
    :param vartuple:
    :return:
    """
    print ("arg is: ", arg1)
    print ("arg is: ", vartuple)
    # for var in vartuple:
    #     print ("Varible length arg is",var)
    return

# # Now you can call printinfo function
# printinfo()      #  TypeError: printinfo() missing 1 required positional argument: 'arg1'
# printinfo(10)
# printinfo(60, 70)
# printinfo(50, 60, 70)
# printinfo(50, 60, 70,49,30,279,467,78, 67.87)
#
# a=[10,23,56,78]
# b=list(a)
# print(b)
# a[3]=95
# # a[1]=34
# print(b)

# def m(list):
#     v = list[0]
#     for e in list:
#         if v > e:
#             v = e
#     return v
#
#
# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
#
# for row in values:
#     print(m(row), end=" ")
#
# print("my friend name is{}, his age is".format("Narendra",28))
# print("D", end = ' ')
# print("C", end = ' ')
# print("B", end = ' ')
# print("A", end = ' ')
#
# print(format("Welcome", "10s"), end = '#')

# print("abef".replace("cd","12"))





