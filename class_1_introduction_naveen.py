__author__ = "Naveen kumar"
x = 10   # variable

def num(x=10):
    x = 10  # argument

class Naveen:
    x = 32  # attribute


# print(type(x))

y = []
print(type(y))

"""
To understand the oops concept, we have to understand following concepts
1. what is class ?
    Ans: Class is nothing but just blue-print.There is no use of class definition,
        until unless you have created the instance/object for the particular class.

2. what are the extra advantages of classes compared with functions?
    Ans: 1. Grouping of function in the form of methods, provided with specific class name.
         2. we can inherit the class into another class
         3. we can perform multiple class related properties (Data hiding/ Data abstraction/ method overriding/encapsulation...)  
3. Difference between method and function ?
    Ans: Function which is defined inside of the class is a method.
         Function which is defined outside of the class is a Function.
4. what is Constructor method (def __init__(self)) ?

    Ans: Constructor method (def __init__(self)) is a special kind of method,
         as soon as you have created an object/ instance for the class then
          automatically ___init__ method will be executed, without calling it
5. How many instances/objects we can create for a class?
    N number of instances/ objects we can create for  a single class.
6. What is self ?

7. what is the difference between class variable and instance variable.
    class variables will be shared among the multiple instances of the same class. but  
instance variables will not be not be shared.

 ( or )
What is the difference between the class variable and instance variable?
Ans:  Class variables can use in all instances of the same class created by the user.

class variables, which have the same value across all class instances (i.e., static variables)
Instance variables can use only for the same instance.
Instance variables are owned by instances of the class. 
this means that for each object or instance of a class, the instance variables are different.

Ø  Class variable will be shared among the multiple instances of the class.
Ø  But instance variable will be independent.
Ø  Class variables are defined within the class but outside of the class method.
Ø  Class variables are not used as frequently as an instance variables. 
"""

class Naveen:
    w = 10
    def __init__(self):
        print("rohith")
        print("gayatri")

    def vineela(self):
        print("vineela & subhash")

obj = Naveen()  # We need to created object
print(obj)
print(id(obj))
# n = Naveen
# print(id(n))
# print(obj.w)
# print(n.w)

class Bike:
   s = 45
   def __init__(self, name, number):
       self.name = name
       self.number = number
       print("This was printed , because of you have created object for this class")
       print("This vehicle Name is {0} and vehicle Number is {1}".format(name, number))
   def abc(self):
       print("python")


# q = Bike("Honda shine", "AP002354")  # We need to created object
# print(q.s)
# print(q.name)
# print(q.number)
# print(id(q))

# z = Bike("Honda shine", "AP002354")
# print(z.s)
# print(z.name)
# print(z.number)
# print(id(z))
# q.name = "bike"
# print(q.name)


""" We can add variables to the class from outside by using instance """

# q.game = "cricket"
# q.role = "right arm batsman"
# q.bowler = "right arm off spin"
# print(q.game, '\n', q.role, '\n', q.bowler)

"""
Result:
=======
his was printed , because of you have created object for this class
This vehicle Name is Honda shine and vehicle Number is AP002354
cricket 
 right arm batsman 
 right arm off spin
 
after created an object, we can also access variables with that object
Ex:
q.name
"""

class Employee_nvn:
    def __init__(self, EmpId, Expe, sal, Level, Rating):
        self.EmpID = EmpId
        self.Expe = Expe
        self.Level = Level
        self.Rating = Rating
        if(Expe == 1 and Level == "c1" and  Rating == "superstar" ):
            print(" Hike is 25%,Salary after increment",((.25*sal)+sal))
        elif(Expe == 1 and Level == "c1" and Rating == "star" ):
            print(" Hike is 20%,Salary after increment",((.20*sal)+sal))
        elif(Expe == 1 and Level == "c1" and Rating == "pillor" ):
            print(" Hike is 15%,Salary after increment",((.15*sal)+sal))
        elif(Expe == 1 and Level == "c1" and Rating == "below expectations" ):
            print(" Hike is 9%,Salary after increment",((.10*sal)+sal))

        elif((Expe == (2 or 3)) and Level == "c2" and  Rating == "superstar" ):
            print(" Hike is 18%,Salary after increment",((.18*sal)+sal))
        elif((Expe == (2 or 3)) and Level == "c2" and Rating == "star" ):
            print(" Hike is 15%,Salary after increment",((.15*sal)+sal))
        elif((Expe == (2 or 3)) and Level == "c2" and Rating == "pillor" ):
            print(" Hike is 10%,Salary after increment",((.10*sal)+sal))
        elif((Expe == (2 or 3)) and Level == "c2" and Rating == "below expectations" ):
            print(" Hike is 8%,Salary after increment",((.08*sal)+sal))

        elif(Expe == (4 or 5 or 6) and Level == "c3" and  Rating == "superstar" ):
            print(" Hike is 15%,Salary after increment",((.15*sal)+sal))
        elif(Expe == (4 or 5 or 6) and Level == "c3" and Rating == "star" ):
            print(" Hike is 12%,Salary after increment",((.12*sal)+sal))
        elif(Expe == (4 or 5 or 6) and Level == "c3" and Rating == "pillor" ):
            print(" Hike is 8%,Salary after increment",((.08*sal)+sal))
        elif(Expe == (4 or 5 or 6) and Level == "c3" and Rating == "below expectations" ):
            print(" Hike is 6%,Salary after increment",((.06*sal)+sal))

        elif(Expe == (7 or 8 or 9) and Level == ("c4" or "c5")  and  Rating == "superstar" ):
            print(" Hike is 13%,Salary after increment",((.13*sal)+sal))
        elif(Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "star" ):
            print(" Hike is 9%,Salary after increment",((.09*sal)+sal))
        elif(Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "pillor" ):
            print(" Hike is 7%,Salary after increment",((.07*sal)+sal))
        elif(Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "below expectations" ):
            print(" Hike is 5%,Salary after increment",((.05*sal)+sal))

        elif(Expe >=10 and Level == ("c6" or "c7")  and  Rating == "superstar" ):
            print(" Hike is 10%,Salary after increment", ((.10*sal)+sal))
        elif(Expe >=10 and Level == ("c6" or "c7") and Rating == "star" ):
            print(" Hike is 7%,Salary after increment", ((.07*sal)+sal))
        elif(Expe >=10 and Level == ("c6" or "c7") and Rating == "pillor" ):
            print(" Hike is 5%,Salary after increment", ((.05*sal)+sal))
        elif(Expe >=10 and Level == ("c6" or "c7") and Rating == "below expectations" ):
            print(" Hike is 3%,Salary after increment", ((.03*sal)+sal))

        else:
            print("given values are not match")



# v = Employee_nvn("HM0002165",2,34000,"c2","star")
# v = Employee_nvn("MNT000253",4,36000,"c3","superstar")
# print(v.EmpID)
# print(v.Level)

"""
We can create many instances for the same class but Each instance is an independent of other instance.
  (i.e when we have created a new instance, it will be created in a new memory location)
"""

# b = Employee_nvn("HM0001669",4,40000,"c3","superstar")
# print(b.EmpID)
# print(b.Level)
# z = Employee_nvn("HM0001669",4,140000,"c5","superstar")

"""
"pass" keyword (a statement) to indicate that nothing happens—the function/class/conditional statements
looping statement is empty.With pass, we indicate a "null" block.
Pass can be placed on the same line, or on a separate line. Pass can be used to quickly add things
 that are unimplemented."""

# class jeevan:
#     pass

# class Vijaya:
# 	def ravi(self):
# 		pass
