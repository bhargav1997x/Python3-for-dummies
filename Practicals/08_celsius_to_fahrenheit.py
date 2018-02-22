#Practical 8: Convert celsius to fahrenheit

#Celsius = Fahrenheit - 32 / 1.8
#Fahrenheit = celsius / 0.55 + 32

def convertCelcius():
    x = input("Fahrenheit: ")
    print("In celsius: ", (x - 32) / 1.8)

def convertFahrenheit():
    x = input("Celsius: ")
    print("In Fahrenheit", x / 0.55 + 32)

def main():
    choice = input("1. Fahrenheit to Celsius \n2. Celsius to Fahrenheit\n")
    if choice == 1:
        convertCelcius()
    else:
        convertFahrenheit()

if __name__ == '__main__':
    main()
