#Practical 6: Prgram to swap 2 variables

x = input("X:- ")
y = input("Y:- ")
choice = input("1. With temp variable \n2. Without temp variable")

if choice == 1:
    #With temporary variable
    x = x + y
    y = x - y
    x = x - y
else:
    #without temporary variable
    x = x * y
    y = x / y
    x = x / y

print("X: ", x,"Y:", y)
