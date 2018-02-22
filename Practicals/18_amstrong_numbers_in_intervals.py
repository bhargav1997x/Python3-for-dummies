#Practical 18: Amstrong number in an interval

value = int(input("upto?: "))
for i in range(1, value): 
    _temp = i       
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if _temp == sum:
         print(_temp)

