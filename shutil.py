"""shutil module help you automate copying files directories (Copying/moving/removing/ directories )
saves the step to the opening ,reading, writing , closing files """


# import shutil, os


"""
Syntax : shutil.copy(source_file_name,destination_file_name) # copy data from source to destination (both names must be a file)
1. Basically the UNIX command cp src dest (copies source file to the destination directory)
2. Destination directory has to exit
3. If the file name already exits there it will be over written
4. Access time & test modification time will be updated"""


# shutil.copyfile("a.json","narendra.json")

# shutil.move(files,Destination)
# shutil.copytree(src,dest)
# shutil.rmtree(path)



# source = os.listdir("/temp/")
# destination = "/temp/narendra_1"
# for file in source:
#     if file.endswith(".txt"):
#         shutil.copy(file,destination)

""""
1.copy data from src to destination
2.Both names must be files (copy files by name)"""


# shutil.copy ('/path/to/file','path/to/other file')
# shutil.move(files,destination)

"""
1. Recursively move a file /Directory(source) to another location(Destination)
2. Destination directory must not already exists """

# import shutil, os
# source = os.listdir("/temp/")
# destination = "/temp/Narendra_2"
# for files in source:
#     if (files.endswith(".txt")):
#         shutil.move(files,destination)
#         shutil.copytree(src,dest)
#
"""
1. Destination must not already exist
2. Error are reported to standard output
"""

# import shutil,os
source = "samples"
BACKUP = "samples-back"

# create a backup directory
# shutil.copytree(source,BACKUP)
# print(os.listdir(BACKUP))
# shutil.rmtree(path)
"""Recrsively delete adictory tree"""

# import shutil
# shutil.rmtree(r'one\two\three')

# source =r'E:\prasanth'
# destination = r"D:\VIDEOS"
# shutil.copytree(source, destination)


