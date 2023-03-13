# &&&&&&& List Comprehension &&&&&
"""Description
You are given an integer 'n' as the input. Create a list comprehension containing the squares of the
integers from 1 till n^2 (including 1 and n), and print the list.
For example, if the input is 4, the output should be a list as follows:
[1, 4, 9, 16]
The input integer 'n' is stored in the variable 'n'. """
import ast, sys
# n = int(input())
# Write your code here (remember to print the list)
# ==>way1
# print([n ** 2 for n in range(1,5)])

# ==> way2
# final_list = [n**2 for n in range(1,n+1)]
# print(final_list)

# ==> way2 Using for loop
# list = []
# for n in range(1,5):
#     list.append(n**2)
# print(list)

# &&&&&&& List Comprehensions &&&&&&&&&
"""Description
Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria]
using list comprehensions.
Sample Input:
['wood','old','apple','big','item','euphoria']
Sample Output:
['old', 'apple', 'item', 'euphoria'] """

# import ast,sys
# input_str = sys.stdin.read()
# input_list = ast.literal_eval(input_str)
# list_vowel = [input_list for input_list in input_list if input_list[0] in 'aeiou']
# print(list_vowel)

# &&&&&& Dictionary Comprehension &&&&&&&
# d = {x.upper(): x*3 for x in 'acbd'}
# print(d)  # {'A': 'aaa', 'C': 'ccc', 'B': 'bbb', 'D': 'ddd'}

"""Following is the code to create a dictionary where the keys are multiples of 3 among 
the first 100 natural numbers and each value is the cube of the key."""

input_list = list(range(1,100))
output_dict = {}

for val in input_list:
    if val % 3 == 0:
        output_dict[val] = val**3
"Now, what would be corresponding dictionary comprehension for the code involved in dictionary creation? "
# output_dict= {val : val**3 for val in input_list if val % 3 == 0}

" What will the output of the following code be?"
# print([i+j for i in "abc" for j in "def"])  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# def func(x, y):
#     z = x * y + x + y
#
# func(2)
# lst = [10,22,44,55,66,77,22,33,44,10,22,44,55,66,22,33,44,55,77,89]
# print(lst.uniqe())
# ^^^^^^^^^^ All built in Methods ^^^^^^^^^^^^

print("All method of List :", [i for i in dir(list) if "__" not in i])


print("All method of set :", [i for i in dir(set) if "__" not in i])


print("All method of tuple :", [i for i in dir(tuple) if "__" not in i])


print("All method of dict :", [i for i in dir(dict) if "__" not in i])

