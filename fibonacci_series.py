# Fibanacci serires 1 st way
# 0,1,1,2,3,5,8,13


number = int(input("Enter the desired number for the fibonacci series: \n "))
n1, n2 = 0, 1
my_sum = 0

for i in range(number):
    print(my_sum, end=' ')
    n1 = n2
    n2 = my_sum
    my_sum = n1 + n2

# Fibanacci serires 2 way

a, b = 0,1
for i in range(0, 5):
    print(a)
    a,b= b, a+b

n = int(input(" Enter a Number: "))

if n% 2== 1:
    print('not a prime')
else:
    print('prime')
