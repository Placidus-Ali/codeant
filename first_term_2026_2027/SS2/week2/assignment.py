# Create a list named 'team' containing these initial members: "Chidi", "Zainab", and "Alice"
# Add a new member named "John" to the end of the list.
# Add a another member named "James" to the very beginning of the list.
# Remove the member "Alice" from the list by using her name.
# Remove the last member from the list.
# Sort the remaining members in alphabetical order.
# Print the final list of the team.



# Create a list with the initial players
team = ["Chidi", "Zainab", "Alice"]

# Add "John" to the end of the list
team.append("John")

# Add "James" to the very beginning of the list
team.insert(0, "James")

# Remove "Alice" from the list by name
team.remove("Alice")

# Remove the last member
team.pop()

# Sort the remaining members in alphabetical order
team.sort()

# Print the final list
print("Final Team:", team)
