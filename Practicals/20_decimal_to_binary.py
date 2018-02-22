#Practical 20: Decimal to binary conversion

value = int(input("Decimal value: "))

base_2 = bin(value)
base_8 = oct(value)
base_16 = hex(value)

print("Binary: ",base_2)
print("Octal: ", base_8)
print("Hexadecimal:", base_16)