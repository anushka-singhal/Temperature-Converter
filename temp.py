def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {kelvin:.2f}K")

    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin}K is equal to {celsius:.2f}°C")

    elif choice == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F is equal to {kelvin:.2f}K")

    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin}K is equal to {fahrenheit:.2f}°F")

    else:
        print("Invalid choice. Please enter a valid option (1-6).")
