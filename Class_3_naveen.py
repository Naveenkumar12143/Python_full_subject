__author__ = "Naveen kumar"

"""
Destroying Objects (Garbage Collection)
Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space.
The process by which Python periodically reclaims blocks of memory that no longer are in use is termed as Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero.
An object's reference count changes as the number of aliases that point to it changes.

An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases when it is deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically.
"""

a = 90      # Create object <40>
b = a       # Increase ref. count  of <90>
c = [b]     # Increase ref. count  of <90>


# del a   # Decrease ref. count  of <40>
# print(b)
# print(c)



"""You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space.
 However, a class can implement the special method __del__(), called a destructor, 
 that is invoked when the instance is about to be destroyed. 
 This method might be used to clean up any non-memory resources used by an instance.
"""

class Ramu:
    def __init__(self, s=5, u=10):
        self.s = s
        self.u = u
        print("JAI HIND")
    def __del__(self):
        n = self.__class__.__name__
        print(n, "destroyed")


# rp = Ramu()
# print(rp)
# hr = rp
# print(hr)
# a1 = rp
# print(id(rp), id(hr), id(a1))  # prints the ids of the object
# del rp
# del hr
# del a1
# print(id(rp), id(hr), id(a1))

"""
When the above code is executed, it produces the following result −

2082446753744 2082446753744 2082446753744
Ramu destroyed
Note − Ideally, you should define your classes in a separate file, then you should import them in your main program 
file using import statement.
In the above example, assuming definition of a Ramu class is contained in "point.py" and there is no other
executable code in it.
"""
# #################    Class Inheritance  #################

"""
# Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.

or

Instead of starting from a scratch, you can create a class by deriving it from a pre-existing class
by writing the parent class name in parentheses after the new_class_name.

The child class inherits the attributes of its parent class, and you can use those attributes as if they were defined
in the child class. 
A child class can also override data members and methods from the parent.

Syntax
Derived classes are declared much like their parent class; however, 
a list of base classes to inherit from is given after the class name −

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite

"""
#  @@@@@@@@   Single Inheritance       @@@@@@@@

class Rangappa:   # define parent class
    parentcount = 4  # class variable

    def __init__(self):
        print("calling parents Family ")

    def parentlove(self):
        print("Taking parent Family love ")

    def Win(self, count):
        Rangappa.parentcount += count

    def Loss(self):
        print("parentcount :", Rangappa.parentcount)

    def Tree(self):
        print("praveen")
        print("Nani")


object = Rangappa()  # obj/instance creation
print(object.parentcount)
object.parentlove()
object.Win(6)
object.Loss()
object.Tree()


class Naveen(Rangappa):
    def __init__(self):
        print("calling child class")
    def Naveen_method(self):
        print('calling child method')


babu = Naveen()  # instance of child  ==> immediately child's init method will be executed
babu.Tree() # again call parent's method
# babu.Naveen_method() # child calls its method
# babu.Loss()  # again call parent's method
# babu.win(7)  # again call parent's method
object.Tree()


"""
When the above code is executed, it produces the following result −

Calling child constructor
Calling parent method
Calling child method
"""

"""
In a similar way, you can drive a class from multiple parent classes as follows −

class A:        # define your class A
.....

class B:         # define your class B
.....

class C(A, B):   # subclass of A and B
.....
"""
#    ******** Multiple Inheritance  ********

class Chess:
    def __init__(self):
        print(" chess is a mind game ")

class Cricket:
    def __init__(self):
        print(" cricket is a outdoor  game")

    def players(self):
        print("each team have 11 players")

class kabadi:
    def stars(self):
        print("kabadi is a very interesting game")
    def happiness(self):
        print("when i play games my happiness*** is unlimited")


class Games(Chess, Cricket, kabadi):
    gain = 99999999999999999999
    def __init__(self):
        Games.gain += 1
        print("play games then enjoy ur life :", Games.gain)

    def fitness(self):
        print("do work exercise improve your fitness and practice leve ")



# naveen = Games()
# naveen.stars()
# naveen.players()
# naveen.happiness()
# naveen.fitness()


"""
You can use is-subclass() or isinstance() functions to check a relationships of two classes and instances.
The is-subclass(sub, sup) boolean function returns True, if the given subclass sub is indeed a subclass of the super
class sup.The isinstance(obj, Class) boolean function returns True, if obj is an instance of class Class or is 
"""

############# multi-level inheritance #############

class Vegtable():
    def carrot(self):
        print("called carrot method available in vegetables class")

class Nonveg(Vegtable):
    def meet(self):
        print("called meet method available in non-veg class ")


class Groundnut(Nonveg):
    def seeds(self):
        print("called meet method available in groundnut class")


class Food(Groundnut):
    def all(self):
        print("called meet method available in all********** class")
        print("rice")
        print("rooty")


# eat = Food()
# eat.all()
# eat.seeds()
# eat.carrot()
# eat.meet()

########## Hierarchical inheritance  #########

class Narendra():
    def knowledge(self):
        print("knowledge gives more confidence by")
        print("books")
        print("friends")
        print("parents")
        print("teachers")
        print("games and so many,,")



class Naveen(Narendra):
    def software(self):
        print("now i am learning python language through Narendra sir")


class Rohit(Narendra):
    def student(self):
        print("calling student method")


class Vineela(Narendra):
    def best(self):
        print("Naveen kumar is best student for my python batch")


class subhash(Narendra):
    def __init__(self):
        print("we are all are Narendra sir students")
    def elder(self):
        print("He is elder brother in my batch")


# sir = subhash()
# narendra = Naveen()
# Boyana = Rohit()
# student = Vineela()

# sir.elder()
# sir.knowledge()

# narendra.software()
# narendra.knowledge()

# Boyina.student()
# Boyina.knowledge()

# student.best()
# student.knowledge()





#       &&&&&&&& Hybrid inheritance &&&&&&&&&

class India():
    def __init__(self):
        print("we love India")
    def Newdelhi(self):
        print("our capital is new delhi")

class Banglore(India):
    def Ka(self):
        print("Bangalore city is a Huge traffic city in the india")

class Hydrabad(Banglore):
    def Ap(self):
        print("few years back hydrabad is ap capital")

class Earth(Hydrabad,India):
    def people(self):
        print("peoples always learning new thing in this generation")


# living = Earth()
# living.Newdelhi()
# living.Ka()
# living.Ap()

'''
How to check if a class is subclass of another?
Python provides a function issubclass() that directly tells us if a class is subclass of another class
'''


# Python example to check if a class is
# subclass of another

class Base():
    pass  # Empty Class


class Derived(Base):
    pass  # Empty Class


# Driver Code
# print(issubclass(Derived, Base))
# print(issubclass(Base, Derived))

# b = Base()
# d = Derived()

#
# b is not an instance of Derived
# print(isinstance(b, Derived))

# # But d is an instance of Base

# print(isinstance(d, Base))


# Overriding Methods
# You can always override your parent class methods.
# One reason for overriding parent's methods is that you may want special or different functionality in your subclass.
# Example
# """


class India():
    pass  # Empty Class

class Earth(India):
    pass  # Empty Class



# print(issubclass(Earth,India))
# print(issubclass(India,Earth))

# s = India()
# n = Earth()

# s is not instance of Earth
# print(isinstance(s,India))

# but n is instance of India
# print(isinstance(n,Earth))

# =========== Method overriding (local priority)============================


class Parent():
    x = 4  # class variable / attribute
    def __init__(self):
        self.y = 5  # when user created instance automatically y value automatically
        print("subhashini")
    def get_value(self):
        return Parent.x
    def chandrika(self):
       print("chandrika")

class Child(Parent):  # single inheritance
    def get_value(self):
        return Parent.x + 1

# c = Child()
# print(c.get_value())  # calling function will be replaced with it's return value
# c.chandrika()
# print(c.chandrika())

"""
# == == == == == =  Data hiding & Abstraction= == == == == == == == == == == == == ==
Example
Data Hiding (We can able to hide variable & methods)
An object's attributes may or may not be visible outside the class definition.

You need to name attributes with a double underscore prefix, and those attributes
then will not be directly visible to outsiders.

# Example
#!/usr/bin/python3
"""

class Rain:
    wed = 9   # attribute
    __thinking = 0  # hide attribute

    def __jhon(self):
        Rain.__thinking +=1
        print(Rain.__thinking)
        # self.__thinking +=1
        # print(self.__thinking)

    def flowing(self):
        Rain.__jhon(self)
        print("flowing")

# joy = Rain()  # created instance for the class
# print(joy.wed)  # called class attribute
# print("flowing")  # called class method

# print(joy.__thinking)   # gives an error
# print(joy.__jhon())  # unable to see the hided method or hided object


# print(joy._Rain__thinking)  # hided variable taken out
# print(joy._Rain__jhon())  # hided method taken out

""" If user wants to see hided objects & methods, see below code:"""
"""
Syntax for data abstaction:
attribute abstaction 
instance.singleUnderscoreClassNameDoubleUnderscoreAttributeName
Method abstaction 
instance.singleUnderscoreClassNameDoubleUnderscoreMethodName
"""

# Note: super()
"""
Python Super() Function
Super function allows us to call a same method which is available in the parent class."""

class Rangappa:
    pushpavathi = 459
    def method_1(self):
        print("this is method_1")

    def abc(self):
        print("this is abc method")

class Naveen(Rangappa):

    def method_3(self):
        print("this is method_3 ")

    def method_4(self):
        Naveen.method_3(self)  # by using class name you can utilize same class related methods
        print("this is method_4 ")

    def method_2(self):
        super().abc()  # Accessing parent class methods in child class method  by using super keyword
        print(super().pushpavathi)  # accessing parent class attributes in child class method by using super keyword
        # Rangappa.method_1(self)
        print("this is method_2")

# nani = Naveen()
# nani.method_1()
# nani.abc()
# nani.method_3()
# nani.method_2()

"""
Polymorphism means that different types respond to the same function.
Polymorphism is very useful as it makes programming more resulting  and therefore easier.
the same function is defined on objects of different types.
"""

"""
__add__
x + y resolves to x.__add__(y)

5 + 4
9
one = 4
one.__and__(5)
4

Any object that implements the __add__ function will work with the <object> + x syntax.

__contains__
__contains__ is the built in protocol for membership.

x in y resolves to y.__contains__(x)
When the interpreter encounters ‘b’ in [‘a’, ‘b’] it knows to look for the __contains__ function on the object to the right of in and pass it the object to the left of in as parameter.

A list object has that function defined and the interpreter then executes the corresponding code block.

All data structures have the concept of membership defined:

>>> 'b' in ['a', 'b']
True
>>> 'b' in ('a', 'b')
True
>>> 'b' in {'a': 1, 'b': 2}
True
>>> 'b' in {'a', 'b'}
True
Demonstrating __contains__:

>>> ['a', 'b'].__contains__('b')
True
>>> ('a', 'b').__contains__('b')
True
>>> {'a': 1, 'b': 2}.__contains__('b')
True
>>> {'a', 'b'}.__contains__('b')
True
Any object that implements the __contains__ function will work with the x in <object> syntax.

__iter__
__iter__ is how iteration is implemented in Python. This protocol is a bit more involved than the previous protocols.

Taking this code:

>>> number = [1, 2]
>>> for i in [1, 2]:
...     print(i)
...
1
2
Roughly here is the sequence of events: * interpreter calls __iter__ on the list object, * an object of type iterator is returned. * interpreter then calls __next__ repeatedly on the iterator * interpreter actions the code in the for loop * interpreter interrupts the loop if a StopIteration Exception occurs.

To illustrate:

>>> itr_obj = [1, 2].__iter__()
>>> type(itr_obj)
<class 'list_iterator'>
>>> itr_obj.__next__()
1
>>> itr_obj.__next__()
2
>>> itr_obj.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
Any object that implements the __iter__ function will work with the for x in <object>: ... syntax.

"""
