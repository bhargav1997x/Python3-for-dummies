#Practical 27: Factorial of  N < 1000 using resursion

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * factorial(x-1))

value = int(input("Upto? "))
print(factorial(value))