import math

a = input("Enter number\n")
b = input("enter another number\n")
a = float(a)
b = float(b)
key = input("enter operation:1-add, 2-sub, 3-mul, 4-div, 5-pdiv, 6-power\n")

if (key == '4' or '5') and b==0.0 :
        c = input("enter number other than zero\n")
        b = float(c)
        choices = { '4':a/b, '5':int(round(a/b))}
        answer = choices.get(key, 'default')
else :
        choices = {'1':a+b, '2':a-b, '3':a*b, '6':a**b}
        answer = choices.get(key, 'default')

print (answer)