__author__ = "Naveen kumar"

import json
from json import load

"""
json full form JavaScript Object notation.
Inspired by java script but now independent to any programming language
In json most frequent functions are 4 (load, loads, dump, dumps)
"""

"""
Note:1 In Notepad/Notepad++ save below data with extension .json
while saving we can provide any name. 
save the file, where the source(.py) file you are supposed to write,
I mean in the same directory)"""

"""json.load() is used to read the dictionary data, from JSON file """


with open("address.json")as nvn:
    data = json.load(nvn)


print(data)
name = data["name"]
biodata = data["biodata"]
age = data["age"]
print(name, "\n", biodata, "\n", age)


""" ************ OR ************ """

with open("biodata.json")as data_file:
    data = load(data_file)

# print(data)
# print(data["brother name"])
# print(data["from"])
# print(data["from"][5:])
# print(data["from"][:5])
# print(data["parents"])

""" json.loads() is used to convert the JSON String into the Python dictionary."""

# human = '{"game":"cricket","role":"all rounder","my favorite cricketers":["virender shewag","kane wiliamsion"]}'
# human_dict = json.loads(human)
# print(human_dict, "\n", type(human_dict))
# print(human_dict["my favorite cricketers"])

"""******************************************************************************"""

"""json.dump() method can be used for writing data into JSON file.

Syntax: json.dump(dict, file_pointer)"""

"""The dump() method is used when the Python objects have to be stored in a file.
The dump() needs the json file name in which the output has to be stored as an argument."""

# data to be written

content = {"alpha": "ABCDEFGhijklm",
           "upper": "ABCDEFGHI",
           "lower": "abcdef",
           "digits": "12345",}


# print(content)

with open("john.json", "w") as outfile:
    json.dump(content, outfile)

"""

json.dumps() method can convert a Python dictionary into a JSON string.
Syntax: json.dumps(dict, indent)

dumps() is used when the objects are required to be in string format(used for parsing, printing,...)
dumps() does not require any such file name to be passed.
"""

# Data to be written

content = {
    "Favorite game": "Cricket",
    "Batting order": "Opening",
    "Role": "Batting All rounder",
    "Batting style": "Right Hand Bat",
    "Bowling style": "Right-arm off spin",
}

# json_object = json.dumps(content)
# print(json_object)
# print(type(json_object))

