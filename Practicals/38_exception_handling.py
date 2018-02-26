#Pratical 38: Program to handle exceptions

value_1 = int(input("1st value: "))
value_2 = int(input("2nd value: "))
try:
    value_1 //= value_2
except Exception:
    value_1 = 'NULL'
    print("Can't divide with zero")
else:
    print("no errors: printing ")
finally:
    print(value_1, "\n")
