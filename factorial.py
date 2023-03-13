# Finding the factorial of a number by taking user input:

# 5! 5x4x3x2x1  = 120   # 0! = 1

# number = int(input("Enter any desired number: \n "))
# factorial = 1
#
# if number < 0:
#     print('sorry! factorial cannot be calculated for negative numbers.')
# elif number == 0:
#     print('the factorial of 0 is 1.')
# else:
#     for i in range(1, number+1):
#         factorial = factorial * i
#     print(f'The factorial of {number} is { factorial }')


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        # fact *= i
    return fact

print(factorial(5))

a = []
for x in "banana":
    a.append(x)
print(a)


class Bank_application():
    def __init__(self):
        self.amount = 0
    def deposit(self, Amount):
        self.amount += Amount
        print('Amount successful deposit')
    def withdrawal(self, Amount):
        if(self.amount-Amount >= 500):
            self.amount -= Amount
            print("Amount successful Withdraw")
        else:
            print("insufficient account balance  /n you to keep at least Rs 500 in your account")
    def display(self):
        print("your bank balance is: ", self.amount)


a = Bank_application()
for i in range(0,30):
    print("1.deposit, 2.withdrawal, 3.display, 4.exit")
    x = int(input("Enter your choice:"))
    if (x==1):
        Amount = float(input("Enter Amount to be deposit:"))
        a.deposit(Amount)
    elif (x==2):
        Amount = float(input("Enter Amount to be withdrawal:"))
        a.withdrawal(Amount)
    elif(x==3):
        a.display()
    elif(x==4):
        exit()

    else:
        print("you have entered wrong values")
