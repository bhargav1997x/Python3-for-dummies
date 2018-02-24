#Matrix multiplication
import numpy.matlib
import numpy as np

print('Get transpose of 3×3 dimension')
print('enter elements for matrix')
m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        m1[x][y] = int(input())

mm1 = np.asmatrix(m1)

print('This is first matrix')
print(mm1)
mt1 = mm1.transpose()
print('transpose of matrix')
print(mt1)
