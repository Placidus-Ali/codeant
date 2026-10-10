# Step 1: 
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Step 2: 
print("\nChoose an arithmetic operation from below:")
print("Type + for Addition")
print("Type - for Subtraction")
print("Type * for Multiplication")
print("Type / for Division")

operation = input("Enter your chosen operator symbol: ")

# Step 3: 
if operation == "+":
    result = num1 + num2
    print(result)

elif operation == "-":
    result = num1 - num2
    print(result)

elif operation == "*":
    result = num1 * num2
    print(result)

elif operation == "/":
    result = num1 / num2
    print(result)

else:
    print("You entered a wrong operator")