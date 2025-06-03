FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp_in_c = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_in_c

def convert_to_fahrenheit(celsius):
    temp_in_f = (celsius + 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_in_f

temp = float(input("Enter the temperature to convert: "))
user_input = input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()

if user_input == "c":
    temp_in_f = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {temp_in_f}°F")
elif user_input == "f":
    temp_in_c = convert_to_celsius(temp)
    print(f"{temp}°C is {temp_in_c}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")