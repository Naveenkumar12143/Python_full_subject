__author__ = "Naveen kumar"
import random
from random import randint,choice



"""
randint() is an inbuilt function of the random module in Python3.
Syntax : randint(start, end)
Parameters :
(start, end) : Both of them must be integer type values.
Returns :
A random integer within the given range as parameters.
Errors and Exceptions :

ValueError : Returns a ValueError when floating
             point values are passed as parameters.

TypeError : Returns a TypeError when anything other than
            numeric values are passed as parameters.
"""

# # Generates a random number between

# r1 = randint(x,y)  # a given positive range
# print("Random number between {} and {} is {}".format(x, y, r1))
# Random number between 50 and 100 is 63
# Generates a random number between

n2 = randint(-15,-1)
x = 50
y = 100
# print("Random number between -15 and -1 is {}".format(n2))
# Random number between -15 and -1 is -6

# Generates a random number between
# a = randint(-20,5)
# print("Random number between -20 and 5 is {}".format(a))
# Random number between -20 and 5 is 4
# Generates a random number between

# Code #2 : Program demonstrating the ValueError.
# # imports random module

'''If we pass floating point values as
parameters in the randint() function'''


# r1 =randint(1.5, 9.3)
# print(r1)

# Output : ValueError: non-integer arg 1 for randrange()

# Traceback (most recent call last):
#   File "C:\Users\HP\Desktop\important\random_module_naveen.py", line 47, in <module>
#     r1 =randint(1.5, 9.3)
#   File "C:\Users\HP\AppData\Local\Programs\Python\Python310\lib\random.py", line 370, in randint
#     return self.randrange(a, b+1)
#   File "C:\Users\HP\AppData\Local\Programs\Python\Python310\lib\random.py", line 309, in randrange
#     raise ValueError("non-integer arg 1 for randrange()")
# ValueError: non-integer arg 1 for randrange()

# Code #3 : Program demonstrating the TypeError


'''If we pass string or character literals as
parameters in the randint() function'''

# z = random.randint(5,'nvn')
# print(z)

# output :
# Traceback (most recent call last):
#   File "C:\Users\HP\Desktop\important\random_module_naveen.py", line 66, in <module>
#     z = random.randint(5,'nvn')
#   File "C:\Users\HP\AppData\Local\Programs\Python\Python310\lib\random.py", line 370, in randint
#     return self.randrange(a, b+1)
# TypeError: can only concatenate str (not "int") to str

# importing randint function

# from random import randint
# print(randint(5, 33))
# print(randint(-20, -1))
# print(randint(-5, 25))
#

# Function which generates a new
# random number everytime it executes
# Applications :
#
# The randint() function can be used to simulate a lucky draw situation.
# print(range(8))

def rand_int_generator(start_val, end_val, num_of_vals):
    random_numbers_list = []
    for element in range(num_of_vals):
        try:
            result = randint(start_val, end_val)
            random_numbers_list.append(result)  # all the required random values will append to single list
        except Exception as error_info:
            print(error_info)
    return random_numbers_list

# print(rand_int_generator(1, 25, 5))


def rand_int_generator(start_val, end_val, num_of_vals):

    """
    :param start_val: should provide staring integer value
    :param end_val:should provide ending integer value
    :param num_of_vals: how many values you want
    :return: Will generate list of random integer values, for the provided range of a, b
    """
    random_numbers_list = []
    for element in range(num_of_vals):
        try:
            result = randint(start_val, end_val)
            random_numbers_list.append(result)  # all the required random values will append to single list
        except Exception as error_info:
            print(error_info)
    return random_numbers_list


# random_numbers_list  = rand_int_generator(1, 50, 10)
# print(random_numbers_list)


# print("Naveen,Rana and Sai")

# Function takes user input and returns
# true or false depending whether the
# user wins the lucky draw!
"""
Let’s say User has participated in a lucky draw competition. 
The user gets three chances to guess the number between 1 and 10. 
If guess is correct user wins, else loses the competition."""

def rand_guess():
    """
    True :
          If win-condition is satisfied then,  the function rand_guess returns True
    False:
          If user's choice doesn't match,  win-condition then it is printed
    :return:  this function returns True or False
    """
    # calls generator() which returns a random integer between 1 and 10
    random_number = randint(1, 10)
    # defining the number of guesses the user gets
    guess_left = 2
    # Setting a flag variable to check the win-condition for user
    flag = 0
    # looping the number of times the user gets chances
    while guess_left > 0:
        # Taking a input from the user
        guess = int(input("Pick your number to enter the lucky draw\n"))
        # checking whether user's guess matches the generated win-condition
        if guess == random_number:
            # setting flag as 1 if user guessses  correctly and then loop is broken
            flag = 1
            break
        else:
            # If user's choice doesn't match, win-condition then it is printed
            print("Wrong Guess!!")
        #         # Decrementing number of guesses left by 1
        guess_left -= 1  # guess_left = guess_left  - 1 ( assignment operator)
    # If win-condition is satisfied then, the function rand_guess returns True
    if flag == 1:
        return True
    # Else the function returns False
    else:
        return False


# if __name__ == '__main__':
#     if rand_guess():
#         print("Congrats!! You Win.")
#     else:
#         print("Sorry, You Lost!")

# Output :

# Pick your number to enter the lucky draw
# 4
# Wrong Guess!!
# Pick your number to enter the lucky draw
# 9
# Congrats!! You Win.
