"""
Age in Days, Weeks, and Months Calculator
Takes a user's age in years and breaks it down into other time units.
"""
# Inputs
name = input("Enter your name: ")
age_years = int(input("Enter your age in years: "))

# Math Operations
months = age_years * 12
weeks = age_years * 52
days = age_years * 365

# Output 
print("== Time Report for ==")
print(f"You have lived: {months:,} Months")
print(f"You have lived: {weeks:,} Weeks")
print(f"You have lived: {days:,} Days")
