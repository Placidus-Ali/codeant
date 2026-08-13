"""
BMI Calculator
This project calculates the Body Mass Index and uses conditional logic to explain what the number actually means.
"""

# Inputs
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Math Operation
bmi = weight / (height ** 2)

# Determine health category based on standard BMI ranges
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Output with 2-decimal formatting and category injection
print("== BMI Results ==")
print(f"Your calculated BMI is: {bmi:.2f}")
print(f"Health Classification: {category}")
