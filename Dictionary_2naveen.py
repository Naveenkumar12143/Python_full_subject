__author__ = "Naveen kumar"

#################     d.fromkeys(seq,val)    #################
# a = ["surendra", "Aruna","Naveen", "narendra", "bhagyasree"]
# z = [33,44,55,66,77]
# n = {}  # taken empty dictionary
# h = n.fromkeys(a,z)
# z = 45
# print(h)
# print(h["surendra"])
# h = n.fromkeys(a,z)
# print(h)
##############################################################################

s = {'surendra': [33, 44, 55, 66, 77], 'Aruna': [33, 44, 55, 66, 77], 'Naveen': [33, 44, 55, 66, 77],
     'narendra': [33, 6.7, 5995, 121, 77], 'bhagyasree': [33, 44, 55, 66, 77]}
#The method get() returns a value for the given key.
# #If key is not available then returns default value None.
# print(s["Naveen"])
# print(s.get("Naveen"))
# print(s["narendra"])
# print(s.get("narendra"))
# print(s.get("lucky"))### (None) ##### # #If key is not available then returns default value None.

# # The method keys() returns a list of all the available keys in the dictionary.
# l = {'surendra': 29, 'Aruna': 26, 'narendra': 30, 'swathi': 22, 'john':55}
# print(l.keys())
# print(l.values())
# print(l)

fine = {"firstName": "Narendra", "lastName": "Boyina", "age": 27, "sex": "M", "salary": "xxxxxx",
           "registered":"false"}
# print(fine)
# print(fine.keys())
# print(fine.values())
# del fine["age"]
# print(fine)

########## Membership operators in dictionaries  ###############

lucky = {
    "firstName": "Narendra",
    "lastName": "Boyina",
    "age": 24,
    "sex": "M",
    "salary": "xxxxx",
    "registered": True,
}

"""Test if a key exists in a dictionary (Use in operator to test weather a key exists or not"""
# print('salary' in lucky )  #Output: True#
# print('hi' not in lucky)
# print('sex' not in lucky)
# print('lastname' in lucky)  ##case sensitive
# print('lastName' in lucky)

##############    list of dictionaries    ################
# data = [1, 2, 3]

nani = [
    {'name': 'Narendra',
     'mobile': '9700422902',
     'email': ['boyinanarendra1@gmail.com', "Vinod", 'bhagyasreenarendra@gmail.com', "Hanumanth", "Harinath",
               "Sudheer"]},

    {'name': 'Naveen kumar',
     'mobile': '80749xxx77',
     'email': 'naveenk12143@gmaail.com'},

    {'name': 'BR Techno Solutions',
     'mobile': '9000 30 1444',
     'email': 'virenderraju5@gmai.com'}
    ]

# print(nani, type(nani))
# print(nani[1]["email"])
# print(nani[1]["email"][-4:])
# print(nani[2]["name"])


##############    dictionary of dictionaries    ################

hello = {155: {'name': 'Narendra', 'mobile': '9700422902', 'email': 'boyinanarendra1@gmail.com'},
            22: {'name': 'Surendra', 'mobile': ["2332333", '9959538530'], 'email': 'surendraboyina1@gmail.com'},
            330: {'name': 'Yugesh', 'mobile': '9999900007', 'email': 'sivaramprasad.perumella@gmail.com'}
            }

# print(hello)
# print(hello.keys())
# print(hello[22].values())
# print(hello[22].keys())
# hello[330]["email"] = "naveenk12143@gmail.com"


#############    tuple of dictionaries    ################

raj = (
    {'name': 'Narendra',
     'mobile': '9700422902',
     'email': ['boyinanarendra1@gmail.com', "Vinod", 'bhagyasreenarendra@gmail.com', "Hanumanth", "Harinath",
               "Sudheer"]},

    {'name': 'Surendra',
     'mobile': '99595xx530',
     'email': 'surendraboyina1@gmail.com'},

    {'name': 'BR Techno Solutions',
     'mobile': '9000 30 1444',
     'email': 'brtechnosolutions2019@gmail.com'}
)

# print(raj[0])
# print(raj[1])
# print(raj[2])
# print(raj , type(raj))
# print(raj[1]["email"][-10 :])
# print(raj)

a = {"A":1,"B":2}
a["c"] = ""
print(a.get('c'))
print(a)