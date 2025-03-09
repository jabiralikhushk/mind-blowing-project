
# Unit Converter

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048
    }
    
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    
    value_in_grams = value * weight_units[from_unit]
    return value_in_grams / weight_units[to_unit]


def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.236588
    }
    
    value_in_liters = value * volume_units[from_unit]
    return value_in_liters / volume_units[to_unit]


def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        print("\nChoose a category to convert:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Volume")
        print("5. Exit")
        
        category_choice = input("Enter your choice (1-5): ")

        if category_choice == '1':  # Length Conversion
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from (meters, kilometers, centimeters, millimeters, miles, yards, feet): ").lower()
            to_unit = input("Enter the unit to convert to (meters, kilometers, centimeters, millimeters, miles, yards, feet): ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif category_choice == '2':  # Temperature Conversion
            value = float(input("Enter the temperature value to convert: "))
            from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ").capitalize()
            to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ").capitalize()
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif category_choice == '3':  # Weight Conversion
            value = float(input("Enter the weight value to convert: "))
            from_unit = input("Enter the unit to convert from (grams, kilograms, milligrams, pounds, ounces): ").lower()
            to_unit = input("Enter the unit to convert to (grams, kilograms, milligrams, pounds, ounces): ").lower()
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif category_choice == '4':  # Volume Conversion
            value = float(input("Enter the volume value to convert: "))
            from_unit = input("Enter the unit to convert from (liters, milliliters, cubic_meters, gallons, quarts, pints, cups): ").lower()
            to_unit = input("Enter the unit to convert to (liters, milliliters, cubic_meters, gallons, quarts, pints, cups): ").lower()
            result = convert_volume(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif category_choice == '5':  # Exit
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
