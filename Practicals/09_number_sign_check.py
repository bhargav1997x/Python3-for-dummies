#Practical 9: Program to check number os positive, negative or zero

value = input("Enter a value: ")

value = int (value)
if value < 0:
    print("Number is Negative\n")
elif value > 0:
    print("Number is Positive\n")
else:
    print("Number is zero\n")