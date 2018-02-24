#add two matrices
import numpy.matlib
import numpy as np


def getm(numb):  # function to take input of matrix as list
    for l in range(0, 9):
        a = input()
        a = int(a)
        numb.append(a)
    return


def makem(m):  # function to convert list to matrix
    i = j = k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                m[[i], [j]] = numb[k]
    return


print('Add two matrices')
print('enter data for first matrix')
numb = []
getm(numb)
m = np.matlib.ones((3, 3))
makem(m)
m1 = m  # matrix 1

print('enter data for second matrix')
numb = []
getm(numb)
m = np.matlib.ones((3, 3))
makem(m)
m2 = m  # matrix 2

print('This is first matrix')
print(m1)
print('This is second matrix')
print(m2)
summ = np.add(m1, m2)  # sum of matrix
print('Addition of matrices')
print(summ)
