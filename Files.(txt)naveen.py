__author__ = "Narendra Boyina"
"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.
S = "Narendra"

## Syntax for Open a file
f_object = open(filename, mode)
There are different modes for opening a file:
==> txt file modes r r+ w w+ a a+
==> binary modes rb rb+ wb wb+ ab ab+



f_o = open("Rama.txt", r+)

1.r
Opens a file for reading only.
The file pointer is placed at the beginning of the file. 
This is the default mode.

2.rb
Opens a file for reading only in binary format.
The file pointer is placed at the beginning of the file.
This is the default mode.

3. r+
Opens a file for both reading and writing.
The file pointer placed at the beginning of the file.

4. rb+

Opens a file for both reading and writing in binary format.
The file pointer placed at the beginning of the file.

5. w
Opens a file for writing only. Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.

6. wb

Opens a file for writing only in binary format.
Overwrites the file if the file exists.
If the file does not exist,creates a new file for writing.

7. w+
Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist,creates a new file for reading and writing.

8. wb+

Opens a file for both writing and reading in binary format.
Overwrites the existing file if the file exists.
If the file does not exist,creates a new binary file for reading and writing.

9. a
f_p = open("priyanka.txt", 'a')
Opens a file for appending. 
The file pointer is at the end of the file if the file exists.
If the file does not exist,it creates a new file for writing.

10. ab

Opens a file for appending in binary format. The file pointer is at the end of the file
if the file exists. 
If the file does not exist, it creates a new file for writing.

11. a+

Opens a file for both appending and reading.
The file pointer is at the end of the file if the file exists.
If the file does not exist, it creates a new file for reading and writing.

12. ab+
Opens a file for both appending and reading in binary format.
The file pointer is at the end of the file if the file exists.
The file opens in the append mode. If the file does not exist,
it creates a new file for reading and writing.

"""

# 1
# fileobject.closed

# Returns True if file is closed, False otherwise.
#
# 2 fileobject.mode
#
# Returns access mode with which file was opened.
#
# 3. fileobject.name
#
# Returns name of the file.

##Open a file
# f_o = open("praveen&naveen.txt","w+")
# print("name of the file: ",f_o.name)
# print("closed or not:" ,f_o.closed)
# print("which mode: ",f_o.mode)
# # f_o.closed()
# print("closed or not : ",f_o.closed)


"""
The close() Method
The close() method of a file object flushes any unwritten information and closes the file object, after which no more writing can be done.

Python automatically closes a file when the reference object of a file is reassigned to another file.
It is a good practice to use the close() method to close a file.

Syntax
fileObject.close()
"""


"""
The write() Method
The write() method writes any string to an open file.
It is important to note that Python strings can have binary data and not just text.
The write() method does not add a newline character ('\n') to the end of the string

Syntax
fileObject.write(string)
"""

##Open a file
# fw = open("sravani.txt", "w+")
# fw.write("This is my python file \t Yeah its great!!\nI hope you understand")
# fw.write("\nWriting in next line\n")
# fw.write("she is my first lover")
# fw.close()  # Closed the open file
# print("Closed or not : ", fw.closed)


"""
The read() Method
The read() method reads a string from an open file.
It is important to note that Python strings can have binary data. apart from text data.

Syntax
fileObject.read([count]);
Here, passed parameter is the number of bytes to be read from the opened file.
This method starts reading from the beginning of the file and
if count is missing, then it tries to read as much as possible, maybe until the end of file.
"""

# fs = open("sravani.txt", "r")  #open a file
# n = fs.read()
# print("Read String is : ", n)
# fs.close()  # closed file

"""
OUTPUT:
Read String is :  This is my python file 	 Yeah its great!!
I hope you understand
Writing in next line
she is my first lover
"""

# fs = open("sravani.txt", "r")  #open a file
# n = fs.read(17)
# print("Read String is : ", n)
# fs.close()  # closed file


# OUTPUT: # Read String is :  This is my python


"""
File Positions
The tell() method tells you the current cursor position within the file;
in other words, the next read or write will occur at that many bytes from the
beginning of the file.

The seek(offset, [from]) method changes the current file position.
The offset argument indicates the number of bytes to be moved.
The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, the beginning of the file is used as the reference position.
If it is set to 1, the current position is used as the reference position.
If it is set to 2 then the end of the file would be taken as the reference position.
"""

# fp = open("pushpa.txt", "w+")
# fp.write("qwerty This is my python file \t Yeah its great!!\nI hope you understand")
# fp.write("\n writing in the line")
# fp.write("\n she my mother")
# fp = open("pushpa.txt", "r")
# john = fp.read(6)
# print("read string is: ",john)
# fp.close()
# position = fp.tell()
# print("current cursor position in file: ",position)
# fp.seek(12,0)
# position = fp.tell()
# print("current cursor position in life: ",position)
# print("mode is: ", fp.mode)
# fp.seek(0, 0)
# fp.write("enjoy to learn")
# fp.close()
# print(fp.closed)

"""
This produces the following result
Read String is :  This isBha
Current cursor position in file:  10
mode is:  r+
Again read String is :   file 	 Yeah its great!!
I hope you understand
Writing in next line
True

"""

def read_line_wise(path_file):
	f = open(path_file)
	output = f.readlines()
	print(output)
	print(output[0])  # only
	f.close()


# path_file = "sravani.txt"
# read_line_wise(path_file)

daily_tasks = []

def read_lines(path):
	f = open(path, 'r+')
	for t in f.readlines():
		daily_tasks.append(t)
	print(daily_tasks)

# path ="pushpa.txt"
# read_lines(path)
# print("dummu")
# print("lucky")


daily_tasks = []

def read_lines(data):
	try:
		f = open(data, "r")
		for t in f.readlines():
			daily_tasks.append(t)
		print(daily_tasks)
	except Exception as o:
		print(o)


data = "kseryfhdgbfhsusjhdh.txt"
read_lines(data)
print("john")
print("cricket")