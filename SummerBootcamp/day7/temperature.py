"""
Temperature Converter (Dual Direction)
This program allows the user to choose which direction they want to convert, 
handling both Celsius and Fahrenheit cleanly in one script
"""


print("** Temperature Converter **")
name = input("Enter your name: ")
choice = input("Choose an option (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("*" * 40) 
    print(f"Your Temperature is {fahrenheit}°F")
    print("*" * 40) 

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("*" * 40) 
    print(f"Your temperature is {celsius}°C")
    print("*" * 40) 

else:
    print("Invalid choice. Please run the script again and select 1 or 2.")
