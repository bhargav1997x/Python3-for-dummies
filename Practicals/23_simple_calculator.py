#Practial 23: Simple calculator


def compute(x, _a, _b):
    return {
        1: _a + _b,
        2: _a * _b,
        3: _a / _b,
        4: _a - _b
        #5: _a ** _b,
        #6: _a % _b
    }.get(x, 1)

choice = int(input("1. Addition \n2.Multiplication \n3.Division \n4.Subtraction: "))
operand_1 = int(input("Operand 1 value: "))
operand_2 = int(input("Operand 2 value: "))

if operand_2 == 0 and choice == 3:
    print("enter non-zero value")
print(compute(choice, operand_1, operand_2))
