#Practical 16: Multiplication table

choice = input("1. Range table \n2. Single table: ")

if choice == 1:
    value = input('Upto? ')

    for j in range(1, value + 1):
        for i in range(1, 11):
            print(j * i)
        print("**********************\t")

else:
    value = input("Show table of: ")
    for i in range(1, 11):
            print(value * i)
