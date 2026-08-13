# write a python script that request for name and score from a student. If the score it less than 50, 
# it will say the person failed, but if the score is above 50, the person passed.

name = input("What is your name: ")
score = int(input("What is your score: "))

# Check if the student passed or failed
if score >= 50:
    result = "passed. Well-done"
else:
    result = "failed. Try again"

# Prints everything on the same line
print(f"Hello, {name}! Your score is {score}. You {result}!") 
