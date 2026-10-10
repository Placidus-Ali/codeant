# Step 1:
name1 = input("Enter first student's name: ")
score1 = int(input("Enter first student's score: "))

name2 = input("Enter second student's name: ")
score2 = float(input("Enter second student's score: "))

name3 = input("Enter third student's name: ")
score3 = float(input("Enter third student's score: "))

# Step 2: 
students = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3:
total_score = sum(scores)
average = total_score / 3
highest_score = max(scores)
lowest_score = min(scores)

# Step 4: 
print(total_score)
print(average)
print(highest_score)
print(lowest_score)
