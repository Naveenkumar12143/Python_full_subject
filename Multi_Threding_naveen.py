__author__ = "Naveen kumar"
"""
Threading in python is used to run multiple threads (tasks, function calls) at the same time. 
Note that this does not mean that they are executed on different CPUs.
"""
import time
from time import time,sleep

def sqaure(list):
    for number in list:
        sleep(0.5)
        print("sqaure of {0} is {1}".format(number,number**2))


def cube(list):
    for number in list:
        sleep(0.5)
        print("cube of {0} is {1}".format(number,number*number*number))


def mul(list):
    for number in list:
        sleep(0.5)
        print("mul of {0} is {1}".format(number,number*number))


# start_time = time()
# print(start_time)
# list = [1,2,3,4,5]
# sqaure(list)
# cube(list)
# mul(list)
# print(time()-start_time)

"""
output:

1654345759.158171
sqaure of 1 is 1
sqaure of 2 is 4
square of 3 is 9
square of 4 is 16
square of 5 is 25
cube of 1 is 1
cube of 2 is 8
cube of 3 is 27
cube of 4 is 64
cube of 5 is 125
mul of 1 is 1
mul of 2 is 4
mul of 3 is 9
mul of 4 is 16
mul of 5 is 25
7.64346448097229
"""


from threading import Thread

def sqaure(list):
    for number in list:
        sleep(0.5)
        print("sqaure of {0} is {1}".format(number,number**2))


def cube(list):
    for number in list:
        sleep(0.5)
        print("cube of {0} is {1}".format(number,number*number*number))


# def mul(list):
#     for number in list:
#         sleep(0.5)
#         print("mul of {0} is {1}".format(number,number*number))

# l = [1, 2, 3, 4]
# starting_time = time()  # takes the current system time
# T1 = Thread(target=sqaure, args=(l,))
# T2 = Thread(target=cube, args=(l,))
# # T3 = Thread(target=mul,agrs =(l,))
# T1.start()  # Start the thread's activity. Must be called at most once per thread object
# T2.start()
# # T3.start()
# T1.join()  # Wait until the thread terminates
# T2.join()
# # T3.join()
# print(time()-starting_time)  # ending time - starting time

