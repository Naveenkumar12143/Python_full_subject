__author__ = "Naveen kumar"

#example....

# a,b,c = 1,2,3
# print(a)

# a = 1,2,3
# print(a)

# to see entire directory tree and files within
# os.walk is a generator that yields a tuple of 3 values as it walks the directory tree

import os

# path =r"C:\Users\HP\Desktop\important"
# for dirpath,dirname,filename in os.walk(path):
#     print("current path :", dirpath)
#     print("Directories :",dirname)
#     print("File :",filename)
#     print("***********^^^^^^^^^***********")

# we take any variables  but follow the variable rules

# path =r"C:\Users\HP\Desktop\important"
# for praveen,naveen,kumar in os.walk(path):
#     print("current path :", praveen)
#     print("Directories :",naveen)
#     print("File :",kumar)
#     print("***********^^^^^^^^^***********")

# To properly join two files together use os.path.join(). & will be inserted one slash
# file_path = os.path.join(os.environ.get("HOME"), "test.txt") # linux
# print(os.getcwd())

# file_path = os.path.join(os.getcwd(), "Basha.txt")
# # the benefit of os.path.join, is it takes the guess work out of inserting a slash
# print(file_path)

# f_o = open(file_path,"r")
# f_o.read()

if os.path.exists(r"D:\pythonProject\pythonpractice\Game\cricket\lover"):  # returns a boolean
    os.chdir(r"D:\pythonProject\pythonpractice")
    fo = open("Ramanji.txt", "a+")
    fo.write("this is just created")
    fo.close()

# print(os.path.isdir(r"D:\pythonProject\pythonpractice\Game\cricket\lover"))  # True (or) False
# print((os.path.isfile(r"D:\pythonProject\pythonpractice\Basha.txt")))

# ^^^^^^^^^^ Very useful for file manipulation^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^ os.path has other useful methods^^^^^^^^^^

# print(os.path.dirname(r"D:\pythonProject\pythonpractice\Game\cricket\lover\Ramanji.txt"))# # returns the directory /tmp
# print(os.path.split(r"D:\pythonProject\pythonpractice\Rock star.json"))# # returns both the directory and the fil

"""We can find out, From the root path(provided by user) 
what are the files (.txt/.py/.doc)available in each sub-folders.  """

"""
The %s operator lets you add a value into a Python string. 
The %s signifies that you want to add a string value into a string. 
The % operator can be used with other configurations, such as %d, to format different types of values.
In more modern versions of Python, the % syntax has become less widely used in favor of f strings and the format() method.
"""

# x = "Praveen"
# print(x.endswith("n"))

def get_file_paths(path, extension):
    """
       we can find-out .py files available in each subdirectory from provided root directory
    """
    for path, subdir, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print("FileName: ", os.path.join(path, file))

# path =r"D:\pythonProject\pythonpractice"
# path = r"C:\Program Files (x86)\Google\Update"
# get_file_paths(path, ".py")


"""Create 5 folders & each folder should contain one text file"""

import os

# name = input("Enter any name : ")
# file_name = input("Enter name for file: ")
# for i in range(1,6):
#     path =os.getcwd()
#     x = name + "_"+str(i) # creating directory name
#     os.mkdir(x) # creating folder
#     os.chdir(x) # entering in to that directory
#     y = file_name+".txt" # creating file name
#     open(y,"a+") # creating a file
#     os.chdir(path)

import time
from time import sleep

# name = input("Enter any name : ")
# file_name = input("Enter name for file: ")
# for i in range(1,6):
#     path =os.getcwd()
#     x = name + "_"+str(i) # creating directory name
#     os.mkdir(x) # creating folder
#     os.chdir(x) # entering in to that directory
#     y = file_name+".txt" # creating file name
#     open(y,"a+") # creating a file
#     os.chdir(path)

# print("os.mkdir time starts now at %s" % time.ctime())
# time.sleep(15)
# print("os.rmdir time starts now at %s" % time.ctime())