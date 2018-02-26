#Practical 22: Factors of number

value = int(input("Number? "))
factor = []
for i in range(1, value):
    if(value % i) == 0:
        factor.append(i)

print(factor)
