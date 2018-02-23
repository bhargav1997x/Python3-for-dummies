#Practical 31: Patterns in python

def triangle(_depth, _type):
        k = 2 * _depth - 2
        for i in range(0, _depth):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i+1):
                print(_type, end=" ")
            print("\r")

def rightTriangle(_depth, _type):
    for i in range(0, _depth):
        for j in range(0, i+1):
            print(_type, end=" ")
        print("\r")

def leftTriangle(_depth, _type):
    k = 2 * _depth - 2
    for i in range(0, _depth):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print(_type, end=" ")
        print("\r")

_choice = int(input(
    "1. Triangle \n2.Right-angle triangle - right \n3.Right-angle triangle - left\n"))
_depth = int(input("Enter depth: "))
_type = input("pattern character: ")

if _choice == 1:
    triangle(_depth, _type)
elif _choice == 2:
    rightTriangle(_depth, _type)
else:
    leftTriangle(_depth, _type)
