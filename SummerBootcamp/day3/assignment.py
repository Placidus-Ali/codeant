# Assignment

"""
Filename: student_card.py
Create a program that generates a customized Student ID card by taking user input and printing it in two different styles.

Instructions:
Part 1
a. Use a single line comment above your input section to explain what you are doing.
b. Use an inline comment next to one of your print() statements to what is does

Part 2: Inputs
Request for the student's Name, School, and Grade.

Part 3: Outputs
a. Print the details on the same line using the + operator to join the strings together.
b. Print a customized profile card using separate print() lines framed with decorative dashes (---).
"""

# Part 2: 
name = input("Enter student name: ")
school = input("Enter school name: ")
grade = input("Enter grade: ")

print("\n" + "=" * 40)

# Part 3 - a
print("Name: " + name + " | School: " + school + " | Grade: " + grade) # Joins all strings together with +

print("\n" + "=" * 40)

# Part 3 - b
print("--- STUDENT PROFILE CARD ---")
print("--------------------------------")
print("Name: " + name)
print("School: " + school)
print("Grade: " + grade)
print("--------------------------------")