#add two matrices
import numpy.matlib
import numpy as np

print('Add two matrices of 3×3 dimension')
print('enter elements for first matrix')
m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        m1[x][y] = int(input())

mm1 = np.asmatrix(m1)

print('enter elements for second matrix')
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        m2[x][y] = int(input())

mm2 = np.asmatrix(m2)
print('This is first matrix')
print(mm1)
print('This is second matrix')
print(mm2)
summ = mm1+mm2  # Addition of matrix
print('sum of matrices')
print(summ)
