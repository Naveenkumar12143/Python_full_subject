__author__ = "Naveen kumar"

"""
while loop:
Repeats a statement or group of statements while a given condition is TRUE. 
It tests the condition before executing the loop body.

We generally use this loop when we don't know the number of times to iterate before hand.
Syntax of while loop:
====================
initialization
while test_expression:
    statement(s)
    updation

"""
# count = 10
# while count <15:
#     print("present count is:",count)
#     count += 1
# print("see you!")

# output:
# present count is: 10
# present count is: 11
# present count is: 12
# present count is: 13
# present count is: 14

# see you

# # '0' to  The 'Infinite' Loop
# #!/usr/bin/python3
# Calculator addition (continuous inputs from user)

# nvn = 5
# temp = 0
# while nvn == 5:
#     num = int(input("enter value: "))
#     temp += num
#     print("total value:",temp)
# print("see you!")

"""
# output :
# enter value: 5
# total value: 5
# enter value: 5
# total value: 10
# enter value: 15
# total value: 25
# enter value: 35
# total value: 60
# enter value: 60
# Enter a number  :Traceback (most recent call last):
#    File "examples\test.py", line 5, in
#       num = int(input("Enter a number  :"))
# KeyboardInterrupt
#
# """

# #03 Using else Statement with Loops
# #!/usr/bin/python3

# john = 2
# while john < 6:
#     print(john, "is less than 6")
#     john = john + 1
# else:
#     print(john, "is  not less than 6")


# output:
# 2 is less than 6
# 3 is less than 6
# 4 is less than 6
# 5 is less than 6
# 6 is  not less than 6

#04 Single Statement Suites
#!/usr/bin/python3

flag = int(input("Enter True as 1/ False as 0 : "))
while flag == 1:
    print('Hard disk Crashed due to Memory Issue!')
print("Good bye!")


"""
break keyword will cause your while/for-loop stop executing and exit with out reaching the end of the iterable
# or the end of the range function"""

# c = "Naveen  kumar love your work and do hard-work to reach your goal, don't be panic " \
# "Don't think all the people will know all the things your good boy"
#
# print(c)

#output:
#Naveen  kumar love your work and do hard-work to reach your goal, don't be panic Don't think all the people
# will know all the things your good boy


# d = c.split()  #return list
# print(d) # pinting list

#output:
#['Naveen', 'kumar', 'love', 'your', 'work', 'and', 'do', 'hard-work', 'to', 'reach', 'your', 'goal,', "don't", 'be',
#'panic', "Don't", 'think', 'all', 'the', 'people', 'will', 'know', 'all', 'the', 'things', 'your', 'good', 'boy']

# n =[]
# for a in d:
#     if a =="to":
#         break
#     else:
#         n.append(a)
# print(n)

# output: ['Naveen', 'kumar', 'love', 'your', 'work', 'and', 'do', 'hard-work']

#c = "[Naveen  kumar love your work and do hard-work to reach your goal, don't be panic " \
# "Don't think all the people will know all the things your good boy]"

# print(" ".join(d[:d.index("work")]))

#output: Naveen kumar love your

#print(len(c)) #148

"""
continue- keyword
by using continue keyword we tell our iterable(list/tuple/dict/set) to skip particular value & executing the rest of the code.
Example: except "panic" for print all the words in the list """

# z = ("john", "jididi", "dost" ,"my" ,"slef") #<class 'tuple'>
# z = ["john", "jididi", "dost" ,"my" ,"slef"]  #<class 'list'>
# z = {"john", "jididi", "dost" ,"my" ,"slef" } #<class 'set'>
# z = "john", "jididi", "dost" ,"my" ,"slef"   #<class 'tuple'>
#
# q = " 'john', 'jididi', 'dost', 'my', 'slef' " # <class 'str'>
# v =" john, jididi, dost, my, slef"
# print(type(v))
#
# print(z)
# output: ['john', 'jididi', 'dost', 'my', 'slef']
#
# f =[]
# for k in z:
#     if(k=="my"):
#         continue
#     else:
#         f.append(k)
# print(f)
#
# output: ['john', 'jididi', 'dost', 'slef']


# Interview questions on loops:
# ===========================
# How to replace a value in list multiple places at a time "
# hello will be replaced with Naveen

# y = ['22','32','342','4.5',"Naveen",'44','565','6786',"hi","55.6",'4.rl']
# # print(y)
# # print(type)
# # print(len(y))
#

# for a in y:
#     if a == "hi":
#         y[y.index(a)] = "hello"
#         print(y)
#
#    #######  OR  #########
# for n in y:
#     if n == "Naveen":
#         x = y.index("Naveen")
#         y[x] = "utfrdsefjyug"
#         print(y)#


# e = {1:"nvn",2:"pvn",3:"hi",4:"hello",5:"bye"}

# print(e)
# print(e.keys())
# print(e.values())


# for x in e:
#     print(x)

# for key in e.keys():
#     print(key)