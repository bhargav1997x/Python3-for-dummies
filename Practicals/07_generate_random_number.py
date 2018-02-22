#Practical 7: Program to generate random number

import os
import random

choice = input("1. Range \n2. Without Range\n")
if choice == 1:
    lower_range = input("Lower range: ")
    upper_range = input("Upper range: ")
    step = input("Step: ")
    print("Random Value: ", random.randrange(lower_range, upper_range, step))

else:
    value =random.SystemRandom()
    print("Random value: ", value.random() * 20);