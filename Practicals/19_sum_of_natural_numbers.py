#Practical 19:  Sum of natural numbers

value = int(input("upto? "))
sum = 0
for i in range(1, value):
    sum = value * (value + 1) / 2
print(sum)
