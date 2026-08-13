user_name = "Charles"
user_age = 25
wallet_balance = 45.50
is_logged_in = True

# Printing each variable and its type
print("--- Data Type Inspector ---")
print(f"Value: {user_name} | Type: {type(user_name)}")
print(f"Value: {user_age} | Type: {type(user_age)}")
print(f"Value: {wallet_balance} | Type: {type(wallet_balance)}")
print(f"Value: {is_logged_in} | Type: {type(is_logged_in)}")

print(f"Value: {user_name} | Type: {type(user_name).__name__}")