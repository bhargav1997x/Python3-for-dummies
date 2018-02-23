#Practical 34: Set operations in python

set_1 = {}
set_2 = {}
value = int(input("No. of values in set 1: "))
for i in range(0, value):
    temp = int(input())
    set_1.update(temp)
   
value = int(input("No. of values in set 2: "))
for i in range(0, value):
    temp = int(input())
    set_2.update(temp)

# set union 
print("Union is",set_1 | set_2 )

# set intersection 
print("Intersection is",set_1 & set_2)

# set difference 
print("Difference is",set_1 - set_2)

# set symmetric difference 
print("Symmetric difference is",set_1 ^ set_2)
