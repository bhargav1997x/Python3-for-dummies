#Practical 29: Addition of two matrices

matrix_1 = []
matrix_2 = []

value = int(input("Matrix dimension: "))

print("Enter value of matrix 1: ")
for i in range(0,value):
    for j in range(0, value):
        matrix_1[i][j] = input()

print("Enter value of matrix 2: ")
for i in range(0,value):
    for j in range(0, value):
        matrix_2[i][j] = input()

for i in range(0, value):
    for j in range(0, value):
        matrix_1 += matrix_2
    print("\n")

print(matrix_1)