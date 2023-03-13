# ******* Prime Numbers *********

# num = 20
# count = 0

# if num > 1:
#     for i in range(1, num+1):
#         if (num%i) == 0:
#             count = count + 1
#         if count == 2:
#             print("Number is prime")
#         else:
#             print("Number is not prime")


# ******* Prime Numbers *********
# n = int(input("enter a number: \n"))
#
# if n % 2 == 0:
#     print(" not prime ")
# else:
#     print("prime")

# ******* Prime Numbers *********


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
print(factorial(3))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        # fact *= i
    return fact

print(factorial(5))

n = int(input("Enter a desired number: \n"))
# a,b = 0,1
for i in range(1,n+1):
    print(a)
    a,b = b, a+b