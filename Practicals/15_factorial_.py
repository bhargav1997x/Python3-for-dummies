#Practical 15: Find factorial of number

def getFactorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * getFactorial(n - 1))

value = input("Enter a number: ")
print(getFactorial(value))
