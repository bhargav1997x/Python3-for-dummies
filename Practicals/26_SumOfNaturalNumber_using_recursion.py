#Practical 26: Sum of natural numbers using recursion

def sumOfNatural(x):
    if x == 1:
        return 1
    else:
        return (x + sumOfNatural(x-1))

value = int(input("Upto? "))
print(sumOfNatural(value))