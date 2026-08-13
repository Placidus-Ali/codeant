"""
Simple Interest & Return Calculator
Helps users calculate how much money their investment or savings will grow over time.
"""

# Inputs
amount = float(input("Enter the initial investment amount ($): "))
rate = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
years = float(input("Enter the number of years: "))

# Math Operations (Formula: SI = P * R * T / 100)
interest_earned = (amount * rate * years) / 100
final_balance = amount + interest_earned

# Output with Commas and Currency Formatting
print(" == Investment Growth == ")
print(f"Initial Deposit: ${amount}")
print(f"Interest Earned: ${interest_earned}")
print(f"Total Value after {years} years: ${final_balance}")
