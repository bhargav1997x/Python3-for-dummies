#Practical 13: Generate N prime numbers

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if n % i == 0:
                status = False
    return status

value = input("Number Upto? ")
for n in range(1, value):
    if is_prime(n):
        if n == value:
            print n
        else:
            print n, ",",

