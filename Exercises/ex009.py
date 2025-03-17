# Your Student ID:230543019
# Your Name and Surname:IBRAHIM TAHA PINAR
def temperatureCalculator():
    option = int(input("Please Choose Temperature Conversion:\nPress 1 for Celsius to Fahrenheit\nPress 2 for Fahrenheit to Celsius\n"))
    if option != 1 and option != 2:
        print("Invalid option! Please enter 1 or 2.")
        return 0
    temperature = int(input("Please enter a temperature to convert: "))
    if option == 1:
        convertedTemperature = (temperature * 9/5) + 32
        print(f"Your input temperature in Fahrenheit : {convertedTemperature:.1f}")
    elif option == 2:
        convertedTemperature = (temperature - 32) * 5/9
        print(f"Your input temperature in Celcius : {convertedTemperature:.1f}")
    
        
temperatureCalculator()