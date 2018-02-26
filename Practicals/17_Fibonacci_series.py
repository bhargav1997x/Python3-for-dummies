#Practical 17: Fibonacci series 

value = int(input("How many terms? "))

# first two terms
_n1 = 0
_n2 = 1
count = 0
# check if the number of terms is valid
if value <= 0:
   print("Please enter a positive integer")
elif value == 1:
   print("Fibonacci sequence upto",value,":")
   print(_n1)
else:
   print("Fibonacci sequence upto",value,":")
   while count < value:
       print(_n1,end=' , ')
       nth = _n1 + _n2
       # update values
       _n1 = _n2
       _n2 = nth
       count += 1