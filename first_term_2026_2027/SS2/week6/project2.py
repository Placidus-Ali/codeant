# Step 1:
name = input("Enter your name: ")
daily_savings = float(input(f"How much do you save daily?: ₦"))

# Step 2:
weekly_savings = daily_savings * 7
monthly_savings = daily_savings * 30
yearly_savings = daily_savings * 365

# Step 3:
print("Hello", name)
print("Your Daily Savings is", daily_savings)
print("Your Weekly Savings is", weekly_savings)
print("Your Monthly Savings", monthly_savings)
print("Your Yearly Savings is", yearly_savings)