# a = 'siva'
# print(a)
#
# _2a = "naveen"
# print(_2a)

# a = [2,1,2,4,5,4,3]
# b = a
# print(a)
# print(set(b))
# print(ord(b))
# b = a
# print(list(set(a)))


# h = []
# for i in b:
#     print(i.unique())


# l = [2,1,2,4,5,4,3]
# print("Original List: ", l)
# res = [*set(l)]
# print("List after removing duplicate elements: ", res)

test_list = [2,1,2,4,5,4,3]
print("The original list is : "
      + str(test_list))

# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]

# printing list after removal
print("The list after removing duplicates : "
      + str(res))

a = [2,1,2,4,5,4,3]
print(str(a))

res = []
[res.append(x)for x in a if x not in res]
print(res)

# a = 'rejiayuaeoiusaeuei'
#
# for i in a:
#     if i in 'aeiou':
#         print(i, end =" ")


n = 'naveenkumar,praveenkumar'

print(* {i for i in n if i in 'aeiou'} )

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(6))

sentance = "fhksdUeierwb,bsdAhkdeOsuew"

print(*[i for i in sentance if i in 'aeiouAEIOU'])

for letter in sentance:
    if letter in 'aeiouAEIOU':
        print(letter, end=" ")

a,b = 0,1
for i in range(0,5):
    print(a)
    a,b = b, a +b
