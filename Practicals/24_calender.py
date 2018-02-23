#Practical 24: Calender in python

import calendar

choice = int(input("1.Year \n2.Month: "))

if choice == 1:
    year = input("Year: ")
    for i in range(1, 12):
        print(calendar.month(year, i))

if choice == 2:
    year = input("Year: ")
    month = input("Month: ")
    print(calendar.month(year, month))
