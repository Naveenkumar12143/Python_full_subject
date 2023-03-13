# def sai():
#     print("naveen")
#
# sai()
#
# def nvn(a,b,c):
#    print(a+b)
#    print(b*c)
#
#
# nvn(3,4,6)
#
# def rana(n,a,k,s,i,y,*v):
#    print(n,a,k,s,i,y,v)
#
#
# rana(4,5,6,7,8,9,10,11)
#
# def room(a,n =100):
#    print(a,n)
#
# room(4)
#
# def bunny(**kw_args):
#    print(kw_args)


# bunny(a=54,n=21)

# *******List Built in Methods *********

# insert() Method

# l = [1,'two','there','five','eight',45,63,72.1,'two','python']
# l.insert(2,'praveen kumar')
# print(l)

# count() Method

# n = l.count(1)
# print(n)

# index() Method

# t = l.index('python')
# print(t)

# reverse() Method

# l.reverse()  # 1st way
# print(l)

# t = l[: : -1]  # 2nd way
# print(t)

# &&&&&&&& append Method &&&&&&&&

# l.append([1,1,2,3,3,44,])
# print(l)

# &&&&&&&& extend() Method &&&&&&&&&&
# l.extend(["naveen",'praveen','kumar'])
# print(l)

# &&&&&&&& delete() Method &&&&&&&&

# del l[3]
# print(l)

# &&&&&&&& pop() Method &&&&&&&&

# w = l.pop()
# print(l)

# &&&&&&&& remove() Method &&&&&&&&

# l.remove('naveen')
# print(l)

#&&&&&&&& clear() Method &&&&&&&&

# l.clear()
# print(l)

# &&&&&&&& join() Method &&&&&&&&
h = ['nvn', 'pk', 'cnk']  # only strings take the join method you give integers it will give type error.

m = '$'.join(h)
print(m)

# using while loop

# a = 0
# while a<10:
#     print(a)
#     a = a+1
#     print("john", 'sai')

# n = []
# for a in range(10,20):
#     n.append(a)
# print(n)

# a = input('Enter any Name')
# a = 63
# if a % 9 ==0 and a % 7 == 0:
#     print(a, 'divisible by 9 and 7')
#     print('bye')

# nvn = [10,20,30]
#
# def sai(nvn):
#     print(nvn)
#     nvn.append(40)
#     nvn[1] = "python"
#     print(nvn)
#
# sai(nvn)
# print(nvn)

# 02 Call by reference
hi = [23,64,85]

def v(hi):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", hi)
    hi.append("hello")
    hi[2] = "rockstar"
    a = ["bye", 57, "see", "you"]
    print(a)
    print("Values inside the function after change: ", hi)

# call by value
def change(x):
    x = x+10
    print(x)

# y = 10
# print(y)
# change(y)

def change(x):
    x = x+1

# a = 10
# change(a)
# print(a)

# Call by Value Example-1

# def fun(x):
#     print('inside fun', x, id(x))
#     # print('inside fun')
#
# a=23
# print('outside fun', a, id(a))
# #print('outside fun', id(x))
# fun(a)
# print('Outside fun', a, id(a))
# # print('outside fun', id(a))

# call by Value Example-2

def sai(a):
    print('inside sai before modification : ', a, id(a))
    a=[100, 2.4]
    a.append('Naveen')
    # print(a,type(a))
    # print('inside sai after modification : ', a, id(a))

# a=[23]
# a.append(45)
# print('outside sai before calling : ', a, id(a))
# sai(a)
# print('outside sai after calling : ', a, id(a))


def sum_mul_dev(arg1, arg2, arg3, arg4):
    """
    this function will perform addition and multiplication
    :param arg1: have to provide telugu marks
    :param arg2: have to provide english marks
    :param arg3: have to provide math marks
    :param arg4:
    :return:
    """
    n = 10
    total = arg1 + arg2 + arg3 + arg4
    # mul = arg1 * arg2 * arg3 * arg4
    # dev = arg1 - arg2 - arg3 - arg4
    print("inside the function total values: ", total)
    # print("inside the function multiplication value: ", mul)
    # print("inside the function subtraction values: ", dev)
    # print(n)

    # return total

# sum_mul_dev(10,20,30,40)
# c = sum_mul_dev(2,3,5,7)
# print("outside the function total values: ", total)
# print("outside the function multiplication value: ", mul)


# ::::::::::Return Statement:::::::
def sai():
    print('good morning')
    print('lucky')
    return 10
    print('bad')

# print(sai())

def function(a, b, c, d, e, f):

    total = a + b + c + d + e + f
    mul=a * b * c * d * e * f
    return total, mul

# print(function(1, 2, 3, 4, 5, 6))
# function(1, 2, 3, 4, 5, 6)

# *********string , int concatenation******
name = "Naveen"
age = 23

# print('my name is '+ name +' and my age is ' +str(age))
# print('my name is ',name ,' and my age is ' ,str(age))
# print(f 'my name is {name} and my age is {age}')

# *********.format**********
# print('my name is  {} and my age is {} '.format(name,age)) # using variables
# print('my name is  {0} and my age is {1} '.format(name,age,25))  # using index values


# $$$$$$$$$$ conditionals $$$$$$$$$$$$$$$$$
# if 5 > 3:
#     print('True')  # condition satisfied
# else:
#     print('False')


# if 20 < 10:
#     print('True')
# else:
#     print('False')  # condition Not satisfied


# name = input('Enter any name : ')
# age = int(input('Enter your age : '))

# if age < 8:
#     print(f'{name} is a kid')

# elif (age > 8) and (age < 13):
#     print(f'{name} is a young ')
#
# elif (age >= 13) and (age < 18):
#     print(f'{name} is a teenager')
#
# else:
#     print(f'{name} is a adult')

# %%%%%%%% For  loop %%%%%%


# my_list = [1,2,3,4,5]
#
# for data in my_list:
#     print(data)

# %%%%%%%% continue statement %%%%%%

my_list = [10, 20, 30, 40, 50]

for num in my_list:
    if num == 30:
        print('found the number')
        continue
    # print(num)


# %%%%%%%%  Break statement %%%%%%


my_list = [10,20,30,40,50]

for num in my_list:
    if num == 30:
        print('found the number')
        break
    print(num)


# my_list = [1,2,3,4]
#
# for num in my_list:
#     for letter in 'abc':
#         print(num,letter)


# $$$$$$ For loop with RAnge &&&&&&&

# for num in range(5):  # range will be 0 to n-1
#     print(num)

# $$$$$$ Nested For loop with multiplication &&&&&&&

# for i in range(1,6):
#     for n in range(1,6):
#         k = i * n
#         print(k, end=' ')
#     print(k)


# ******* while loop *********
# count = 0
# while count < 5:
#     print('the count is : ', count)
#     count = count + 1
# print('Done !')

# ******* infinite lop *********

# var = 1
# while var == 1:
#     num = int(input("Enter any a Number: "))
#     print("You entered a :", num)
# print(' Thank you !')

# @@@@@@@@@ Functions @@@@@@@@@

def greeting():
    print('Hello')
    print('Have a grate day')

# greeting()

def add_mul_sub(a,b):
    total = a + b
    product = a * b
    differance = a - b
    return total,product,differance

# all = add_mul_sub(5,5)
# print(all)


# @@@@@@@@ Local variables @@@@@@@@

def fun1():
    x = 10
    print('The value of x is :', x)

def fun2():
    x = 50
    print('The value os x is :', x)
    fun1()

# fun2()

# @@@@@@@@ Global variables @@@@@@@@

x = 100

def fun1():

    print('The value of x is :', x)

def fun2():

    print('The value os x is :', x)
    fun1()

fun2()

# @@@@@@@@ passing a list as an argument @@@@@@@@


def function(data):
    for z in data:
        print(z)

sports = ['cricket','football','Kabadi']

# function(sports)

# @@@@@@@@ The pass statement @@@@@@@@

def fun5():
    pass


k = 'bmaunmdbraai'
a= k

# print(a[0: : 2])
# print(a[1: : 2])
# print(a[0: : 2]+","+a[1: : 2])

# a = ["one","two","three","four"]
# b = a
# print(a)
# print(b)

# a = ["one", "two", "three", "four","five","six"]
# b = sorted(a)
# print(a)
# print(b)
#
# a = ('Monty Python', 'British', 1969)
# print(list(a))

# user = input("take any Apple fruit")
# print(user)
# a = 'apple'
# print(a[: : -1])
# vowels = 'a','e','o','i','u'


# l = [1,2,3,4]
# for i in l[::1]:
#     print(i,end =" ")

# a,b = 0,1
# for i in range(0,10):
#     print(a)
#     a,b = b, a+b
#
# even_numbers = []
# for c in range(0,50):
    
# a = 1
# b = ("the number is ", + a)
# print(b)
#
# a = "naveen"
# b = " kumar"
# print(a + b)


# a = "naveen"
# b = "9"
# print(a + b)




# Fibonacci series program in python using recursive method

# a, b = 0, 1
# for i in range(0, 5):
#     print(a)
#     a, b = b, a+b
#

# swipe two variables without using third variable

# n = int(input("Enter a number"))
#
# a, b = 5, 10

# python program to reverse a number

n = "python"
print(n[: : -1])

# a = int(input("Enter a number"))
# b = int(input("Enter a number"))
#
# print(a+b,b-a,a-b)

# x, y = 20,30
# x = x+y
# y = x-y
# x = x-y
# print(x,y)

a = 7
b = 5.6

a , b = b, a
print(a,b)







