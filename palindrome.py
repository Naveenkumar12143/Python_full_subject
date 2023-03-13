# Finding weather a data palindrome or not

# palindrome : like that  # 121, Madam , malayalam

data = input(" Enter the required the message or data :  \n ")
reverse = data[::-1]  # madam
if data == reverse:
    print(f"{data} is a palindrome")
else:
    print(f"{data} is not palindrome")


