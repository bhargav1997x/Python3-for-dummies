#Practical 32: Check palindrome of string

value = input("Enter string: ")
temp = value[::-1]

if value == temp:
    print("Palindrome 1")
else:
    print("Not Palindrome -1")