AHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(temperature):
    global AHRENHEIT_TO_CELSIUS_FACTOR
    return (temperature - 32) * AHRENHEIT_TO_CELSIUS_FACTOR
    

def convert_to_fahrenheit(temperature):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = float(input("Enter the temperature to convert: "))
conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if conversion_type == 'C':
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temperature}°F")

elif conversion_type == 'F':
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temperature}°C")

else:
    print("Invalid temperature. Please enter a numeric value.")