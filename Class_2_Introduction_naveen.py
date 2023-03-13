__author__ = "Naveen kumar"

# Terminalogy:

# x = 10    # where x is variable or global variable

# def venkat(x):  # where x is an argument
#     pass

# class ramu(x):  # where x is an attribute
#     pass

# Overview of OOPS Terminology

"""
Class − A user-defined prototype for an object 
that defines a set of attributes that characterize any object of the class.
The attributes are data members (class variables and instance variables)and methods, accessed via dot notation.
Instance − An individual object of a certain class.
"""

"""
Class variable − A variable that is shared by all instances of a class.
Class variables are defined within a class but outside any of the class's methods. 
Class variables are not used as frequently as instance variables are.

                         (or)
class attributes :
=================
class attributes belong to the class itself, 
they will be shared by all the instances.
Such attributes are defined in the class body (usually at the top)

Data member/ instance variable:− Instance variable that holds data associated with a class and its objects.

"""

# How to use class variable inside method ==> b using class name

class Addition:
    count = 0
    def __init__(self):
        print('Hero')

    def raju(self):
        Addition.count += 1  # usage of class variable==> class_name.class_variable
        print("present count value :", Addition.count)

    def ravi(self):
        Addition.count += 9
        print("present count value :", Addition.count)


# add = Addition()
# print(add.count)
# print(id(add))

# add.raju()
# print(add.count)  # class attribute (count) was shared by 1st instance

# add.ravi()
# print(add.count)

"""class variable will be shared among all the instances created by the user"""
# a1 = Addition()
# print(a1.count)
# print(id(a1.count))

# a1.raju()
# print(a1.count)  # class attribute (count) was shared by 2nd instance also


# a1.ravi()
# print(a1.count)

# print(add.count)

"""

Object − A unique instance of a data structure that is defined by its class.
An object comprises both data members (class variables ) and methods.
"""


# Operator overloading − The assignment of more than one function to a particular operator.

class Honda:
    """ All Honda Cars and Cars price"""
    count = 6

    def __init__(self, name, model, price):
        """as soon as created the instance, this method will be executed"""
        self.name = name
        self.model = model
        self.price = price
        Honda.count += 1  # class_name.class_variable
        print("This is Honda company car:", Honda.count)
        print("name is {0} and car Model is {1}, {1} car price is {2}".format(name, model, price))

        # print("This is constructor method")
        # print("Once created instance automatically this method will execute")
        # print("how many times you will create new instance those many times this constructor
        # method will execute automatically")

    def displayName(self):
        print("This is Honda company car: ".format(Honda.count))
        print("Name :", self.name, "Model:", self.model, "price :", self.price)

    def displayBrand(self):
        print("Name :", self.name, "Model:", self.model, "price :", self.price)

    def display_price(self):
        print("Name :", self.name, "Model:", self.model, "price :", self.price)
        print("depending on model:", self.price)

        all_cars = ("city", "Amaze", "WR_V", "Jazz", "BR_V", "Mobilio", "CR_V", "Brio", "Civic")
        print(all_cars)


# company = Honda("Honda", "city", 1800000)
# company.displayName()
# print(company.count)

# car = Honda("Honda", "WR-V", 2100000)
# car.displayBrand()
# print(car.count)

# motorcars = Honda("Honda","Amaze",1350000)
# motorcars.display_price()
# print(motorcars.count)


# Note : company != car != motorcars
# different instances located in different memory location
# print(company)  # <__main__.Honda object at 0x000002006F643E80>
# print(car)  # <__main__.Honda object at 0x000002006F643D90>
# print(motorcars)  # <__main__.Honda object at 0x000002006F643D00>


def display_Details():
    print("Full details", Biodata.nvnCount)


class Biodata:
    nvnCount = 7

    def __init__(self, name, age, place, f_name, m_name):
        self.name = name
        self.age = age
        self.place = place
        self.f_name = f_name
        self.m_name = m_name
        Biodata.nvnCount += 3  # class_name.class_variable,
        print("ALL IS WELL NAVEEN")

    def Information(self):
        print("name:", self.name, "age:", self.age, "place:", self.place,
              "f_name:", self.f_name, "m_name:", self.m_name, Biodata.nvnCount)

        follow = ("Do hard work naveen.Always believe your self. No one can care your life."
                  "your life totally your responsibility")
        print(follow)


# " This would create first object of Employee class "

life = Biodata("Naveen", 22, "India", "Rangappa", "Pushpavathi")
display_Details()
print(life.nvnCount)

# Naveen = Biodata("Praveen", 26, "India", "Rangappa", "Pushpavathi")
# Naveen.Information()
# print(Naveen.nvnCount)


# Now, putting all the concepts together

class Employee:
    """ Common base class for all employees """
    empCount = 3

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



# This would create first object of Employee class
# emp1 = Employee("tom", 23000)

# This would create second object of Employee class
# emp2 = Employee("rohan", 25000)

# This would create second object of Employee class
# emp3 = Employee("bunny", 45000)

# emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()

# print(emp1.empCount)
# print("Total Employee ", Employee.empCount)

# You can add, remove, or modify attributes of classes and objects at any time

# emp1.age = 21  # Add an 'age' attribute.
# print(emp1.age)

# emp1.name = 'banu'  # Modify 'name' attribute.
# print(emp1.name)

# del emp1.salary  # Delete 'salary' attribute.
# print(emp1.salary)

# print("Employee 2 salary is : {}".format(emp2.salary))
# print(emp2.name)

# Instead of using the normal statements to access attributes, you can use the following functions −

class Employee:
    """Common base class for all employees"""
    empCount = 15
    tom = 20

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 5  # class_name.class_variable,
        print("__init__ method executed")

    def displayCount(self):
        print("Total Employee", Employee.empCount, Employee.tom)

    def displayEmployee(self):
        print(" Name : ", self.name, " Salary: ", self.salary)


# " This would create first object of Employee class "
# jhr = Employee("Rahul", 29000)

# This would create second object of Employee class"
# emp2 = Employee("john", 55000)

# jhr.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee ", Employee.empCount)

""" The hasattr(obj,name) − to check if an attribute exists or not."""
# print(hasattr(jhr, "salary"))
# print(hasattr(jhr, "name"))
# print(hasattr(jhr, "age"))

# jhr.age = 23
# print(jhr.age)

# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# two ways to add data to  the class objects.

###      Normal way 1        ###

# setattr(emp2, "name", "virender sehwag")
# print(emp2.name)

# setattr(emp2,"salary",74000)
# print(emp2.salary)

####    Advanced way 2         ###
# emp2.name = "santhosh"
# print(emp2.name)

# emp2.salary = 92000
# print(emp2.salary)

"""The getattr(obj, name[, default]) − to access the attribute of object """

# print(jhr.salary)
# print(getattr(jhr ,"salary"))
# print(getattr(emp2,"name"))

""" The delattr(obj, name) − to delete an attribute."""
# delattr(jhr,"salary")
# print(delattr(jhr,"salary"))
# print(hasattr(emp2, 'salary'))   # Returns true if 'salary' attribute exists

"""we in previous steps we have deleted salary attribute, so displaying result as False """
# setattr(emp2, 'salary', 70000) # Set attribute 'salary' at 70000
# s = getattr(emp2, 'salary')    # Returns value of 'salary' attribute
# print(s)
# print(emp2.salary)
# delattr(emp2, 'salary')  # Delete attribute 'salary'
# print(hasattr(emp2, 'salary'))#o access all these attributes −



class Sample:
    def __init__(self):
        print("let see")


obj = Sample()