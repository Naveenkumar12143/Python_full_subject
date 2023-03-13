
__author__ = "Naveen kumar"
"""
Module: • Python module is nothing but a python file(the .py extension) 
======= 
• purpose of Modules : for using the functions, classes methods defined in another file, in the current python file
We are having  3 types of modules in python 
1. User defined modules (we need to create these modules)
2. Internal modules ( During installation of python interpreter these modules 
will be installed on your machine))
3. External modules (We need to install these modules)  
"""
# In linux flavour operating systems ()
# =======================================
# module install
# python -m pip install module_name
# =======================================
# module upgrade
# python -m install --upgrade module_name
# ========================================

"""
Different ways to utilize modules
1. import module
2. from module_name import function
3. from module_name import function_1, function_2, ..., funcetion_n
4. from module_name as alias_name (or) short_name
5. from module_name import function as alias_name (or) short_function_name
6. from module_name import *
7. from directory_name import module_name 
8. from directory_name.module_name import function
9. from directory_name.module_name import function1, function2,... function_n
10. from directory_name.module_name import function_name as alias_name (or) short_name
11. from directory_name.module_name import function_names as alias_names (or) short_names
12. from directory_name.module_name import *  (all functions)
13. from directory_name.module_name import class_name
14. from directory_name.module_name import class_name1, class_name2, ...class_name_n
15. from directory_name.module_name import
 * (importing all class)
16. from directory_name.module_name import class_name as alias_name (or) short_name
17. from directory_name.module_name import class_names as alias_names (or) short_names
"""


""" 1.import module """
import Banglore

# Banglore.add(1,3)
# Banglore.sree()
# Banglore.abc(4,6,5,2)
# Banglore.printinfo(22,6,5,78,6,8,6,7,)

"""2. from module_name import function"""
from Banglore import printinfo

# printinfo(3,44,53,25,34,6)
# printinfo(10,80,74,90,37,90,67,77)
# printinfo(13,5,67,97,56,34)

"""3. from module_name import function_1, function_2, ..., funcetion_n"""
from Banglore import add, abc, sree


# add(33,77)
# add(10,100)
# add(99,11)
# abc(22,5,34,6)
# abc(11,55,7,9)
# sree()

# Providing alias name for the module
"""4. from module_name as alias_name (or) short_name"""
import Banglore as Bng

# Bng.sree()
# Bng.printinfo(44,6,4,7,8,45,6,7)
# Bng.add(1,9)


# Providing alias name for the function
"""5. from module_name import function as alias_name (or) short_function_name"""
from Banglore import printinfo as p

# p(1,2,54,3,7,4,2,5,)
# p(22,54,6,7,88,55,6,)

"""6. from module_name import *"""
# from Banglore import *

# printinfo(8,6,7,4,6,3,5,4,3)
# add(3,3)
# sree()

""" 7. from directory_name import module_name"""
from venella import Function_2naveenk

# Function_2naveenk.cal(4,5,4)
# Function_2naveenk.nvn(2,3,4,3,44,5,name ="naveen")
# Function_2naveenk.func_name(1,2,3,44,5,66,python ="language")

""" 8. from directory_name.module_name import function """
from venella.Function_2naveenk import cal

# cal(2,5,3)
# cal(4,8,2)
# nvn(11,55,6)

"""9. from directory_name.module_name import function1, function2,... function_n"""
# from venella.Function_2naveenk import cal,nvn

# cal(11,4,7)
# nvn(1,3,2,sunday ="funday")

"""10. from directory_name.module_name import function_name as alias_name (or) short_name"""
from subhash.Function_1naveen import print_me,genarate_email

# print_me(11,66,33)
# print_me(8,7,8)
# genarate_email("praveen", "kumar")
# genarate_email("naveen", "12143")

"""11. from directory_name.module_name import function_names as alias_names1, function_names as alias_names2"""
from subhash.Function_1naveen import print_me as p,genarate_email as gn

# p(6,4,7)
# p(6,5,2)
# gn("naveenkumar","smail3843")

""" 12. from directory_name.module_name import *  (importing all functions)"""
from subhash.Function_1naveen import *

# person_info("naveen",22)
# print_info(1.8,97,0,98,)
# print_my_info()
# sample_calculator(2,6,5,9,7)
# print_me(61,45,76)