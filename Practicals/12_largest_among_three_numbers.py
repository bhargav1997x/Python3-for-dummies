#Practical 12: Largest among three numbers

value = [-1, 0, 1]

value[0] = input("Enter three numbers: ")
value[1] = input()
value[2] = input()

value[0] = int(value[0])
value[1] = int(value[1])
value[2] = int(value[2])

max = 0
for i in range(0, 3):
    if(int(max) < value[i]):
        max = value[i]
print("Max value is: ", max)
