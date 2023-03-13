__author__ = "Naveen kumar"
"""
The OS module allows us to interact with the underlying operating system in several different ways.
- Navigate the file system
- Get file information
- Look up and change the environment variables- Move files around
- Many moreTo begin, import the os module. This is a built in module, 
no third party modules need to be installed.
"""

import os,time
from datetime import  datetime

# dir()  # will display all of the methods and attributes of os module
# print(dir(os))

"""to get current working directory """

# path = os.getcwd()
# print(path)  # C:\Users\HP\Desktop\important

"""To change directory, from one path to another path. 
this requires a path to change to """

# syntax ==> os.chdir(path)
# path = r"D:\pythonProject\sir projects\Microsoft.SkypeApp_kzf8qxf38zg5c!App"
# path = r"C:\Users\HP\Desktop\important"
# os.chdir(path)
# print(os.getcwd())

"""To print list of directory names in provided path,
Syntax ==> os.listdir(path) but by default path is in the current directory"""

# path = r"C:\Users\HP\Desktop\important"
# os.chdir(path)
# print(os.listdir(path))

# path = r"C:\Users"
# os.chdir(path)
# print(os.listdir(path))  # will display

"""" To create a new directory. 
 Syntax ==> mkdir("Directory/folder name")"""

# os.mkdir("Sravani")
# os.mkdir("triweni")
# os.mkdir("triveni")

# os.mkdir(r"C:sssssssssssssssssss")


# os.mkdir(r"C:\Intel\Wireless\Data\aruna\karthik")

"""" Remove single directory/ multiple directories
     Syntax ==> os.rmdir(file)"""

# os.rmdir("triweni")
# os.rmdir("triveni")
# os.rmdir(r"C:sssssssssssssssssss")




############"""creation of directories/sub-dir"""#############

"""if you want to create multiple directories at once
(directory inside directory inside directory ..ectc)
Syntax ==> os.makedirs("directory_Name/Sub_directory_1/Sub_directory_2")"""


# os.makedirs("Rangappa/Pushpavathi/Praveen kumar/Naveen kumar")
# os.makedirs("Narendra sir/veneela/subhash/naveen/rohit")


############"""Removes of directories/sub-dir"""#############

"""if you want to remove multiple directories at once
(directory inside directory inside directory ..ectc)
syntax ==>os.removedirs("directory_name/sub_directory_1/sub_directory_2")"""

# os.removedirs("Rangappa/Pushpavathi/Praveen kumar/Naveen kumar")
# os.removedirs("Narendra sir/Veneela/Subhash/Naveen/Rohit")


# os.makedirs("Game/cricket/lover")
# Dirs created ==>path changed ==>printed path after changed==> came back one stepDir
# path = "Game/cricket/lover"
# os.makedirs(path)
# path_before_enter = os.getcwd()  # will display pwd
# print(path_before_enter)  # C:\Users\HP\Desktop\important

""" come back with giving path """

# os.chdir("../")  # based on OS  we have to given/direction
# print(os.getcwd())  # C:\Users\HP\Desktop

# os.chdir("../../")
# print(os.getcwd())  # C:\Users


""" create a file with write mode  """

# fp = open("test.txt", "w+")
# fp.write("Hi,\nThis file was created just for execution purpose")
# fp.close()

""" Rename a file or folder"""

# os.rename("test.txt","mahesh.txt")  # This renames text.txt to mahesh.txt
# os.rename("mahesh.txt","Basha.txt")  # This renames text.txt to Basha.txt

""" Look at info about files"""
# print(os.stat("Basha.txt"))
# Useful stat results: st_size (bytes), st_mtime (time stamp)
# print(os.stat("Basha.txt").st_size)  # display size of the file
# print(os.stat("Basha.txt").st_mtime)  # display the last modification time of the file (but can't understand by user)
# last_mod_time = os.stat("Basha.txt").st_mtime
# print(datetime.fromtimestamp(last_mod_time))  # Now user can understand recently file modified time
# present_time = time.time()
# print(present_time)
# print(datetime.fromtimestamp(present_time))


""" Create directories 10 & each directory should contain one text file ?"""

# name = input("Enter any name :")
# name = input("Enter any name :")
# file_name = input("Enter name for file: ")
# for i in range(1,3):
#     path =r"C:\Users\HP\Desktop\important"
#     x = name + "_" + str(i)  # creating directory name
#     os.mkdir(x)  # creating folder
#     os.chdir(x)  # entering in to that directory
#     y = file_name+".txt"  # preparing a file name
#     open(y,"a+")  # with the file_name, creating a file
#     os.chdir(path)


"""create 5 directories, Each  directory should have one directory  & in that sub directory 1 text file should be there."""

outer_dir_name = input("Enter outer dir name: ")
inner_dir_name = input("Enter any name: ")
file_name = input("Enter name for file: ")

for i in range(1,6):
    path = os.getcwd()
    outer_dir_name = outer_dir_name+"_"+str(i)
    os.mkdir(outer_dir_name)
    os.chdir(outer_dir_name)
    a = inner_dir_name +"_"+ str(i)
    os.mkdir(a)
    os.chdir(a)
    z = file_name+".json"
    with open(z,"a+") as f_o:
        f_o.write("this is present in "+path+"/"+ outer_dir_name+"/"+a+ "folder")
    os.chdir(path)
    outer_dir_name = outer_dir_name[ :outer_dir_name.index("_")]

